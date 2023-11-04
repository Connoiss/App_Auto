# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtWidgets
import subprocess
import pymysql
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDialog, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)
# import os

class Ui_login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.handleButton()

    def loginAction(self):
        self.loginBu.setText("登录中")
        # print(self.chosenType)
        # print(type(self.usrID))
        db = pymysql.connect(host="localhost", user="root", password="", charset="utf8")
        csor = db.cursor()
        csor.execute("use librarymanager")
        if self.chosenType == "用户":
            pass
        elif self.chosenType == "管理员":
            pass


    def typeOfUsr(self):
        self.chosenType = self.usrType.checkedButton().text()

    def getID(self):
        self.usrID = self.ID.text()

    def getPwd(self):
        self.usrpwd = self.pwd.text()

    def openRegisterWin(self):
        # os.system("register.exe")
        subprocess.call("register.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def handleButton(self):
        self.loginBu.clicked.connect(self.loginAction)
        self.usrType.buttonClicked.connect(self.typeOfUsr)
        self.ID.textChanged.connect(self.getID)
        self.pwd.textChanged.connect(self.getPwd)
        self.signBu.clicked.connect(self.openRegisterWin)

    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(400, 300)
        login.setMinimumSize(QSize(400, 300))
        login.setMaximumSize(QSize(400, 300))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(9)
        login.setFont(font)
        icon = QIcon()
        icon.addFile(u"test/LibIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        login.setWindowIcon(icon)
        self.usrRadioButton = QRadioButton(login)
        self.usrType = QButtonGroup(login)
        self.usrType.setObjectName(u"usrType")
        self.usrType.addButton(self.usrRadioButton)
        self.usrRadioButton.setObjectName(u"usrRadioButton")
        self.usrRadioButton.setGeometry(QRect(110, 40, 115, 19))
        self.AdmRadioButton = QRadioButton(login)
        self.usrType.addButton(self.AdmRadioButton)
        self.AdmRadioButton.setObjectName(u"AdmRadioButton")
        self.AdmRadioButton.setGeometry(QRect(220, 40, 115, 19))
        self.tipForID = QLabel(login)
        self.tipForID.setObjectName(u"tipForID")
        self.tipForID.setGeometry(QRect(80, 100, 72, 15))
        self.ID = QLineEdit(login)
        self.ID.setObjectName(u"ID")
        self.ID.setGeometry(QRect(140, 100, 161, 21))
        self.tipForPwd = QLabel(login)
        self.tipForPwd.setObjectName(u"tipForPwd")
        self.tipForPwd.setGeometry(QRect(100, 160, 72, 15))
        self.pwd = QLineEdit(login)
        self.pwd.setObjectName(u"pwd")
        self.pwd.setGeometry(QRect(140, 160, 161, 21))
        self.pwd.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.pwd.setEchoMode(QLineEdit.Password)
        self.loginBu = QPushButton(login)
        self.loginBu.setObjectName(u"loginBu")
        self.loginBu.setGeometry(QRect(90, 230, 93, 28))
        self.loginBu.setMouseTracking(True)
        self.loginBu.setTabletTracking(True)
        self.loginBu.setFocusPolicy(Qt.ClickFocus)
        self.loginBu.setStyleSheet(u"color: rgb(121, 186, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.signBu = QPushButton(login)
        self.signBu.setObjectName(u"signBu")
        self.signBu.setGeometry(QRect(220, 230, 93, 28))
        self.signBu.setCursor(QCursor(Qt.ArrowCursor))
        self.signBu.setFocusPolicy(Qt.StrongFocus)
        self.signBu.setStyleSheet(u"color: rgb(121, 186, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.signBu.setInputMethodHints(Qt.ImhNone)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"\u56fe\u4e66\u7ba1\u7406\u7cfb\u7edf-\u767b\u5f55", None))
        self.usrRadioButton.setText(QCoreApplication.translate("login", u"\u7528\u6237", None))
        self.AdmRadioButton.setText(QCoreApplication.translate("login", u"\u7ba1\u7406\u5458", None))
        self.tipForID.setText(QCoreApplication.translate("login", u"\u8d26\u53f7ID:", None))
        self.ID.setPlaceholderText(QCoreApplication.translate("login", u"\u8bf7\u8f93\u5165\u8d26\u53f7ID", None))
        self.tipForPwd.setText(QCoreApplication.translate("login", u"\u5bc6\u7801:", None))
        self.pwd.setPlaceholderText(QCoreApplication.translate("login", u"\u8bf7\u8f93\u5165\u767b\u5f55\u5bc6\u7801", None))
        self.loginBu.setText(QCoreApplication.translate("login", u"\u767b\u5f55", None))
        self.signBu.setText(QCoreApplication.translate("login", u"\u6ce8\u518c", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    win = Ui_login()
    win.show()
    app.exec()