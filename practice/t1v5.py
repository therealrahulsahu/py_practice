from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel,QGroupBox,QCheckBox, QLineEdit, QWidget,QVBoxLayout,QDialogButtonBox, QTabWidget, QMainWindow, QApplication, QDialog, QTabWidget,QComboBox
import sys


class Tab(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyqt 5")
        self.setWindowIcon(QIcon("d\\rahul code\\icons\\exit.ico"))
        self.setGeometry(200, 200, 800, 450)

        vbox = QVBoxLayout()
        tabWidget = QTabWidget()

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.accepted.connect(self.reject)

        tabWidget.addTab(Tabcontact(), "Contact Details")
        tabWidget.addTab(TabPersonDetails(), "Person Details")


        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

class Tabcontact(QWidget):
    def __init__(self):
        super().__init__()

        namelabel = QLabel("Name :")
        nameedit = QLineEdit()

        phonelabel = QLabel("Phone :")
        phoneedit = QLineEdit()

        emaillabel = QLabel("Email :")
        emailedit = QLineEdit()

        addrlabel = QLabel("Adderess :")
        addredit = QLineEdit()

        vbox = QVBoxLayout()

        vbox.addWidget(namelabel)
        vbox.addWidget(nameedit)

        vbox.addWidget(phonelabel)
        vbox.addWidget(phoneedit)

        vbox.addWidget(emaillabel)
        vbox.addWidget(emailedit)

        vbox.addWidget(addrlabel)
        vbox.addWidget(addredit)

        self.setLayout(vbox)



class TabPersonDetails(QWidget):
    def __init__(self):
        super().__init__()

        groupBox = QGroupBox("Select Your Gender")

        list = ['Male', 'Female']

        combo = QComboBox()
        combo.addItems(list)

        vbox = QVBoxLayout()
        vbox.addWidget(combo)

        groupBox.setLayout(vbox)
        groupBox2 = QGroupBox("Select favorite Programming lang ")
        pytohn = QCheckBox("Python")
        cpp = QCheckBox("C++")
        java = QCheckBox("Java")
        csharp = QCheckBox("C#")

        vboxp = QVBoxLayout()
        vboxp.addWidget(pytohn)
        vboxp.addWidget(cpp)
        vboxp.addWidget(java)
        vboxp.addWidget(csharp)


        mainlayout = QVBoxLayout()
        mainlayout.addWidget(groupBox)
        mainlayout.addLayout(vboxp)

        self.setLayout(mainlayout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tab()
    ex.show()
    sys.exit(app.exec_())
