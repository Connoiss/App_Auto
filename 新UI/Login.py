# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_Login(QtWidgets.QWidget):
    current_user = None  # 用于存储当前登录账号的类变量

    def __init__(self):
        super().__init__()
        self.current_user = None
        self.setupUi(self)
        self.handleButton()

    def loginAction(self):
        self.login.setText("登录中")
        user_name = self.getID()
        password = self.getPwd()
        if self.check_data_existence('user_name', user_name):
            if self.check_data_existence('user_password', password):
                self.current_user = user_name  # 设置当前登录账号，传参给其他页面
                self.openSelectWin()
            else:
                QMessageBox.warning(self, '提示', '密码错误，请重新输入')
        else:
            self.ifintoregist()
        self.login.setText("登录")

    def getID(self):  # 获取用户名
        return self.lineEdit.text()

    def getPwd(self):  # 获取密码
        return self.lineEdit_2.text()

    def openRegisterWin(self):  # 打开注册界面
        subprocess.call("register1.exe", shell=True)

    def openSelectWin(self):  # 打开模式选择界面
        subprocess.call("Modeselect.exe", shell=True)

    def check_data_existence(self, column, value):  # 检查数据是否在数据库
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
                return True
            else:
                return False

        except pymysql.Error as err:
            print(f"Error: {err}")

        finally:
            # 关闭连接
            if connection and connection.open:
                cursor.close()
                connection.close()

    def ifintoregist(self):  # 是否进入注册界面函数
        msgBox = QMessageBox()
        msgBox.setWindowTitle('提示')
        msgBox.setText('用户名不存在，是否注册账号？ ')
        # 添加自定义按钮，并将其点击事件连接到自定义槽函数
        yes_button = msgBox.addButton(QMessageBox.Yes)
        yes_button.clicked.connect(self.openRegisterWin)
        no_button = msgBox.addButton(QMessageBox.No)
        no_button.clicked.connect(msgBox.close)
        # 设置默认按钮
        msgBox.setDefaultButton(QMessageBox.Yes)
        msgBox.exec()

    def handleButton(self):  # 信号，槽连接
        self.login.clicked.connect(self.loginAction)
        self.lineEdit.textChanged.connect(self.getID)
        self.lineEdit_2.textChanged.connect(self.getPwd)
        self.signup.clicked.connect(self.openRegisterWin)

    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(400, 290)
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 371, 181))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.widget1 = QWidget(Login)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(120, 210, 158, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.login = QPushButton(self.widget1)
        self.login.setObjectName(u"login")

        self.horizontalLayout_2.addWidget(self.login)

        self.signup = QPushButton(self.widget1)
        self.signup.setObjectName(u"signup")

        self.horizontalLayout_2.addWidget(self.signup)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText(QCoreApplication.translate("Login",
                                                      u"<html><head/><body><p><span style=\" font-size:18pt;\">\u7528\u6237\u540d</span></p></body></html>",
                                                      None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("Login", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Login",
                                                        u"<html><head/><body><p><span style=\" font-size:18pt;\">\u5bc6\u7801</span></p></body></html>",
                                                        None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Login", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.login.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.signup.setText(QCoreApplication.translate("Login", u"\u6ce8\u518c", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication([])
    win = Ui_Login()
    win.show()
    app.exec()
