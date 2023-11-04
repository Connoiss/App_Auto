import sys
from PySide6.QtWidgets import QApplication
from AAAAA import Ui_login


if __name__ == "__main__":
    app = QApplication([])
    win = Ui_login()
    win.show()
    sys.exit(app.exec())
