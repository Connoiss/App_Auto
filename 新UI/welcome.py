# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReDesignedMAIMAI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!################################################################################

from PySide6 import QtWidgets
import subprocess

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Main(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.handleButton()

    def openRegisterWin(self):
        # os.system("register.exe")
        subprocess.call("register.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def openLoginWin(self):
        # os.system("login.exe")
        subprocess.call("login.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def handleButton(self):
        self.ButtonLogin.clicked.connect(self.openLoginWin)
        self.ButtonSignup.clicked.connect(self.openRegisterWin)

    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setEnabled(True)
        Main.resize(400, 300)
        Main.setMinimumSize(QSize(400, 300))
        self.gridLayout = QGridLayout(Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Welcome = QLabel(Main)
        self.Welcome.setObjectName(u"Welcome")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.Welcome.setFont(font)
        self.Welcome.setTabletTracking(False)

        self.gridLayout.addWidget(self.Welcome, 0, 0, 1, 1)

        self.ButtonLogin = QPushButton(Main)
        self.ButtonLogin.setObjectName(u"ButtonLogin")
        self.ButtonLogin.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.ButtonLogin, 1, 0, 1, 1)

        self.ButtonSignup = QPushButton(Main)
        self.ButtonSignup.setObjectName(u"ButtonSignup")

        self.gridLayout.addWidget(self.ButtonSignup, 2, 0, 1, 1)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"ReDesignedMAIMAI", None))
#if QT_CONFIG(whatsthis)
        Main.setWhatsThis(QCoreApplication.translate("Main", u"<html><head/><body><p>\u91cd\u6784\u5f0f\u97f3\u6e38\u624b\u53f0</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Welcome.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\">\u6b22\u8fce\u4f7f\u7528\u672c\u8f6f\u4ef6</p></body></html>", None))
        self.ButtonLogin.setText(QCoreApplication.translate("Main", u"\u767b\u5f55", None))
        self.ButtonSignup.setText(QCoreApplication.translate("Main", u"\u6ce8\u518c", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication([])
    window = Ui_Main()
    window.show()
    app.exec()