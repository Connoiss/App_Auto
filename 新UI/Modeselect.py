# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '模式选择.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import pymysql
import psutil
import os
import serial
import uartorigin
import register1

from Login import Ui_Login
from pywinauto import mouse
from pywinauto.application import Application
from appium import webdriver as app_web
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QPushButton, QSizePolicy, QWidget)


class Ui_ModeSelection(QWidget):
    is_mode = 0
    mode_list = [0, 0, 0, 0, 0, 0]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.activity()
        self.is_mode = 0
        self.update_mode_list()

    def activity(self):
        self.Select.currentIndexChanged.connect(self.handle_selection_change)  # 当下拉框选择项发生变化时触发

    def handle_selection_change(self):
        if self.is_mode:
            self.ok.clicked.disconnect()
        # 根据选择的模式更新计数
        mode_mapping = {
            "二键模式": 55,
            "四键模式": 54,
            "六键模式": 53,
            "八键模式": 52,
            "九键模式": 51,
            "舞立方": 50
        }
        selected_text = self.Select.currentText()
        self.is_mode = mode_mapping.get(selected_text, 0)
        # 在界面上显示推荐模式
        print(self.is_mode)
        favor_mode = self.check_data_existence('favor_mode', Ui_Login.current_user)
        recommended_mode = favor_mode[3] if favor_mode[3] else "无"
        self.RecommendedMode.setText(recommended_mode)
        self.ok.clicked.connect(self.OK_clicked)

    def OK_clicked(self):
        global serial_port
        print("is_mode:", self.is_mode)
        if self.is_mode == 55:  # 2k
            if self.proc_exist('dnplayer.exe'):
                self.end_program('dnplayer.exe')
            self.mode_list[0] += 1
            self.ok.clicked.connect(self.handleCalc_MushDash())
        elif self.is_mode == 54:  # 4k
            if self.proc_exist('dnplayer.exe'):
                self.end_program('dnplayer.exe')
            self.mode_list[1] += 1
            self.ok.clicked.connect(self.handleCalc_Malody())
        elif self.is_mode == 53:  # 6k
            if self.proc_exist('MuseDash.exe'):
                self.end_program('MuseDash.exe')
            self.mode_list[2] += 1
            self.ok.clicked.connect(self.handleCalc_Malody())
        elif self.is_mode == 52:  # 8k
            if self.proc_exist('MuseDash.exe'):
                self.end_program('MuseDash.exe')
            self.mode_list[3] += 1
            self.ok.clicked.connect(self.handleCalc_Malody())
        elif self.is_mode == 51:  # 9k
            if self.proc_exist('MuseDash.exe'):
                self.end_program('MuseDash.exe')
            self.mode_list[4] += 1
            self.ok.clicked.connect(self.handleCalc_Malody())
        elif self.is_mode == 50:  # 5LF
            if self.proc_exist('MuseDash.exe'):
                self.end_program('MuseDash.exe')
            self.mode_list[5] += 1
            self.ok.clicked.connect(self.handleCalc_Malody())
        self.sendtosql()  # 上传推荐模式至数据库
        try:
            serial_port = serial.Serial(uartorigin.auto_open_serial(), 115200, 8, 'N', 1)
            send_hex = bytes.fromhex(str(self.is_mode))  # 将模式转换为字符串
            serial_port.write(send_hex)  # 调用串口发送函数发送数字
            self.is_mode = 0
            a = serial_port.read()  # 读取串口数据
            print(a)
        except Exception as e:
            print(f"串口连接和发送失败: {e}")
        finally:
            serial_port.close()

    def generate(self, mode):  # 排序得出推荐模式
        max_key = max(range(len(mode)), key=lambda i: mode[i])
        key_names = ["二键", "四键", "六键", "八键", "九键", "舞立方"]

        # self.sendtosql(max_key_names[max_key])
        # self.sendtosql(max_key_names[min_key])
        return key_names[max_key]

    def check_data_existence(self, column, value):
        global connection, cursor
        try:
            # 连接到 MySQL 数据库
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='123456',
                database='remaimai'
            )
            # 创建游标对象
            cursor = connection.cursor()
            # 执行查询，检查数据是否存在
            query = f"SELECT * FROM re2 WHERE {column} = %s"
            cursor.execute(query, (value,))
            # 获取查询结果
            result = cursor.fetchone()
            # 检查结果是否存在
            if result:
                return result
            else:
                return False
        except pymysql.Error as err:
            print(f"Error: {err}")
        finally:
            # 关闭连接
            if connection and connection.open:
                cursor.close()
                connection.close()

    def sendtosql(self):  # 上传推荐模式至数据库
        mode_str = ''.join(map(str, self.mode_list))
        db = pymysql.connect(host="localhost", user="root", password="123456", database='remaimai')
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute("use remaimai")
            cursor.execute("UPDATE re2 SET favor_mode=\"{}\" modes=\"{}\" WHERE user_name=\"{}\"; ".format(
                self.generate(self.mode_list),
                mode_str,
                Ui_Login.current_user))
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
        # 关闭数据库连接
        db.close()

    def update_mode_list(self):
        # 从数据库获取存储的字符串
        favor_mode = self.check_data_existence('favor_mode', Ui_Login.current_user)
        if favor_mode[3]:
            mode_str = favor_mode[3]
            # 将字符串解析为列表
            self.mode_list = [int(char) for char in mode_str]

    # 进程检测
    def proc_exist(self, process_name):
        pl = psutil.pids()
        for pid in pl:
            if psutil.Process(pid).name() == process_name:
                return pid

    # 进程关闭
    def end_program(self, pro_name):
        os.system('%s%s' % ("taskkill /F /IM ", pro_name))

    def handleCalc_Malody(self):
        Application("uia").start(r"D:\leidian\LDPlayer9\dnplayer.exe")
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
        Application("uia").start(r"D:\leidian\LDPlayer9\dnplayer.exe")
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

    def handleCalc_MushDash(self):
        os.startfile(r'P:\SteamLibrary\steamapps\common\Muse Dash\MuseDash.exe')

    # activity
    def setupUi(self, ModeSelection):
        if not ModeSelection.objectName():
            ModeSelection.setObjectName(u"ModeSelection")
        ModeSelection.resize(384, 240)
        self.gridLayout = QGridLayout(ModeSelection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Recommend = QLabel(ModeSelection)
        self.Recommend.setObjectName(u"Recommend")

        self.gridLayout.addWidget(self.Recommend, 1, 0, 1, 1)

        self.RecommendedMode = QLabel(ModeSelection)
        self.RecommendedMode.setObjectName(u"RecommendedMode")

        self.gridLayout.addWidget(self.RecommendedMode, 1, 1, 1, 1)

        self.Select = QComboBox(ModeSelection)
        self.Select.addItem("")
        self.Select.addItem("")
        self.Select.addItem("")
        self.Select.addItem("")
        self.Select.addItem("")
        self.Select.addItem("")
        self.Select.setObjectName(u"Select")

        self.gridLayout.addWidget(self.Select, 0, 0, 1, 2)

        self.ok = QPushButton(ModeSelection)
        self.ok.setObjectName(u"ok")
        self.ok.setAutoDefault(False)

        self.gridLayout.addWidget(self.ok, 2, 0, 1, 2)

        self.retranslateUi(ModeSelection)

        QMetaObject.connectSlotsByName(ModeSelection)

    # setupUi

    def retranslateUi(self, ModeSelection):
        ModeSelection.setWindowTitle(QCoreApplication.translate("ModeSelection", u"\u6a21\u5f0f\u9009\u62e9", None))
        self.Recommend.setText(QCoreApplication.translate("ModeSelection",
                                                          u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u63a8\u8350\u6a21\u5f0f\uff1a</span></p></body></html>",
                                                          None))
        self.RecommendedMode.setText(QCoreApplication.translate("ModeSelection", u"SomeMode", None))
        self.Select.setItemText(0, QCoreApplication.translate("ModeSelection", u"\u4e8c\u952e\u6a21\u5f0f", None))
        self.Select.setItemText(1, QCoreApplication.translate("ModeSelection", u"\u56db\u952e\u6a21\u5f0f", None))
        self.Select.setItemText(2, QCoreApplication.translate("ModeSelection", u"\u516d\u952e\u6a21\u5f0f", None))
        self.Select.setItemText(3, QCoreApplication.translate("ModeSelection", u"\u516b\u952e\u6a21\u5f0f", None))
        self.Select.setItemText(4, QCoreApplication.translate("ModeSelection", u"\u4e5d\u952e\u6a21\u5f0f", None))
        self.Select.setItemText(5, QCoreApplication.translate("ModeSelection", u"\u821e\u7acb\u65b9", None))

        self.Select.setPlaceholderText(
            QCoreApplication.translate("ModeSelection", u"\u8bf7\u9009\u62e9\u6a21\u5f0f", None))
        self.ok.setText(QCoreApplication.translate("ModeSelection", u"\u786e\u5b9a", None))
    # retranslateUi


if __name__ == '__main__':
    app = QApplication([])
    window = Ui_ModeSelection()
    window.show()
    app.exec()
