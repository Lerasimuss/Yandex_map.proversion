# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scale_2 = QtWidgets.QLabel(self.centralwidget)
        self.scale_2.setGeometry(QtCore.QRect(0, 550, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.scale_2.setFont(font)
        self.scale_2.setObjectName("scale_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(100, 560, 101, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.coor_y = QtWidgets.QLabel(self.centralwidget)
        self.coor_y.setGeometry(QtCore.QRect(0, 510, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.coor_y.setFont(font)
        self.coor_y.setObjectName("coor_y")
        self.coor_x = QtWidgets.QLabel(self.centralwidget)
        self.coor_x.setGeometry(QtCore.QRect(0, 470, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.coor_x.setFont(font)
        self.coor_x.setObjectName("coor_x")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(100, 480, 101, 31))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(100, 520, 101, 31))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.widget_map = QtWidgets.QWidget(self.centralwidget)
        self.widget_map.setGeometry(QtCore.QRect(9, 19, 781, 441))
        self.widget_map.setObjectName("widget_map")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scale_2.setText(_translate("MainWindow", "Масштаб:"))
        self.coor_y.setText(_translate("MainWindow", "Y:"))
        self.coor_x.setText(_translate("MainWindow", "X:"))
