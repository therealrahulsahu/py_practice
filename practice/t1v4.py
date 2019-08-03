import sys

from PyQt5.QtWidgets import (QApplication, QMenu, QMainWindow, QWidget, QVBoxLayout)


class myclass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sample 2")
        self.setGeometry(100, 100, 800, 450)


    def contextMenuEvent(self, event):
        cetralwidget = QWidget()
        self.setCentralWidget(cetralwidget)
        cenlay = QVBoxLayout()
        cetralwidget.setLayout(cenlay)

        contmenu = QMenu(self)

        newaction = contmenu.addAction("New")
        openaction = contmenu.addAction("Open")
        quitaction = contmenu.addAction("Quit")

        action = contmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitaction:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myclass()
    ex.show()
    sys.exit(app.exec_())
