
"""

This program centers a window
on the screen.

"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
# QDesktopWidget   provides information about the user desktop including screen size


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(800, 450)
        self.center()   # this place activity in center of screen

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()   # It provides the geometry of (self)Activity/else
        # print(qr)
        cp = QDesktopWidget().availableGeometry().center()
        # It gives geometry of desktop and then center gives center point of screen
        # print(cp)
        qr.moveCenter(cp)
        # print(qr)
        self.move(qr.topLeft())
        # print(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())