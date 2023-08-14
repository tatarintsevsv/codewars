from PyQt5 import  QtSql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError, QSqlDriver

from PyQt5 import QtCore, QtWidgets
import sys
from datetime import datetime
from time import sleep

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QtWidgets.QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        self.spin = QtWidgets.QSpinBox(self.central_widget)
        self.combo = QtWidgets.QComboBox(self.central_widget)
        self.combo.addItems({"1", "2", "3", "4"})

        self.grid_layout.addWidget(self.spin, 0, 0)
        self.grid_layout.addWidget(self.combo, 1, 0)
        self.cfg = QtCore.QSettings("MY_TEST", "SETTINGS")


        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setUserName("postgres")  # postgres is the default root username
        self.db.setPassword("1qaz@WSX3edc")  # add your password here
        self.db.setHostName("localhost")
        self.db.setDatabaseName("postgres")
        print("Available drivers", self.db.drivers())

        if not self.db.open():
            print("Unable to connect.")
            print('Last error', self.db.lastError().text())
            exit(0)
        else:
            print("Connection to the database successful")
        self.db.driver().subscribeToNotification("SAVED")
        self.db.driver().notification['QString', 'QSqlDriver::NotificationSource', 'QVariant'].connect(self.onNotification)
        #self.db.driver().notification[
        #    str, QtSql.QSqlDriver.NotificationSource, "QVariant"
        #].connect(self.onNotification)
        #print(f"Error: {self.db.lastError().text()}")


        self.q = QSqlQuery()
        if not self.q.exec("delete from speedtest"):
            print(f"Error: {self.q.lastError().text()}")
            exit(0)
        for i in range(1000):
            t = QtCore.QDateTime.currentDateTime()
            self.q.prepare("insert into speedtest (id, t_start) values (?, ?)")
            self.q.addBindValue(i)
            self.q.addBindValue(t)
            if not self.q.exec():
                print(f"Error: {self.q.lastError().text()}")
            sleep(0.001)
        #quit(0)

    #@QtCore.pyqtSlot(str, QtSql.QSqlDriver.NotificationSource, "QVariant")
    def onNotification(self, name, source, payload):
        print(name, source, payload)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())