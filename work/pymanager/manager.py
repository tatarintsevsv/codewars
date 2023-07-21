#!/usr/bin/python3
import json
import requests
import sys
import os
import os.path
import time
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
token = '6347021317:AAGa8NnGpPiV-LtbosqryRzZlPIjE3GRWXs'
#https://api.telegram.org/bot6347021317:AAGa8NnGpPiV-LtbosqryRzZlPIjE3GRWXs/getUpdates
#https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}
sendmessage_url = f'https://api.telegram.org/bot{token}/sendMessage'
updatemarkup_url = f'https://api.telegram.org/bot{token}/editMessageText'


proxies = {
   'http': 'http://192.168.22.70:3128',
   'https': 'http://192.168.22.70:3128',
}



class Loader:
    def __init__(self):
        self.scriptlist = ('cfgloader.py','cfgloader2.py')
        pass

    def sendScriptCmd(self, query, chat_id, message_id=-1):
        if query[:5] == "start":
            cmd = [f"disown `./{query[6:]}`&"]
        elif query[:4] == "stop":
            cmd = [f"kill `pidof {query[6:]} &`"]
        else:
            return
        p = subprocess.Popen(cmd,shell=True, start_new_session=True, stdout=subprocess.PIPE)
        #out, err = p.communicate()
        #text = out
        #requests.post(sendmessage_url, data=f"CMD {cmd}", proxies=proxies)

    def sendScriptCmdKbd(self, query, chat_id, message_id=-1):
        p = subprocess.Popen(f"ps -aux|grep {query}",shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        text = out
        keyboard = {
            "inline_keyboard": [[{"text": "Запуск", "callback_data": f"start_{query}"},{"text": "Останов", "callback_data": f"stop_{query}"} ]],
            "resize_keyboard": True
        }
        data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(keyboard)}
        if message_id == -1:
            r = requests.post(sendmessage_url, data=data, proxies=proxies)
        else:
            data['message_id'] = message_id
        r = requests.post(updatemarkup_url, data=data, proxies=proxies)

    def sendScriptKbd(self, query, chat_id, message_id=-1):
        keyboard = {
            "inline_keyboard": [],
            "resize_keyboard": True
        }
        for s in self.scriptlist:
            keyboard["inline_keyboard"].append([{"text": f"{s}", "callback_data": f"script_{s}"}])
        data = {'chat_id': chat_id, 'text' : 'Выбирай скрипт','reply_markup': json.dumps(keyboard)}
        if message_id == -1:
            r = requests.post(sendmessage_url, data=data, proxies=proxies)
        else:
            data['message_id'] = message_id
        print(data)
        r = requests.post(updatemarkup_url, data=data, proxies=proxies)
        print(r.text)

    def sendQueryType(self, chat, text, message_id=-1):
        keyboard = {
        "inline_keyboard": [[{"text": "Скрипты", "callback_data": "scriptlist"}, {"text": "Статус", "callback_data": "status"}]],
        "resize_keyboard": True
        }
        data = {'chat_id': chat, 'text': text, 'reply_markup': json.dumps(keyboard)}
        if message_id == -1:
            r = requests.post(sendmessage_url, data=data, proxies=proxies)
        else:
            data['message_id'] = message_id
        r = requests.post(updatemarkup_url, data=data, proxies=proxies)

    def processMessage(self,data):
        msg = json.loads(data)
        type = list(msg)[-1]
        if type == 'message':
            cmd = msg['message'].get('text')
            id = msg['message']['chat']['id']
            self.sendQueryType(id, 'Чего изволим?')
        if type == 'callback_query':
            message_id = msg['callback_query']['message']['message_id']
            chat_id = msg['callback_query']['message']['chat']['id']
            query = msg['callback_query']['data']
            if query == 'scriptlist':
                self.sendScriptKbd(query, chat_id, message_id)
            elif query[:7] == 'script_':
                self.sendScriptCmdKbd(query[7:], chat_id, message_id)
            elif query.split('_')[0] in ('start', 'stop'):
                self.sendScriptCmd(query, chat_id, message_id)


l=Loader()

#data = sys.stdin.read()
data='''
{
"callback_query":{"id":"7249580257444447434","from":{"id":1687924437,"is_bot":false,"first_name":"\u0421\u0435\u0440\u0433\u0435\u0439","last_name":"\u0422\u0430\u0442\u0430\u0440\u0438\u043d\u0446\u0435\u0432","username":"tsv_kraskript","language_code":"ru"},
"message":{"message_id":3,"from":{"id":6347021317,"is_bot":true,"first_name":"botva-plotva","username":"AnPyManagerTestBot"},
"chat":{"id":1687924437,"first_name":"\u0421\u0435\u0440\u0433\u0435\u0439","last_name":"\u0422\u0430\u0442\u0430\u0440\u0438\u043d\u0446\u0435\u0432","username":"tsv_kraskript","type":"private"},"date":1689912856,"edit_date":1689914709,"text":"...grep cfgloader.py","entities":[{"offset":91,"length":12,"type":"url"},{"offset":195,"length":12,"type":"url"}],"reply_markup":{"inline_keyboard":[[{"text":"\u0417\u0430\u043f\u0443\u0441\u043a",
"callback_data":"start_cfgloader.py"},{"text":"\u041e\u0441\u0442\u0430\u043d\u043e\u0432","callback_data":"stop_cfgloader.py"}]]}},
"chat_instance":"6299339272676359786","data":"start_cfgloader.py"
}}
'''
l.processMessage(data)