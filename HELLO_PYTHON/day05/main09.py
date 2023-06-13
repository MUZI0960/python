from random import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("./Main09.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
    
    
    def drawStar(self, cnt):
    
        ret = ""
        for i in range(cnt):
            ret += "*"
        
        ret += "\n"
        
        return ret
    
    def btnClick(self):
        
        first = self.leFirst.text()
        last = self.leLast.text()
        
        firstNum = int(first)
        lastNum = int(last)
        
        txt = ""
        
        for i in range(firstNum, lastNum+1):
            txt += self.drawStar(i)
        
        
        self.te.setText(txt)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    