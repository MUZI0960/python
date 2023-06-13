from random import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox
from holoviews.examples.reference.apps.bokeh.selection_stream import sel


form_class = uic.loadUiType("./Main10.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.com = "123"
        self.pb.clicked.connect(self.btnClick)
        self.randomCom()
    
    
    def getStrike(self, com, mine):
        
        ret = 0
        
        c1 = str(com)[0:1]
        c2 = str(com)[1:2]
        c3 = str(com)[2:3]
        
        m1 = str(mine)[0:1]
        m2 = str(mine)[1:2]
        m3 = str(mine)[2:3]
    
        if(c1 == m1):
            ret += 1
        if(c2 == m2):
            ret += 1
        if(c3 == m3):
            ret += 1
        
        return ret
    
    def getBall(self, com, mine):
        
        ret = 0
        
        c1 = str(com)[0:1]
        c2 = str(com)[1:2]
        c3 = str(com)[2:3]
        
        m1 = str(mine)[0:1]
        m2 = str(mine)[1:2]
        m3 = str(mine)[2:3]
    
        if(c1 == m2 or c1 == m3):
            ret += 1
        if(c2 == m1 or c2 == m3):
            ret += 1
        if(c3 == m1 or c3 == m2):
            ret += 1
        
        
        return ret
    
    
    def randomCom(self):
        
        arr = [
            1,2,3,4,5,   6,7,8,9
            ]

        for i in range(1000):
            rnd = int(random()*9)
            a = arr[rnd]
            b = arr[0]
            arr[0] = a
            arr[rnd] = b
        
        n1 = arr[0]
        n2 = arr[1]
        n3 = arr[2]
        
        num1 = str(n1)
        num2 = str(n2)
        num3 = str(n3)
        
        self.com = num1 + num2 + num3
        
        return self.com
    
    def btnClick(self):
        
        n = self.le.text()
        num = int(n)
        
        
        resultS = self.getStrike(123, num)
        resultB = self.getBall(123, num)
        
        str_old = self.pte.toPlainText()
        str_new = n + "s:" + str(resultS) + "b:" + str(resultS) + "\n"
        
        self.pte.setPlainText(str_old+str_new)
        self.le.setText("")
        
        if(resultS == 3) :
            QMessageBox.about(self, 'you win', n)
               
        print(str_old)
        print(resultS)
        print(resultB)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    