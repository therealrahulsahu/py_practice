from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
import sys


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Bon Apetite')
        self.move(100, 50)
        #vbox = QVBoxLayout()
        #self.setLayout(vbox)
        lb = QLabel(self)
        # vbox.addWidget(lb)

        im = open('dsa.jpg', 'rb')
        im_data = im.read()
        im.close()

        from os import system
        system('dsa.jpg')


AW = QApplication(sys.argv)
dia = MyDialog()
dia.show()
sys.exit(AW.exec_())
