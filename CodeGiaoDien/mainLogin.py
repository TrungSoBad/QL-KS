import sys
from PyQt6.QtWidgets import QApplication, QDialog
from GDLogin import Ui_Dialog   # file py đã convert

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginDialog()
    window.show()
    sys.exit(app.exec())