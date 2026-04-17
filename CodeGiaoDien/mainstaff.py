import sys
from PyQt6 import QtWidgets
from Staff import Ui_StaffWindow 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_StaffWindow()
        self.ui.setupUi(self)
        
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.BtnCheckIn.clicked.connect(lambda: self.switch_page(0))
        self.ui.btnCheckOut.clicked.connect(lambda: self.switch_page(1))
        self.ui.BtnList.clicked.connect(lambda: self.switch_page(2))
        self.ui.BtnInvoice.clicked.connect(lambda: self.switch_page(4))
        self.ui.BtnService.clicked.connect(lambda: self.switch_page(3))
        self.ui.BtnAcccount.clicked.connect(lambda: self.switch_page(5))
    
    def switch_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
    

# ======================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())