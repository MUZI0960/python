import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic, QtCore
from PyQt5.Qt import QPushButton


form_class = uic.loadUiType("./myomok.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        
        self.flagWB = True 
        
        self.setupUi(self)
        
        for j in range(10):
            for i in range(10):
                btn1 = QPushButton('',self)
                btn1.setIcon(QtGui.QIcon('0.png'))
                btn1.setIconSize(QtCore.QSize(40,40))
                btn1.setGeometry(QtCore.QRect(i*40,j*40,40,40))
                    
                btn1.clicked.connect(self.btnClick)
                # btn1.mouseDoubleClickEvent(self.btndbClick)
            
        
    def btnClick(self):
        
        if self.flagWB :
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else:
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flagWB = not self.flagWB        
            
    
    
    
    
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    