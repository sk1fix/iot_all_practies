# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/Ycheba/iot_all_practies/less6/des.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(760, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(110, 510, 75, 23))
        self.pause.setObjectName("pause")
        self.screenShot = QtWidgets.QPushButton(self.centralwidget)
        self.screenShot.setGeometry(QtCore.QRect(390, 510, 75, 23))
        self.screenShot.setObjectName("screenShot")
        self.save_but = QtWidgets.QPushButton(self.centralwidget)
        self.save_but.setGeometry(QtCore.QRect(660, 510, 75, 23))
        self.save_but.setObjectName("save_but")
        self.sett_but = QtWidgets.QPushButton(self.centralwidget)
        self.sett_but.setGeometry(QtCore.QRect(770, 510, 75, 23))
        self.sett_but.setObjectName("sett_but")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 80, 421, 301))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(670, 90, 281, 191))
        self.widget_2.setObjectName("widget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Видеопоток"))
        self.pause.setText(_translate("MainWindow", "Пауза"))
        self.screenShot.setText(_translate("MainWindow", "Снимок"))
        self.save_but.setText(_translate("MainWindow", "Сохранить"))
        self.sett_but.setText(_translate("MainWindow", "Настройки"))
