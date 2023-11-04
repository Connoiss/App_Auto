import os
import subprocess
import psutil
import serial
import serial.tools.list_ports
import threading
import binascii
import time

from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from appium import webdriver as app_web
from pywinauto.application import Application
from pywinauto import mouse

# default value
baunRate = 115200
is_read = False
is_write = False
write_buff = []
sys_buff = []
mSerial = None
callback = None
is_opened = 0
is_registed = 0
global receive


class states_game:
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(500, 300)
        self.window.setWindowTitle('应用自动化')

        self.button1 = QPushButton('打开Malody', self.window)
        self.button1.move(100, 80)
        if proc_exist('Appium.exe'):
            self.button1.clicked.connect(self.handleCalc_dnplayer)
            self.button1.clicked.connect(self.handleCalc_Malody)
        elif proc_exist('dnplayer.exe') and proc_exist('Appium.exe'):
            self.button1.clicked.connect(self.handleCalc_Malody)
        else:
            self.button1.clicked.connect(self.handleCalc_Appium)
            self.button1.clicked.connect(self.handleCalc_dnplayer)
            self.button1.clicked.connect(self.handleCalc_Malody)

        self.button2 = QPushButton('打开Maipaid', self.window)
        self.button2.move(300, 80)
        if proc_exist('Appium.exe'):
            self.button1.clicked.connect(self.handleCalc_dnplayer)
            self.button1.clicked.connect(self.handleCalc_Maipaid)
        elif proc_exist('dnplayer.exe') and proc_exist('Appium.exe'):
            self.button1.clicked.connect(self.handleCalc_Maipaid)
        else:
            self.button1.clicked.connect(self.handleCalc_Appium)
            self.button1.clicked.connect(self.handleCalc_dnplayer)
            self.button1.clicked.connect(self.handleCalc_Maipaid)

        # self.button3 = QPushButton('打开qq', self.window)
        # self.button3.move(100, 180)
        # self.button3.clicked.connect(self.handleCalc3)
        #
        # self.button4 = QPushButton('打开bibi', self.window)
        # self.button4.move(300, 180)
        # self.button4.clicked.connect(self.handleCalc4)

        # self.button5 = QPushButton('打开Appium', self.window)
        # self.button5.move(100, 180)
        # self.button5.clicked.connect(self.handleCalc5)
        #
        # self.button6 = QPushButton('打开模拟器', self.window)
        # self.button6.move(300, 180)
        # self.button6.clicked.connect(self.handleCalc6)

        self.button7 = QPushButton('账号系统', self.window)
        self.button7.move(200, 300)
        self.button7.clicked.connect(self.handleCalc_User)

    def handleCalc_Malody(self):
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

    def handleCalc_Maipaid(self):
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

    def handleCalc_QQ(self):
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

    def handleCalc_bilibili(self):
        desired_caps = {
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': '9',  # 手机安卓版本
            'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
            'appPackage': 'tv.danmaku.bili',  # 启动APP Package名称tv.danmaku.bili
            'appActivity': '.MainActivityV2',  # 启动Activity名称.MainActivityV2}
            'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            'noReset': True,  # 不要重置App
            'newCommandTimeout': 6000,
            'automationName': 'UiAutomator2'
            # 'app': r'd:\apk\bili.apk',
        }
        driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def handleCalc_Appium(self):
        app = Application("uia").start(r"C:\Users\22203\AppData\Local\Programs\Appium\Appium.exe")
        dlg = app["Appium"]
        dlg.wait(wait_for="ready", timeout=60, retry_interval=1)
        mouse.click(button="left", coords=(970, 640))
        dlg.minimize()

    def handleCalc_dnplayer(self):
        Application("uia").start(r"D:\leidian\LDPlayer9\dnplayer.exe")
        # dlg = app["LDPlayerMainFrame"]
        # dlg.wait(wait_for="ready", timeout=60, retry_interval=1)
        # # time.sleep(20)
        # mouse.click(button="left",coords=(1775,20))

    def handleCalc_User(self):
        str = (
            r'python S:\本科\创业园1104耀视达\手台\各模块\py\打开模拟器\appium自动化py程序\程序\用户信息采集系统\jietupipei.py')
        os.system(str)


