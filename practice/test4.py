"""
This program creates a quit
button. When we press the button,
the application terminates.

"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class Button(QPushButton):
    def __init__(self,name,inclass):
        super().__init__(name,inclass)
        self.run()
    def run(self):
        self.clicked.connect(QApplication.instance().quit)
        # It call function which is in argument when button is clicked
        self.resize(self.sizeHint())
        self.move(50, 50)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = Button('Quit', self)

        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # print(*sys.argv,sep='\n')
    ex = Example()
    sys.exit(app.exec_())
