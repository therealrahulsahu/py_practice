from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton,
                             QVBoxLayout, QHBoxLayout, QWidget, QLabel, QRadioButton,
                             QCheckBox, QLineEdit)
import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect, QSize


class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inwin()
        self.ui_buttons()
        self.lab()
        self.checkbx()
        self.lnedit()
        self.ui_layout()


    def lnedit(self):
        self.btnfo1 = QPushButton("Submit")
        self.lned1 = QLineEdit()
        self.lbfo1 = QLabel("Result")
        self.lned1.returnPressed.connect(self.inlineedit)


    def lab(self):
        self.lbrb1 = QLabel()
        self.lbrb2 = QLabel()

    def inwin(self):
        self.setWindowTitle('PyQt5 window')     # setting window title
        self.setGeometry(100, 100, 800+400, 450+225)    # setting geometry of window
        self.setWindowIcon(QIcon('d:\\torrent\\p.ico'))     # adding icon to window

    def ui_buttons(self):
        self.bt1 = QPushButton('Click here', self)   # creating button
        # self.bt1.move(100, 100)    # setting its location
        # self.bt1.setGeometry(QRect(100, 100, 110, 50))   # setting location and dimension
        self.bt1.resize(140, 50)
        self.bt1.setIcon(QIcon('d:\\torrent\\p.ico'))    # setting icon image
        self.bt1.setIconSize(QSize(40, 40))   # setting icon size
        self.bt1.setToolTip('<h3>Your button</h3>')  # adding tooltip on button with html code
        self.bt1.setToolTipDuration(2e3)     # setting tooltip duration
        self.bt1.clicked.connect(self.resp1)    # setting response
        self.bt1.setWhatsThis(": This btn : ")  # press shift+F1 on widget

        self.bt2 = QPushButton('another', self)
        self.bt2.clicked.connect(self.resp2)

        self.rb1 = QRadioButton("Physics")
        # self.rb1.setChecked(True)
        self.rb1.toggled.connect(self.OnRadioBtn)
        # self.rb1.setIcon(QIcon("d:\\torrent\\p.ico"))
        self.rb2 = QRadioButton("Maths")
        self.rb2.toggled.connect(self.OnRadioBtn)
        self.rb3 = QRadioButton("Chemistry")
        self.rb3.toggled.connect(self.OnRadioBtn)

    def checkbx(self):
        self.qc1 = QCheckBox("Python")
        self.qc2 = QCheckBox("C/C++")
        self.qc3 = QCheckBox("Java")
        self.qc4 = QCheckBox("JavaScript")
        self.qc5 = QCheckBox("php")



    def ui_layout(self):
        ctwidgets = QWidget(self)
        self.setCentralWidget(ctwidgets)
        centlay = QHBoxLayout()
        ctwidgets.setLayout(centlay)
        ly1 = QVBoxLayout()
        ly2 = QVBoxLayout()
        centlay.addLayout(ly1)
        centlay.addLayout(ly2)
        ly1.addWidget(self.bt1)
        ly1.addWidget(self.bt2)

        lhin1 = QHBoxLayout()
        ly1.addLayout(lhin1)

        lhin1.addWidget(self.rb1)
        lhin1.addWidget(self.rb2)
        lhin1.addWidget(self.rb3)
        lhin1.addWidget(self.lbrb1)

        lhin2 = QHBoxLayout()
        ly1.addLayout(lhin2)

        lhin3 = QHBoxLayout()
        ly1.addLayout(lhin3)
        lhin3.addWidget(self.qc1)
        self.qc1.toggled.connect(self.chtogg)
        lhin3.addWidget(self.qc2)
        self.qc2.toggled.connect(self.chtogg)
        lhin3.addWidget(self.qc3)
        self.qc3.toggled.connect(self.chtogg)
        lhin3.addWidget(self.qc4)
        self.qc4.toggled.connect(self.chtogg)
        lhin3.addWidget(self.qc5)
        self.qc5.toggled.connect(self.chtogg)
        lhin3.addWidget(self.lbrb2)

        # im1 = QPixmap('d:\\torrent\\p.ico')     # creating image object
        # lb1 = QLabel(self)
        # lb1.setPixmap(im1)
        # ly1.addWidget(lb1)

        h2ly2 = QHBoxLayout()
        ly2.addLayout(h2ly2)

        h2ly2.addWidget(self.lned1)
        h2ly2.addWidget(self.btnfo1)
        h2ly2.addWidget(self.lbfo1)

    def inlineedit(self):
        self.lbfo1.setText(self.lned1.text())

    def chtogg(self):
        if self.qc1.isChecked():
            self.lbrb2.setText("selected : "+self.qc1.text())
        if self.qc2.isChecked():
            self.lbrb2.setText("selected : "+self.qc2.text())
        if self.qc3.isChecked():
            self.lbrb2.setText("selected : "+self.qc3.text())
        if self.qc4.isChecked():
            self.lbrb2.setText("selected : "+self.qc4.text())
        if self.qc5.isChecked():
            self.lbrb2.setText("selected : "+self.qc5.text())

    count = 0

    def resp1(self):
        if self.count % 2:
            self.count += 1
            self.bt1.setText('Welcome')
        else:
            self.count += 1
            self.bt1.setText('Get Lost')

    def resp2(self):
        if self.count % 2:
            self.count += 1
            self.bt2.setText('Welcome')
        else:
            self.count += 1
            self.bt2.setText('Get Lost')

    def OnRadioBtn(self):
        rdbtn = self.sender()
        if rdbtn.isChecked():
            self.lbrb1.setText('Selected '+rdbtn.text())
if __name__ == '__main__':
    app = QApplication(sys.argv)    # creating application window
    A = Win()   # creating a window object
    A.show()    # giving command to display it
    sys.exit(app.exec_())   # creating close button or alt+F4 as response
