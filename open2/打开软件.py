from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox
from appium import webdriver as app_web

class states():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(500, 300)
        self.window.setWindowTitle('open.py')
#textEdit = QPlainTextEdit(window)
#textEdit.setPlaceholderText("请输入薪资表")
#textEdit.move(10, 25)
#textEdit.resize(300, 350)
        self.button1 = QPushButton('打开Malody', self.window)
        self.button1.move(100, 80)
        self.button1.clicked.connect(self.handleCalc1)

        self.button2 = QPushButton('打开Maipaid', self.window)
        self.button2.move(300, 80)
        self.button2.clicked.connect(self.handleCalc2)

        self.button3 = QPushButton('打开qq', self.window)
        self.button3.move(100, 180)
        self.button3.clicked.connect(self.handleCalc3)

        self.button4 = QPushButton('打开bibi', self.window)
        self.button4.move(300, 180)
        self.button4.clicked.connect(self.handleCalc4)

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
                "appActivity": "com.unity3d.player.UnityPlayerActivity",  # com.unity3d.player.UnityPlayerActivity
                "noReset": True,
                "unicodekeyboard": True,
                "resetkeyboard": True
            }
        driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def handleCalc3(self):
        desired_caps = {
            'platformName': 'Android',  # ?????????????????
            'udid  ': 'emulator-5554',  # ??????????豸??Ψ??豸?????
            'deviceName': 'deviceName',  # ????????豸?????????????
            'platformVersion': '9',  # ??????????汾
            'appPackage': 'com.tencent.mobileqq',  # apk????com.tencent.mobileqq
            'appActivity': '.activity.SplashActivity',  # apk??launcherActivity/.activity.SplashActivity
            'unicodeKeyboard': True,  # ???unicodeKeyboard?????????????????
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
states.window.show()

app.exec_()
