# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regedit.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox,QApplication
import sys
import pymysql

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SignUp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.activities=[]

    def getUsername(self):
        self.Username_SignUp = self.Username_SignUp.text()

    def doRe(self):
        # print(type(self.ID),self.ID)
        # print(self.ID,self.usrName,self.usrGender,self.contact,self.compa,self.career,self.fstpwd,self.pwdsecond)
        try:
            a = False
            # b = self.usrGender
            c = False
            for i in self.Username_SignUp:
                if 33 <= ord(i) <= 126:
                    continue
                else:
                    a = True
            for i in self.Password_Forsure:
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
            elif self.Password_SignUp != self.Password_Forsure:
                pwdwrong = QMessageBox()
                pwdwrong.setWindowTitle("密码错误!")
                pwdwrong.setText("两次输入的密码不一致!")
                pwdwrong.exec()
            elif len(self.Password_SignUp) > 16 or len(self.Password_SignUp) < 6:
                pw = QMessageBox()
                pw.setWindowTitle("密码错误!")
                pw.setText("密码必须6~16位!")
                pw.exec()
            else:
                db = pymysql.connect(host="localhost", user="root", password="123456", charset="utf8")
                csor = db.cursor()
                csor.execute("use remaimai")
                csor.execute("select * from re1;")
                readers = csor.fetchall()
                # print(readers)
                for i in readers:
                    if self.Username_SignUp == i[0]:
                        IdrepeatError = QMessageBox()
                        IdrepeatError.setWindowTitle("用户ID错误!")
                        IdrepeatError.setText("已经存在该ID用户，请换一个ID!")
                        IdrepeatError.exec()
                    # print(readers)
                    else:
                        # sql = "insert into rpwd values (\"{}\",\"{}\")".format(self.ID,self.pwdsecond)
                        # print(sql)
                        csor.execute("insert into re1 values (\"{}\",\"{}\")".format(self.Username_SignUp, self.Password_Forsure))
                        csor.execute("select * from re1;")
                        readers = csor.fetchall()
                        for i in readers:
                            # print(i)
                            if self.Username_SignUp == i[0]:
                                suc = QMessageBox()
                                suc.setWindowTitle("成功!")
                                suc.setText("您已成功注册成为本图书馆用户!")
                                suc.exec()
                                break
                        # csor.execute(
                        #     "insert into rdinfo values (\"{}\",\"{}\",\"{}\")".format(self.Username_SignUp,
                        #                                                             self.usrName,
                        #                                                             self.usrGender,
                        #                                                                      ))
                        db.commit()
                        break
                    db.close()
                    csor.close()
        except AttributeError:
            owrong = QMessageBox()
            owrong.setWindowTitle("错误!")
            owrong.setText("请填写信息!")
            owrong.exec()

    def closeEvent(self, event):
        sys.exit(0)

    def getName(self):
        self.Username_SignUp = self.Username_SignUp.text()

    def getFstpwd(self):
        self.Password_SignUp = self.Password_SignUp.text()

    def getSecpwd(self):
        self.Password_Forsure = self.Password_Forsure.text()
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.resize(403, 320)
        self.layoutWidget = QWidget(SignUp)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 361, 221))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Username = QLabel(self.layoutWidget)
        self.Username.setObjectName(u"Username")
        self.Username.setAlignment(Qt.AlignCenter)
        self.Username.setWordWrap(False)
        self.Username.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.Username, 0, Qt.AlignHCenter)

        self.Username_SignUp = QLineEdit(self.layoutWidget)
        self.Username_SignUp.setObjectName(u"Username_SignUp")

        self.verticalLayout.addWidget(self.Username_SignUp)

        self.Password = QLabel(self.layoutWidget)
        self.Password.setObjectName(u"Password")
        self.Password.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Password)

        self.Password_SignUp = QLineEdit(self.layoutWidget)
        self.Password_SignUp.setObjectName(u"Password_SignUp")

        self.verticalLayout.addWidget(self.Password_SignUp)

        self.Password_Forsure = QLineEdit(self.layoutWidget)
        self.Password_Forsure.setObjectName(u"Password_Forsure")

        self.verticalLayout.addWidget(self.Password_Forsure)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.Username.setText(QCoreApplication.translate("SignUp", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u7528\u6237\u540d</span></p></body></html>", None))
        self.Username_SignUp.setText("")
        self.Username_SignUp.setPlaceholderText(QCoreApplication.translate("SignUp", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.Password.setText(QCoreApplication.translate("SignUp", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u5bc6\u7801</span></p></body></html>", None))
        self.Password_SignUp.setPlaceholderText(QCoreApplication.translate("SignUp", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.Password_Forsure.setPlaceholderText(QCoreApplication.translate("SignUp", u"\u8bf7\u786e\u8ba4\u5bc6\u7801", None))
    # retranslateUi



if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Ui_SignUp()
    win.show()
    sys.exit(app.exec_())