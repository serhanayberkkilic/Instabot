# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_python.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(480, 640)
        self.label = QtWidgets.QLabel(settings)
        self.label.setGeometry(QtCore.QRect(160, 10, 141, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("6641c94e15a0be37af49a4250386c03e.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_Im = QtWidgets.QLabel(settings)
        self.label_Im.setGeometry(QtCore.QRect(0, 330, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Im.setFont(font)
        self.label_Im.setObjectName("label_Im")
        self.label_arenot = QtWidgets.QLabel(settings)
        self.label_arenot.setGeometry(QtCore.QRect(230, 320, 231, 63))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_arenot.setFont(font)
        self.label_arenot.setObjectName("label_arenot")
        self.label_flallow = QtWidgets.QLabel(settings)
        self.label_flallow.setGeometry(QtCore.QRect(10, 210, 339, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_flallow.setFont(font)
        self.label_flallow.setObjectName("label_flallow")
        self.label_fallowers = QtWidgets.QLabel(settings)
        self.label_fallowers.setGeometry(QtCore.QRect(10, 140, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_fallowers.setFont(font)
        self.label_fallowers.setObjectName("label_fallowers")
        self.lb_post = QtWidgets.QLabel(settings)
        self.lb_post.setGeometry(QtCore.QRect(10, 250, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_post.setFont(font)
        self.lb_post.setObjectName("lb_post")
        self.list_widget_imnot = QtWidgets.QListWidget(settings)
        self.list_widget_imnot.setGeometry(QtCore.QRect(10, 371, 201, 211))
        self.list_widget_imnot.setObjectName("list_widget_imnot")
        self.list_widget_arenot = QtWidgets.QListWidget(settings)
        self.list_widget_arenot.setGeometry(QtCore.QRect(240, 370, 201, 211))
        self.list_widget_arenot.setObjectName("list_widget_arenot")

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Form"))
        self.label_Im.setText(_translate("settings", "I\'m Not Following Back:"))
        self.label_arenot.setText(_translate("settings", "Are Not Following Back:"))
        self.label_flallow.setText(_translate("settings", "Fallow:"))
        self.label_fallowers.setText(_translate("settings", "Fallowers:"))
        self.lb_post.setText(_translate("settings", "Post:"))
