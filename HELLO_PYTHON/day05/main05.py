from random import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("./Main06.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        rnd = random()
        
        mine = self.le_mine.text()
        
        print(mine)
        
        if rnd > 0.5 :
            com = "홀"
        else :
            com = "짝"
        if com == mine :
            result = "승리"
        else : 
            result = "패배"
        
        print("나 : ", com)
        print("컴 : ", mine)
        print("결과 : ", result)
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    