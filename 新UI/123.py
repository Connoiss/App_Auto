# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication
import sys
import pymysql

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_register(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.activities()

    def getID(self):
        self.ID = self.IDiput.text()

    def doRe(self):
        # print(type(self.ID),self.ID)
        # print(self.ID,self.usrName,self.usrGender,self.contact,self.compa,self.career,self.fstpwd,self.pwdsecond)
        try:
            a = False
            b = self.usrGender
            c = False
            for i in self.ID:
                if 33 <= ord(i) <= 126:
                    continue
                else:
                    a = True
            for i in self.pwdsecond:
                if 33 <= ord(i) <= 126:
                    continue
                else:
                    c = True
            if a:
                IDwrong = QMessageBox()
                # IDwrong.setWindowIcon("libIcon.ico")
                IDwrong.setWindowTitle("ID格式错误!")
                IDwrong.setText("ID只能由英文字母、数字和部分英文字符组成!")
                IDwrong.exec()
            elif self.fstpwd != self.pwdsecond:
                pwdwrong = QMessageBox()
                pwdwrong.setWindowTitle("密码错误!")
                pwdwrong.setText("两次输入的密码不一致!")
                pwdwrong.exec()
            elif len(self.fstpwd) > 16 or len(self.fstpwd) < 6:
                pw = QMessageBox()
                pw.setWindowTitle("密码错误!")
                pw.setText("密码必须6~16位!")
                pw.exec()
            else:
                db = pymysql.connect(host="localhost",user="root",password="",charset="utf8")
                csor = db.cursor()
                csor.execute("use librarymanager")
                csor.execute("select * from rpwd;")
                readers = csor.fetchall()
                # print(readers)
                for i in readers:
                    if self.ID == i[0]:
                        IdrepeatError = QMessageBox()
                        IdrepeatError.setWindowTitle("用户ID错误!")
                        IdrepeatError.setText("已经存在该ID用户，请换一个ID!")
                        IdrepeatError.exec()
                # print(readers)
                    else:
                        # sql = "insert into rpwd values (\"{}\",\"{}\")".format(self.ID,self.pwdsecond)
                        # print(sql)
                        csor.execute("insert into rpwd values (\"{}\",\"{}\")".format(self.ID,self.pwdsecond))
                        csor.execute("select * from rpwd;")
                        readers = csor.fetchall()
                        for i in readers:
                            # print(i)
                            if self.ID == i[0]:
                                suc = QMessageBox()
                                suc.setWindowTitle("成功!")
                                suc.setText("您已成功注册成为本图书馆用户!")
                                suc.exec()
                                break
                        csor.execute("insert into rdinfo values (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(self.ID,
                                                                                                           self.usrName,
                                                                                                           self.contact,
                                                                                                           self.usrGender,
                                                                                                           self.compa,
                                                                                                           self.career))
                        db.commit()
                        break
                    db.close()
                    csor.close()
        except AttributeError:
            owrong = QMessageBox()
            owrong.setWindowTitle("错误!")
            owrong.setText("请填写信息!")
            owrong.exec()
    def closeEvent(self,event):
        sys.exit(0)

    def getName(self):
        self.usrName = self.name.text()

    def getGender(self):
        self.usrGender = self.gender.checkedButton().text()

    def getPhoneOrEmail(self):
        self.contact = self.company_2.text()

    def getCompany(self):
        self.compa = self.company.text()

    def getType(self):
        self.career = self.usrType.text()

    def getFstpwd(self):
        self.fstpwd = self.firstPwd.text()

    def getSecpwd(self):
        self.pwdsecond = self.secPwd.text()

    def activities(self):
        self.doRegister.clicked.connect(self.doRe)
        self.IDiput.textChanged.connect(self.getID)
        self.IDiput.textChanged.connect(self.getID)
        self.usrType.textChanged.connect(self.getType)
        self.company.textChanged.connect(self.getCompany)
        self.company_2.textChanged.connect(self.getPhoneOrEmail)
        self.gender.buttonClicked.connect(self.getGender)
        self.name.textChanged.connect(self.getName)
        self.IDiput.textChanged.connect(self.getID)
        self.firstPwd.textChanged.connect(self.getFstpwd)
        self.secPwd.textChanged.connect(self.getSecpwd)
        self.cancel.clicked.connect(self.closeEvent)

    def setupUi(self, register_2):
        if not register_2.objectName():
            register_2.setObjectName(u"register_2")
        register_2.resize(634, 484)
        register_2.setMinimumSize(QSize(634, 484))
        register_2.setMaximumSize(QSize(634, 484))
        icon = QIcon()
        icon.addFile(u"LibIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        register_2.setWindowIcon(icon)
        self.label = QLabel(register_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 71, 16))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        self.label.setFont(font)
        self.IDiput = QLineEdit(register_2)
        self.IDiput.setObjectName(u"IDiput")
        self.IDiput.setGeometry(QRect(180, 30, 371, 20))
        self.label_2 = QLabel(register_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 80, 71, 16))
        self.label_2.setFont(font)
        self.name = QLineEdit(register_2)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(180, 80, 371, 20))
        self.maleRa = QRadioButton(register_2)
        self.gender = QButtonGroup(register_2)
        self.gender.setObjectName(u"gender")
        self.gender.addButton(self.maleRa)
        self.maleRa.setObjectName(u"maleRa")
        self.maleRa.setGeometry(QRect(250, 130, 95, 20))
        self.femaleRa = QRadioButton(register_2)
        self.gender.addButton(self.femaleRa)
        self.femaleRa.setObjectName(u"femaleRa")
        self.femaleRa.setGeometry(QRect(360, 130, 95, 20))
        self.label_3 = QLabel(register_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 210, 131, 16))
        self.label_3.setFont(font)
        self.company = QLineEdit(register_2)
        self.company.setObjectName(u"company")
        self.company.setGeometry(QRect(180, 210, 371, 20))
        self.label_4 = QLabel(register_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 130, 101, 20))
        self.label_4.setFont(font)
        self.label_5 = QLabel(register_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 330, 131, 16))
        self.label_5.setFont(font)
        self.label_7 = QLabel(register_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 310, 131, 16))
        self.label_7.setFont(font)
        self.firstPwd = QLineEdit(register_2)
        self.firstPwd.setObjectName(u"firstPwd")
        self.firstPwd.setGeometry(QRect(180, 310, 371, 20))
        self.firstPwd.setEchoMode(QLineEdit.Password)
        self.label_8 = QLabel(register_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 360, 131, 16))
        self.label_8.setFont(font)
        self.secPwd = QLineEdit(register_2)
        self.secPwd.setObjectName(u"secPwd")
        self.secPwd.setGeometry(QRect(180, 360, 371, 20))
        self.secPwd.setEchoMode(QLineEdit.Password)
        self.label_9 = QLabel(register_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 260, 131, 16))
        self.label_9.setFont(font)
        self.usrType = QLineEdit(register_2)
        self.usrType.setObjectName(u"usrType")
        self.usrType.setGeometry(QRect(180, 260, 371, 20))
        self.doRegister = QPushButton(register_2)
        self.doRegister.setObjectName(u"doRegister")
        self.doRegister.setGeometry(QRect(150, 410, 81, 31))
        self.cancel = QPushButton(register_2)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(420, 410, 81, 31))
        self.label_6 = QLabel(register_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 170, 131, 20))
        self.label_6.setFont(font)
        self.company_2 = QLineEdit(register_2)
        self.company_2.setObjectName(u"company_2")
        self.company_2.setGeometry(QRect(180, 170, 371, 20))

        self.retranslateUi(register_2)

        QMetaObject.connectSlotsByName(register_2)
    # setupUi

    def retranslateUi(self, register_2):
        register_2.setWindowTitle(QCoreApplication.translate("register_2", u"\u56fe\u4e66\u7ba1\u7406\u7cfb\u7edf-\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("register_2", u"\u8bf7\u8f93\u5165ID :", None))
        self.IDiput.setPlaceholderText(QCoreApplication.translate("register_2", u"ID\u53EA\u80FD\u7531\u82F1\u6587\u5B57\u6BCD\u3001\u6570\u5B57\u548C\u90E8\u5206\u82F1\u6587\u5B57\u7B26\u7EC4\u6210", None))
        self.label_2.setText(QCoreApplication.translate("register_2", u"\u8bf7\u8f93\u5165\u59d3\u540d:", None))
        self.name.setPlaceholderText(QCoreApplication.translate("register_2", u"\u8bf7\u8f93\u5165\u60a8\u7684\u59d3\u540d", None))
        self.maleRa.setText(QCoreApplication.translate("register_2", u"\u7537", None))
        self.femaleRa.setText(QCoreApplication.translate("register_2", u"\u5973", None))
        self.label_3.setText(QCoreApplication.translate("register_2", u"\u8bf7\u8f93\u5165\u60a8\u6240\u5728\u5355\u4f4d :", None))
        self.company.setPlaceholderText(QCoreApplication.translate("register_2", u"\u5b66\u6821\u6216\u4f01\u4e1a\u5355\u4f4d", None))
        self.label_4.setText(QCoreApplication.translate("register_2", u"\u8bf7\u9009\u62e9\u60a8\u7684\u6027\u522b :", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("register_2", u"\u8bf7\u8f93\u5165\u60a8\u7684\u5bc6\u7801 :", None))
        self.firstPwd.setPlaceholderText(QCoreApplication.translate("register_2", u"\u8bf7\u8f93\u5165\u60a8\u7684\u5bc6\u7801\uFF0C\u53EA\u80FD\u7531\u82F1\u6587\u5B57\u6BCD\u3001\u6570\u5B57\u548C\u90E8\u5206\u82F1\u6587\u5B57\u7B26\u7EC4\u6210", None))
        self.label_8.setText(QCoreApplication.translate("register_2", u"\u8bf7\u786e\u8ba4\u60a8\u7684\u5bc6\u7801 :", None))
        self.secPwd.setPlaceholderText(QCoreApplication.translate("register_2", u"\u8bf7\u518d\u8f93\u5165\u4e00\u6b21\u8fdb\u884c\u786e\u8ba4\uFF0C\u53EA\u80FD\u7531\u82F1\u6587\u5B57\u6BCD\u3001\u6570\u5B57\u548C\u90E8\u5206\u82F1\u6587\u5B57\u7B26\u7EC4\u6210", None))
        self.label_9.setText(QCoreApplication.translate("register_2", u"\u8bf7\u8f93\u5165\u60a8\u7684\u804c\u4e1a :", None))
        self.usrType.setPlaceholderText(QCoreApplication.translate("register_2", u"\u6559\u5e08\u3001\u5b66\u751f\u3001\u533b\u751f\u3001\u62a4\u58eb\u3001\u653f\u6cbb\u5bb6\u3001\u4f5c\u5bb6\u3001\u79d1\u7814\u4eba\u5458\u7b49", None))
        self.doRegister.setText(QCoreApplication.translate("register_2", u"\u6ce8\u518c", None))
        self.cancel.setText(QCoreApplication.translate("register_2", u"\u53d6\u6d88", None))
        self.label_6.setText(QCoreApplication.translate("register_2", u"\u8bf7\u586b\u5199\u60a8\u7684\u8054\u7cfb\u65b9\u5f0f :", None))
        self.company_2.setPlaceholderText(QCoreApplication.translate("register_2", u"\u8bf7\u586b\u5199\u60a8\u7684\u7535\u8bdd\u53f7\u7801", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    win = Ui_register()
    win.show()
    sys.exit(app.exec())