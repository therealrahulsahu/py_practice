import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):  # QWidget class is inherited to start activity

    def __init__(self):
        super().__init__()  # construct of activity creation is created
        self.initUI()


    def initUI(self):
        self.setGeometry(0, 0, 800, 450)    # (a,b,c,d) a*b-->position coordinates of activity c*d-->is length*height
        self.setWindowTitle('Rk\'s Icon')  # To set activity title
        self.setWindowIcon(QIcon('D:\Torrent\copy.ico'))  # To set activity Icon
        self.show()  # To display activity


if __name__ == '__main__':
    app = QApplication(sys.argv)  # TO start application
    ex = Example()  # To call activity
    sys.exit(app.exec_())  # To end application by closing
