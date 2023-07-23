#!/usr/bin/python3

# TODO: A single connection to stream.binance.com is only valid for 24 hours; expect to be disconnected at the 24 hour mark. So we must close and reconnect every day
# Stream types and other things described here: https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md

# we need this package:
#   > pip3 install websocket-client
import websocket
import datetime
import time
import ssl
import json
import sys
import subprocess


# define some things:
tradepairs = ['BTCUSDT', 'ETHUSDT', 'LTCUSDT']
logpath = "./"
scriptlog = logpath+"_script.log"

# We will restart script after 23 hours
restarttime = datetime.datetime.now() + datetime.timedelta(hours=23)



def on_message(ws, message):
    try:
        object = json.loads(message)
        if 'result' in object:
            return  # it's just subscribe response
        print(f"{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}: rcv {object['s']}/{object['e']}")
        filename = f"{logpath}{object['s']}_{object['e']}_{datetime.datetime.now().strftime('%Y%m%d_%H')}.log"
        with open(filename, "a") as file:
            file.write(f'{message}\n')
        # restart script
        if datetime.datetime.now() >= restarttime:
            print("restarting script")
            subprocess.Popen([sys.argv[0]], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            sys.exit(0)
    except Exception as e:
        print(f'W(!) Oops! We got an exception: {str(e)}')


def on_error(ws, error):
    print(f"(!) Oops! we got an fehler '{error}'")

def on_close(ws, ex, x):
    print("### closed ###")


def on_open(ws):
    # Live Subscribing on WSS open:
    for id, pair in enumerate(tradepairs):
        subscribe = {"method": "SUBSCRIBE", "params": [f"{pair.lower()}@aggTrade", f"{pair.lower()}@depth"], "id": id + 1}
        ws.send(json.dumps(subscribe))


if __name__ == "__main__":
    sys.stdout = open(scriptlog, "a")
    # uncomment this for debug
    # websocket.enableTrace(True)
    print(f"{datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S')} starting..")
    ws = websocket.WebSocketApp("wss://stream.binance.com:443/ws",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=on_open)
    try:
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    except KeyboardInterrupt:
        print("###User interrupted###")
    sys.exit()
