import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QDialog, QVBoxLayout, QLabel, QStackedWidget
from PyQt5.QtGui import QIcon


class SW(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rahul sahu")
        self.setGeometry(200, 200, 800, 450)
        self.stackedwidget()

    def stackedwidget(self):
        vbox = QVBoxLayout()
        self.stackedWidget = QStackedWidget()
        vbox.addWidget(self.stackedWidget)

        for x in range(8):
            label = QLabel("Stacked Child : " + str(x+1))
            label.setStyleSheet('color:red;')

            self.stackedWidget.addWidget(label)

            self.button = QPushButton('Stack '+str(x))
            self.button.setStyleSheet('background-color:green')

            self.button.page = x
            self.button.clicked.connect(self.btn_clicked)
            vbox.addWidget(self.button)
        self.setLayout(vbox)

    def btn_clicked(self):
        self.button = self.sender()
        self.stackedWidget.setCurrentIndex(self.button.page - 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SW()
    win.show()
    sys.exit(app.exec_())
