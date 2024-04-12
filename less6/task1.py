import sys
from main import Ui_MainWindow
from main1 import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer, QTime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QLabel, QOpenGLWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import os

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.video_label = QVideoWidget()
        self.video_label.resize(521, 391)  # Set the size of the widget (width, height)
        self.video_label.move(60, 30)  # Set the position of the widget (x, y)
        
        self.video_player = QMediaPlayer(self)
        self.video_player.setVideoOutput(self.video_label)
        
        self.image_label = self.ui.widget_2
        self.ui.pause.clicked.connect(self.pause_b)
        self.ui.save_but.clicked.connect(self.save_b)
        self.ui.screenShot.clicked.connect(self.screen_b)
        self.ui.sett_but.clicked.connect(self.sett_b)
        self.ui.radioButton.clicked.connect(self.radio_b)
        
        self.video_player.stateChanged.connect(self.video_state_changed)
    def pause_b(self):
        pass

    def save_b(self):
        pass

    def screen_b(self):
        pass

    def sett_b(self):
        self.menu = SettingsWindow(self)
        self.menu.show()

    def radio_b(self):
        pass
    
    def video_state_changed(self, state):
        if state == QMediaPlayer.EndOfMedia:
            self.video_player.setPosition(0)

class SettingsWindow(QtWidgets.QDialog, Ui_Form):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.lab = self.ui.label
        self.lab1 = self.ui.label_2
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
        video_path, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi)")
        media = QMediaContent(QUrl.fromLocalFile(video_path))
        self.main_window.video_player.setMedia(media)  # Устанавливаем медиафайл для проигрывания
        self.main_window.video_player.play()  # Запускаем воспроизведение
        self.close()  # Закрываем окно SettingsWindow
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())