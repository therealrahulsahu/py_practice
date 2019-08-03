"""
In this example, we position two push
buttons in the bottom-right corner
of the window.
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()    # Creating a horozontal box
        hbox.addStretch(1)
        hbox.addWidget(okButton)    # adding a button
        hbox.addWidget(cancelButton)    # adding button

        vbox = QVBoxLayout()    # creating verticle layout
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
