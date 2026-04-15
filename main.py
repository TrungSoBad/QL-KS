import sys
from PyQt6 import QtWidgets
from GDAdmin import Ui_MainWindow   # tên file + class

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.BtnDashBoard.clicked.connect(lambda: self.switch_page(0))
        self.ui.BtnRoom.clicked.connect(lambda: self.switch_page(1))
        self.ui.BtnCustomer.clicked.connect(lambda: self.switch_page(2))
        self.ui.BtnStaff.clicked.connect(lambda: self.switch_page(3))
        self.ui.BtnAddRoom.clicked.connect(lambda: self.switch_page(4))
        self.ui.BtnSerVice.clicked.connect(lambda: self.switch_page(5))
        self.ui.BtnReport.clicked.connect(lambda: self.switch_page(6))
    
    def switch_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
    

# ======================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())