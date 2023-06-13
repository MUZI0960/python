import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import win32api


form_class = uic.loadUiType("./Main07.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb_call.clicked.connect(self.mycall)
        
        self.pb1.clicked.connect(self.btnClick)
        self.pb2.clicked.connect(self.btnClick)
        self.pb3.clicked.connect(self.btnClick)
        self.pb4.clicked.connect(self.btnClick)
        self.pb5.clicked.connect(self.btnClick)
        self.pb6.clicked.connect(self.btnClick)
        self.pb7.clicked.connect(self.btnClick)
        self.pb8.clicked.connect(self.btnClick)
        self.pb9.clicked.connect(self.btnClick)
        self.pb0.clicked.connect(self.btnClick)
    
    def mycall(self):
         win32api.MessageBox(0, self.le.text(), "calling", 1)
        
        
    def btnClick(self):
        
        str_new = self.sender().text()
        str_old = self.le.text()
        
        self.le.setText(str_old+str_new)
        
        print(str_new, str_old)
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    