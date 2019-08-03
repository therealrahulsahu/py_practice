import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)  # To start application
    w = QWidget()  # To start a activity
    w.resize(800, 450)  # To set activity size()
    w.move(0, 0)  # To set activity position
    w.setWindowTitle('Rahul Sahu')  # To set activity title
    w.show()  # To display  activity which is stored in a variable
    sys.exit(app.exec_())  # To set end of application by close button
