import sys
from main import Ui_MainWindow
from main1 import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer, QTime
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import os

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pause.clicked.connect(self.pause_b)
        self.ui.save_but.clicked.connect(self.save_b)
        self.ui.screenShot.clicked.connect(self.screen_b)
        self.ui.sett_but.clicked.connect(self.sett_b)
        self.ui.radioButton.clicked.connect(self.radio_b)
    
    def pause_b(self):
        pass

    def save_b(self):
        pass

    def screen_b(self):
        pass

    def sett_b(self):
        self.menu = SettingsWindow()
        self.menu.show()

    def radio_b(self):
        pass

class SettingsWindow(QtWidgets.QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.lab = self.ui.label
        self.lab1 = self.ui.label_2
        self.lab2 = self.ui.label_3
        self.ui.radioButton.clicked.connect(self.open_file)
        self.ui.radioButton_2.clicked.connect(self.ethernet_vid)
        self.ui.radioButton_3.clicked.connect(self.camera_stream)
        self.ui.pushButton.clicked.connect(self.file_path)

    def open_file(self):
        pass

    def ethernet_vid(self):
        pass

    def camera_stream(self):
        pass

    def file_path(self):
        pass
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())