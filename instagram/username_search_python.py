# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'username_search_python.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_search(object):
    def setupUi(self, search):
        search.setObjectName("search")
        search.resize(480, 640)
        self.lb_text_followers = QtWidgets.QLabel(search)
        self.lb_text_followers.setGeometry(QtCore.QRect(20, 100, 151, 16))
        self.lb_text_followers.setObjectName("lb_text_followers")
        self.lb_text_follows = QtWidgets.QLabel(search)
        self.lb_text_follows.setGeometry(QtCore.QRect(260, 100, 151, 16))
        self.lb_text_follows.setObjectName("lb_text_follows")
        self.le_search = QtWidgets.QLineEdit(search)
        self.le_search.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.le_search.setObjectName("le_search")
        self.pb_okey = QtWidgets.QPushButton(search)
        self.pb_okey.setGeometry(QtCore.QRect(170, 20, 91, 21))
        self.pb_okey.setObjectName("pb_okey")
        self.lw_followers = QtWidgets.QListWidget(search)
        self.lw_followers.setGeometry(QtCore.QRect(20, 130, 201, 471))
        self.lw_followers.setObjectName("lw_followers")
        self.lw_follows = QtWidgets.QListWidget(search)
        self.lw_follows.setGeometry(QtCore.QRect(240, 130, 221, 471))
        self.lw_follows.setObjectName("lw_follows")
        self.pb_reset = QtWidgets.QPushButton(search)
        self.pb_reset.setGeometry(QtCore.QRect(280, 20, 91, 21))
        self.pb_reset.setObjectName("pb_reset")

        self.retranslateUi(search)
        QtCore.QMetaObject.connectSlotsByName(search)

    def retranslateUi(self, search):
        _translate = QtCore.QCoreApplication.translate
        search.setWindowTitle(_translate("search", "Form"))
        self.lb_text_followers.setText(_translate("search", "Followers:"))
        self.lb_text_follows.setText(_translate("search", "Follows:"))
        self.pb_okey.setText(_translate("search", "Okey"))
        self.pb_reset.setText(_translate("search", "Reset"))
