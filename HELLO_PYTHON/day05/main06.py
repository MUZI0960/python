import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./Main05.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        
        num = self.le.text()
        
        dan = int(num)
        
        result = ""
        
        # result += "{}*{}={}\n".format(dan,i,dan*i)
        
        for i in range(1,10):
            # print("{}*{}={}".format(dan,i,dan*i))
            result += "{}*{}={}\n".format(dan,i,dan*i)
            # result += str(dan * i)+"\n"
        
        
        print(result)
        
        self.pt.setPlainText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    