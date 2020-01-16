import sys
from PyQt5.QtWidgets import *

class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,400)


if __name__ =="__main__":
    app = QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    app.exec_()

