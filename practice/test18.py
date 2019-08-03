"""
In this example, we reimplement an
event handler.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):     # to create an event where 'e' is an key information
        if e.key() == Qt.Key_Escape:    # if key press is escape then
            self.close()    # closes if key found


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
