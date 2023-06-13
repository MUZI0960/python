import sys

from PyQt5 import uic, QtGui, QtCore
from PyQt5.Qt import QPushButton, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("./myomok.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],

            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
            
        ]
        
        self.pb2D=[]
        self.flagWB = True 
        self.flagOVER = False
        
        print(self.arr2D[1][1])
        
        super().__init__()
        
        
        self.setupUi(self)
        
        for i in range(19):
            line = []
            for j in range(19):
                temp = QPushButton('', self)
                temp.setIcon(QtGui.QIcon('0.png'))
                temp.setIconSize(QtCore.QSize(40,40))
                temp.setGeometry(QtCore.QRect(j*40,i*40,40,40))
                temp.clicked.connect(self.btnClick)
                temp.setToolTip("{},{}".format(i,j))
                line.append(temp)
            self.pb2D.append(line)
        
        self.pb.clicked.connect(self.btnReset)
        self.myrander()    
    
    def btnReset(self):
        for i in range(19):
            for j in range(19):  
                self.arr2D[i][j] = 0
        self.myrander()
        self.flagOVER = False
        self.flagWB = True
    
            
    def myrander(self):
        for i in range(19):
            for j in range(19):  
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
    
                          
        
    def btnClick(self):
        if self.flagOVER == True:
            return
            
        
        str_ij = self.sender().toolTip()
        
        str_i = str_ij.split(',')[0]
        str_j = str_ij.split(',')[1]
        
        i = int(str_i)
        j = int(str_j)
        
        if self.arr2D[i][j]>0:
            return
        
        stone = -1
        if self.flagWB : 
            stone = 1
            self.arr2D[i][j] = 1
        else:
            stone = 2
            self.arr2D[i][j] = 2
        
        up = self.getUP(i, j, stone)
        dw = self.getDW(i, j, stone)
        ri = self.getRI(i, j, stone)
        le = self.getLE(i, j, stone)
        
        ul = self.getUL(i, j, stone)
        ur = self.getUR(i, j, stone)
        dl = self.getDL(i, j, stone)
        dr = self.getDR(i, j, stone)
        
        
        print("up", up, "dw", dw, "ri", ri, "le", le, "ul", ul,"ur", ur, "dl", dl, "dr", dr )
        
        d1 = up + dw + 1
        d2 = ul + dr + 1
        d3 = le + ri + 1
        d4 = dl + ur + 1
        
        self.myrander()
        
        
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            self.flagOVER = True
            if self.flagWB :
                QMessageBox.about(self, 'GAME OVER', "백돌 승리")
            else :
                QMessageBox.about(self, 'GAME OVER', "흑돌 승리")
        
            
        self.flagWB = not self.flagWB  
    
    def getUP(self, i, j, stone):
        ret = 0
        try:
            while True:
                i += -1
                if i < 0 :
                    return ret
                if self.arr2D[i][j]==stone :
                    ret += 1
                else:
                    return ret 
        except:
            return ret
    
    def getDW(self, i, j, stone):
        ret = 0
        try:
            while True:
                i += 1
                if i < 0 :
                    return ret
                if self.arr2D[i][j]==stone :
                    ret += 1
                else:
                    return ret 
        except:
            return ret
    
    def getRI(self, i, j, stone):
        ret = 0
        try:
            while True:
                j += 1
                if j < 0 :
                    return ret
                if self.arr2D[i][j]==stone :
                    ret += 1
                else:
                    return ret 
        except:
            return ret
    
    def getLE(self, i, j, stone):
        ret = 0
        try:
            while True:
                j += -1
                if j < 0 :
                    return ret
                if self.arr2D[i][j]==stone :
                    ret += 1
                else:
                    return ret 
        except:
            return ret

    def getUL(self, i, j, stone):
        ret = 0
        try:
            while True:
                j += 1
                i += 1
                if j < 0 or i < 0 :
                    return ret
                if self.arr2D[i][j]==stone :
                    ret += 1
                else:
                    return ret 
        except:
            return ret
    
    def getUR(self, i, j, stone):
        ret = 0
        try:
            while True:
                j += -1
                i += 1
                if j < 0 or i < 0 :
                    return ret
                if self.arr2D[i][j]==stone :
                    ret += 1
                else:
                    return ret 
        except:
            return ret
        
    def getDL(self, i, j, stone):
        ret = 0
        try:
            while True:
                j += 1
                i += -1
                if j < 0 or i < 0 :
                    return ret
                if self.arr2D[i][j]==stone :
                    ret += 1
                else:
                    return ret 
        except:
            return ret
        
    def getDR(self, i, j, stone):
        ret = 0
        try:
            while True:
                j += -1
                i += -1
                if j < 0 or i < 0 :
                    return ret
                if self.arr2D[i][j]==stone :
                    ret += 1
                else:
                    return ret 
        except:
            return ret
                   
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    