import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton,
QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QWidget)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        bt1 = QPushButton('Press')
        inp = QLineEdit()
        lb_in = QLabel('Name')
        self.lb_out = QLabel('Empty')
        h1 = QHBoxLayout()
        h2 = QHBoxLayout()

        v1 = QVBoxLayout()

        h1.addStretch(1)
        h2.addStretch(1)

        h1.addWidget(lb_in)
        h1.addWidget(inp)
        h1.addWidget(bt1)

        h2.addWidget(self.lb_out)

        v1.addLayout(h1)
        v1.addLayout(h2)
        self.setLayout(v1)
        bt1.clicked.connect(self.myaction)

        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle('First win')
        self.show()
    def myaction(self):

        self.lb_out.setText('Data')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    s1 = Example()
    sys.exit(app.exec_())
