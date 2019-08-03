from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QSizeGrip)
from PyQt5.QtCore import Qt
import sys


class myclass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sample 2")
        self.setGeometry(100, 100, 800, 450)
        self.UIaction()

    def UIaction(self):
        cetralwidget = QWidget()
        self.setCentralWidget(cetralwidget)
        cenlay = QVBoxLayout()
        cetralwidget.setLayout(cenlay)

        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        szgrip = QSizeGrip(self)
        cenlay.addWidget(szgrip)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myclass()
    ex.show()
    sys.exit(app.exec_())
