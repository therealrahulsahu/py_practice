"""
In this example, we display the x and y
coordinates of a mouse pointer in a label widget."""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)  # creating a string variable

        self.label = QLabel(self.text, self)    # creating a label
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)   # adding a label at coordinates (0,0)

        self.setMouseTracking(True)     # turning mouse tracking on

        self.setLayout(grid)

        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):    # reimplementing mouse event
        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)    # setting text into variable label


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
