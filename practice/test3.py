import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont


class mybt(QPushButton):    # class for button
    def __init__(self, name, inclass):   # passing name on button inside
        super().__init__(name, inclass)
        self.run()
    def run(self):
        self.setToolTip('This is a <b>QPushButton</b> widget')  # setting tooltip content for button
        # print(self.sizeHint())    # returns default size of button
        self.resize(self.sizeHint())    # to give dimension of button
        self.move(50, 50)  # position of button


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))    # Setting font for Tooltip(It is a place where mouse is pointing)

        self.setToolTip('This is a <b>QWidget</b> widget')  # here setting toolip content for activity

        btn = mybt('Press', self)
        """btn = QPushButton('Press', self)   # initializing a button with name-->'press'
        btn.setToolTip('This is a <b>QPushButton</b> widget')   # setting tooltip content for button
        btn.resize(btn.sizeHint())
        btn.move(50, 50)    # position of button"""

        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())