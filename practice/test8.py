"""
ZetCode PyQt5 tutorial

This program creates a submenu.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()    # adding menubar
        fileMenu = menubar.addMenu('File')  # adding menu 'File'

        impMenu = QMenu('Import', self)     # To create menu named 'Import'
        impAct = QAction('Import mail', self)   # To create action named 'Import mail'
        impMenu.addAction(impAct)   # adding action to sub menu 'Import'

        newAct = QAction('New', self)   # To create action named 'New'

        fileMenu.addAction(newAct)  # adding action to menu
        fileMenu.addMenu(impMenu)   # adding menu to activity

        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle('Submenu')
        self.show()


def main():
    app = QApplication(sys.argv)
    Ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
