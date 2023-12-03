import subprocess
import uartorigin
import sys

from appium import webdriver as app_web
from pywinauto.application import Application
from pywinauto import mouse
from PySide6.QtUiTools import QUiLoader
from Modeselect import Ui_ModeSelection
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QTimer, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton, QSizePolicy,
                               QWidget)


class Ui_Connecting(QWidget):  # 连接中界面
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        if uartorigin.auto_open_serial():
            QTimer.singleShot(1000, self.openWelcome)  # 等1000ms后打开欢迎界面
            self.handleCalc_Appium()  # 打开Appium，不然模拟器用不了脚本
        else:
            QTimer.singleShot(3500, self.openConnnectFailed)

    def openWelcome(self):  # 打开欢迎界面
        self.close()
        self.Welcome = Ui_Main()
        self.Welcome.show()

    def openConnnectFailed(self):  # 打开连接失败界面
        self.close()
        self.ConnectFailed = Ui_Form()
        self.ConnectFailed.show()

    def handleCalc_Appium(self):  # 打开Appium和点击连接服务器
        app = Application("uia").start(r"C:\Users\22203\AppData\Local\Programs\Appium\Appium.exe")
        dlg = app["Appium"]
        dlg.wait(wait_for="ready", timeout=60, retry_interval=1)
        mouse.click(button="left", coords=(970, 640))
        dlg.minimize()

    def setupUi(self, Connecting):
        if not Connecting.objectName():
            Connecting.setObjectName(u"Connecting")
        Connecting.resize(400, 300)
        self.gridLayout = QGridLayout(Connecting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Connecting_2 = QLabel(Connecting)
        self.Connecting_2.setObjectName(u"Connecting_2")
        self.gridLayout.addWidget(self.Connecting_2, 0, 0, 1, 1)
        self.retranslateUi(Connecting)
        QMetaObject.connectSlotsByName(Connecting)

    # setupUi

    def retranslateUi(self, Connecting):
        Connecting.setWindowTitle(QCoreApplication.translate("Connecting", u"Connecting\u2026\u2026", None))
        self.Connecting_2.setText(QCoreApplication.translate("Connecting",
                                                             u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">\u8fde\u63a5\u8bbe\u5907\u4e2d\u2026\u2026\u2026\u2026</span></p></body></html>",
                                                             None))
    # retranslateUi


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.activity()

    def back(self):  # 返回到连接界面
        self.close()
        self.back = Ui_Connecting()
        self.back.show()

    def activity(self):
        self.pushButton.clicked.connect(self.back)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Failed", u"Failed", None))
        self.label.setText(QCoreApplication.translate("Failed",
                                                      u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">\u8fde\u63a5\u5931\u8d25\uff01\u8bf7\u68c0\u67e5\u8bbe\u5907\u8fde\u63a5</span></p></body></html>",
                                                      None))
        self.pushButton.setText(QCoreApplication.translate("Failed", u"\u786e\u5b9a", None))
    # retranslateUi


class Ui_Main(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.handleButton()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def openRegisterWin(self):  # 打开注册界面
        # os.system("register.exe")
        self.close()
        subprocess.call("register.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

    def openLoginWin(self):  # 打开登录界面
        # os.system("login.exe")
        self.close()
        subprocess.call("login.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def handleButton(self):  # 信号，槽连接
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
        # if QT_CONFIG(whatsthis)
        Main.setWhatsThis(QCoreApplication.translate("Main",
                                                     u"<html><head/><body><p>\u91cd\u6784\u5f0f\u97f3\u6e38\u624b\u53f0</p></body></html>",
                                                     None))
        # endif // QT_CONFIG(whatsthis)
        self.Welcome.setText(QCoreApplication.translate("Main",
                                                        u"<html><head/><body><p align=\"center\">\u6b22\u8fce\u4f7f\u7528\u672c\u8f6f\u4ef6</p></body></html>",
                                                        None))
        self.ButtonLogin.setText(QCoreApplication.translate("Main", u"\u767b\u5f55", None))
        self.ButtonSignup.setText(QCoreApplication.translate("Main", u"\u6ce8\u518c", None))
    # retranslateUi


if __name__ == '__main__':
    app = QApplication([])
    window = Ui_Connecting()
    window.show()
    app.exec()
