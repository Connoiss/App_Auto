from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from appium import webdriver as app_web


class states():
    def __init__(self):
        uii = QFile("S://本科//创业园1104耀视达//手台//各模块//py//打开模拟器//appium自动化py程序//程序//打开模拟器软件.ui")
        uii.open(QFile.ReadOnly)
        uii.close()

        self.ui = QUiLoader().load(uii)
        self.ui.pushButton_2.clicked.connect(self.handleCalc1)
        self.ui.pushButton_3.clicked.connect(self.handleCalc2)
        self.ui.pushButton_4.clicked.connect(self.handleCalc3)
        self.ui.pushButton_5.clicked.connect(self.handleCalc4)

    def handleCalc1(self):
        desired_caps = {
                "platformName": "Android",
                "platformVersion": "9",
                "deviceName": "emulator-5554",
                "appPackage": "me.mugzone.malody",  # me.mugzone.malody
                "appActivity": ".AppActivity",  # /.AppActivity
                "noReset": True,
                "unicodekeyboard": True,
                "resetkeyboard": True
            }
        driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def handleCalc2(self):
        desired_caps = {
                "platformName": "Android",
                "platformVersion": "9",
                "deviceName": "emulator-5554",
                "appPackage": "com.Reflektone.MaipadDX",  # com.Reflektone.MaipadDX
                "appActivity": "com.unity3d.player.UnityPlayerActivity",
                "noReset": True,
                "unicodekeyboard": True,
                "resetkeyboard": True
            }
        driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def handleCalc3(self):
        desired_caps = {
            'platformName': 'Android',
            'udid  ': 'emulator-5554',  #
            'deviceName': 'deviceName',  #
            'platformVersion': '9',  #
            'appPackage': 'com.tencent.mobileqq',  #
            'appActivity': '.activity.SplashActivity',  #
            'unicodeKeyboard': True,  #
            'noReset': True,
        }
        driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def handleCalc4(self):
       desired_caps = {
           'platformName': 'Android', # 被测手机是安卓
           'platformVersion': '9', # 手机安卓版本
           'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
           'appPackage': 'tv.danmaku.bili', # 启动APP Package名称tv.danmaku.bili
           'appActivity': '.MainActivityV2', # 启动Activity名称.MainActivityV2}
           'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
           'resetKeyboard': True, # 执行完程序恢复原来输入法
           'noReset': True,       # 不要重置App
           'newCommandTimeout': 6000,
           'automationName': 'UiAutomator2'
        #'app': r'd:\apk\bili.apk',
       }
       driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


app = QApplication([])
states = states()

states.ui.show()

app.exec_()