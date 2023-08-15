from PyQt5.QtCore import *
import sys
from time import sleep
from random import choices
"""


 sigStart    -------------   sigInited   -------------     sigDataReceived        /--------------/  
------------>| steteInit |-------------->| stateWork |.......................>   /   writeData  /.......................> /* data analyze */
             -------------               -------------                          /______________/
                   ^                            |         
                   |                            |
         sigStart  |      --------------        | sigErrorOccurred
                   -------| stateError |<--------
                          --------------


"""

class Machine(QObject):
    # Прописываем сигналы состояний
    sigStart = pyqtSignal()
    sigInited = pyqtSignal()
    sigDataReceived = pyqtSignal()
    sigErrorOccurred = pyqtSignal()

    def __init__(self):
        super(Machine, self).__init__()
        # Создаем автомат конечных состояний
        self.machine = QStateMachine(self)
        # Создаем состояния автомата
        self.stateInit = QState(self.machine)
        self.stateWork = QState(self.machine)
        self.stateError = QState(self.machine)

        self.stateInit.setProperty("name", "stateInit")
        self.stateWork.setProperty("name", "stateWork")
        self.stateError.setProperty("name", "stateError")
        # Соединяем событие "вход в состояние" со слотами обработки
        # Если необходимо обрабатывать событие выхода из состояния, прописываем соответствующие .exited.connect()
        self.stateInit.entered.connect(self.initWS)
        self.stateWork.entered.connect(self.startWS)
        self.stateError.entered.connect(self.errorWS)
        # Прописываем переходы между состояниями
        self.stateInit.addTransition(self.sigInited, self.stateWork)
        self.stateWork.addTransition(self.sigErrorOccurred, self.stateError)
        self.stateError.addTransition(self.sigStart, self.stateInit)
        # Указываем в каком состоянии будет автомат при запуске
        self.machine.setInitialState(self.stateInit)
        self.machine.start()
        # Привяжем к сигналу получения данных слот записи
        self.sigDataReceived.connect(self.writeData)

    def printConfig(self):
        print("  current config: ",end="")
        for s in self.machine.configuration():
            print(f"{s.property('name')} ",end="")
        print("")

    def initWS(self):
        self.printConfig()
        print("initializing WS")
        sleep(3)
        self.sigInited.emit()

    def startWS(self):
        while True:
            x = choices([1, 2], [0.8, 0.2])[0]
            if x == 1:
                print("WS data Received", end="")
                self.sigDataReceived.emit()
            else:
                print("WS error", end="")
                self.sigErrorOccurred.emit()
                break
            sleep(0.5)

    def errorWS(self):
        print("    error processing")
        sleep(3)
        self.sigStart.emit()
        pass

    def writeData(self):
        print("    writing data")
        # something like this
        # aggTrade,1685069309937,BTCUSDT,2639467436,26439.83000000,0.00200000,3126584653,3126584653,1685069309936,True,True



if __name__ == '__main__':
    app = QCoreApplication(sys.argv)
    m = Machine()
    sys.exit(app.exec_())