class SerialPort:

    def __init__(self, port, buand):

        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

        # the index of data_bytes for read operation,私有属性
        # only used in read lines
        self.__read_ptr = 0
        self.__read_head = 0
        # store all read bytes
        # used in read date， read lines
        self.__data_bytes = bytearray()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send(self):
        global is_write
        global write_buff

        while is_write:
            if len(write_buff):
                msg = write_buff.pop(0)
                msg = msg + "\n"
                cmd = msg.encode()
                try:

                    self.port.write(cmd)
                except:
                    write_buff.clear()
                    is_write = False
        write_buff.clear()

    def read_data(self):
        global is_read
        global is_opened
        byte_cnt = 0
        while is_read:
            try:
                count = self.port.inWaiting()
                if count > 0:
                    rec_str = self.port.read(count)
                    self.__data_bytes = self.__data_bytes + rec_str
                    # print("receive:",rec_str.decode())
                    # print(rec_str)
                    byte_cnt += count
                    if not is_opened:
                        is_opened = 1
                # print("累计收到：",byte_cnt)
                # time.sleep(0.5)
                self.read_lines()
            except:
                deinit()

    # 将当前所有的数据都读出，读取位置不变，每次读取指针依次移动，不漏数据， 读取行为一直在进行
    def read_lines(self):
        # reset
        line_cnt = 0
        data_len = len(self.__data_bytes)
        # print ("")
        # print ("begin: prt=:", self.__read_ptr, " head =", self.__read_head,"current len =",data_len)
        if self.__read_ptr >= data_len:
            return
        # get all lines in current data_bytes
        while self.__read_ptr < data_len - 1:
            if self.__data_bytes[self.__read_ptr + 1] == 0x0a and self.__data_bytes[self.__read_ptr] == 0x0d:
                tmp = bytearray()
                tmp = self.__data_bytes[self.__read_head:self.__read_ptr]

                try:
                    line = tmp.decode()
                except:
                    self.__read_head = self.__read_ptr + 2
                    self.__read_ptr = self.__read_head
                    continue
                iprint(line)
                line_cnt += 1
                self.__read_head = self.__read_ptr + 2
                self.__read_ptr = self.__read_head
            else:
                self.__read_ptr = self.__read_ptr + 1


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == process_name:
            return pid


def auto_open_serial():
    global baunRate
    global mSerial
    global callback
    global is_registed
    global is_opened
    # reset
    deinit()
    # 列出所有当前的com口
    port_list = list(serial.tools.list_ports.comports())
    port_list_name = []
    # get all com
    if len(port_list) <= 0:
        iprint("the serial port can't find!")
        return False
    else:
        for itms in port_list:
            port_list_name.append(itms.device)
    # try open
    # print(port_list_name)
    for i in port_list_name:
        try:
            mSerial = SerialPort(i, baunRate)
            iprint("try open %s" % i)
            start_task()
            send("")
            # return True
            time.sleep(1)
            if is_opened:
                iprint("connect %s successfully" % i)
                return True
            else:
                deinit()
                if i == port_list_name[len(port_list_name) - 1]:
                    iprint("uart don't open")
                    break
                continue
        except:
            iprint(" uart don't open")
    deinit()
    return False


def deinit():
    global mSerial
    global is_write
    global is_read
    global write_buff
    global is_opened

    if mSerial:
        mSerial.port_close()

    is_opened = 0
    is_read = False
    is_write = False
    write_buff = []

    mSerial = None
    time.sleep(1)


def init():
    global mSerial
    global callback
    global is_registed
    global is_opened
    global is_read
    global is_write
    # retry
    retry_time = 0
    while not auto_open_serial():
        if not is_opened:
            iprint("wait for uart connect, retry %s" % str(retry_time))
        else:
            return True
        retry_time += 1
        time.sleep(2)
        if retry_time == 10:
            iprint(" open uart fail")
            return False


def send(msg):
    global mSerial
    global is_write
    global write_buff
    if is_write:
        write_buff.append(msg)


def start_task():
    global mSerial
    global is_write
    global is_read

    if mSerial:
        is_write = True
        t1 = threading.Thread(target=mSerial.send)
        t1.setDaemon = False
        t1.start()

        is_read = True
        t2 = threading.Thread(target=mSerial.read_data)
        t2.setDaemon = False
        t2.start()


def iprint(msg):
    global callback
    global is_registed

    msg = "[Uart] " + str(msg)
    if is_registed:
        callback.append(msg)
    else:
        print(msg)


def start_sys_cmd():
    global is_registed
    if is_registed:
        t3 = threading.Thread(target=process_receive_sys_cmd)
        t3.setDaemon = False
        t3.start()


def process_receive_sys_cmd():
    global sys_buff
    global is_registed
    global callback
    # print("process_receive_sys_cmd")
    while is_registed:
        # print ("wait,process_receive_sys_cmd")
        if len(sys_buff):
            # print ("receive,process_receive_sys_cmd")
            line = sys_buff.pop(0)
            if "init" in line:
                if is_opened and is_read and is_write:
                    iprint("already open uart")
                    break
                iprint("start init")
                init()
        if is_opened:
            break
    iprint("Eixt uart sys thread")


def register_cback(list):
    global callback
    global is_registed

    callback = list
    is_registed = 1


def unregister_cback():
    global callback
    callback.clear()


def process_receive_msg():
    # global receive
    while True:
        # print("wait")
        if len(receive):
            # print("receive")
            print(receive.pop(0))


def FindUARTConnect():
    receive = []
    register_cback(receive)
    sys_buff.append("init")
    start_sys_cmd()

    t = threading.Thread(target=process_receive_msg)
    t.setDaemon = False
    t.start()


if __name__ == '__main__':
    # FindUART&Connect()
    app = QApplication([])
    states = states_game()
    states.window.show()

    app.exec()


