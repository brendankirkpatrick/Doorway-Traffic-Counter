import sys
import os
import threading
import requests
import datetime
import config
from time import  sleep, strftime, gmtime

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickWindow
from PyQt5.QtCore import QObject, pyqtSignal

class Backend(QObject):

    def __init__(self):
        QObject.__init__(self)

    time = pyqtSignal(str, arguments=['update_time'])
    def update_time(self, curr_time):
         self.time.emit(curr_time)

    peopleIn = pyqtSignal(int, arguments=['update_peopleIn'])
    peopleOut = pyqtSignal(int, arguments=['update_peopleOut'])

    def update_data(self):
        try:
            date = datetime.date.today()
            URL = config.url + '/dataOnDate'
            PARAMS = {'date': date}
            response = requests.get(url = URL, params=PARAMS, timeout=15)
            r = response.json()
            if (r["error"] != None):
                print("Received Error!:" + r.error)
                self.peopleIn.emit(-1)
                self.peopleOut.emit(-1)
            data = r["data"]
            self.peopleIn.emit(data[0])
            self.peopleOut.emit(data[1])
        except:
            print("Error fetching data")
            self.peopleIn.emit(-1)
            self.peopleOut.emit(-1)

    def bootUp(self):
            t_thread = threading.Thread(target=self._bootUp)
            t_thread.daemon = True
            t_thread.start()

    def _bootUp(self):
        while True:
            curr_time = str(datetime.datetime.now())
            self.update_time(curr_time)
            self.update_data()

QQuickWindow.setSceneGraphBackend('software')

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./Application/UI/main.qml')

back_end = Backend()

engine.rootObjects()[0].setProperty('backend', back_end)

back_end.bootUp()

sys.exit(app.exec())
