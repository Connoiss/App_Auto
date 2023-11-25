from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide6.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn = QPushButton('Show Message', self)
        btn.clicked.connect(self.showCustomMessageBox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QMessageBox Example')
        self.show()

    def showCustomMessageBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Custom Message Box')
        msgBox.setText('Do you want to proceed?')

        # 添加自定义按钮，并将其点击事件连接到自定义槽函数
        yes_button = msgBox.addButton(QMessageBox.Yes)
        yes_button.clicked.connect(self.yesButtonClicked)

        msgBox.addButton(QMessageBox.No)
        # no_button.clicked.connect(self.noButtonClicked)

        # 设置默认按钮
        msgBox.setDefaultButton(QMessageBox.Yes)

        msgBox.exec_()

    def yesButtonClicked(self):
        print('Yes button clicked.')

    def noButtonClicked(self):
        print('No button clicked.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
