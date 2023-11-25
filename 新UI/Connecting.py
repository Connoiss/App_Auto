# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '连接设备中.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Connecting(object):
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
        self.Connecting_2.setText(QCoreApplication.translate("Connecting", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">\u8fde\u63a5\u8bbe\u5907\u4e2d\u2026\u2026\u2026\u2026</span></p></body></html>", None))
    # retranslateUi

