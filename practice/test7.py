"""

This program creates a menubar. The
menubar has one menu with an exit action.

"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready to Go...")
        #   Creating Action
        exitAct = QAction(QIcon('d:\\torrent\\p.ico'), '&Exit', self)   # To create a option in menubar
        exitAct.setShortcut('Ctrl+Q')   # To set a shortcut key
        exitAct.setStatusTip('Exit application')    # TO set message in status bar
        exitAct.triggered.connect(qApp.quit)    # To quit application

        exitAct2 = QAction(QIcon('d:\\torrent\\p.ico'), '&Exit_2', self)  # To create a option in menubar
        exitAct2.setShortcut('Ctrl+Q')  # To set a shortcut key
        exitAct2.setStatusTip('Exit application')  # TO set message in status bar
        exitAct2.triggered.connect(qApp.quit)  # To quit application

        self.statusBar()

        mbar = self.menuBar()   # adding menubar to working activity

        fileMenu = mbar.addMenu('&File')    # adding menu named 'File'
        fileMenu.addAction(exitAct)     # adding action to menu

        fileMenu2 = mbar.addMenu('&Edit')
        fileMenu2.addAction(exitAct)
        fileMenu2.addAction(exitAct2)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
