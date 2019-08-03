"""
This program creates a toolbar.
The toolbar has one action, which
terminates the application, if triggered.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('d:\\torrent\\p.ico'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)  # to execute passes function

        exitAct2 = QAction(QIcon('d:\\torrent\\p.ico'), 'Exit2', self)
        exitAct2.setShortcut('Ctrl+Q')
        exitAct2.triggered.connect(qApp.quit)  # to execute passes function

        # toolbar is inherited variable
        self.toolbar = self.addToolBar('Exit')  # adding toolbar with a button named 'exit'
        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(exitAct2)

        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
