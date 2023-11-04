from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtUiTools import QUiLoader
from datetime import *
from register import Ui_SignUp


class Mywindow(QWidget, Ui_SignUp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()
