"""
This example shows three labels on a window
using absolute positioning.
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Tu', self)   # To create label
        lbl1.move(15, 10)

        lbl2 = QLabel('Chutiya', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('Hai', self)
        lbl3.move(95, 70)

        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())