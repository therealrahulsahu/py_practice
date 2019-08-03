# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setWindowIcon(QtGui.QIcon('images\\insert_table.ico'))
        MainWindow.setStyleSheet("background-color:rgb(255, 250, 220)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font-size:30px;\n""\n""")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.name_field.setObjectName("name_field")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_field)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.email_field = QtWidgets.QLineEdit(self.centralwidget)
        self.email_field.setObjectName("email_field")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.email_field)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.phone_field = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_field.setObjectName("phone_field")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phone_field)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.address_field = QtWidgets.QLineEdit(self.centralwidget)
        self.address_field.setObjectName("address_field")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.address_field)
        self.horizontalLayout_3.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 6)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.warning_lb = QtWidgets.QLabel(self.centralwidget)
        self.warning_lb.setStyleSheet("font-size:20px;")
        self.warning_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_lb.setObjectName("warning_lb")
        self.horizontalLayout.addWidget(self.warning_lb)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.reset_bt = QtWidgets.QPushButton(self.centralwidget)
        self.reset_bt.setStyleSheet("background-color:rgb(255, 25, 28);\n"
"/*  border: none;*/\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;")
        self.reset_bt.setObjectName("reset_bt")
        self.horizontalLayout_2.addWidget(self.reset_bt)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.okay_bt = QtWidgets.QPushButton(self.centralwidget)
        self.okay_bt.setStyleSheet("background-color: #4CAF50; /* Green */\n"
"/*  border: none;*/\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"\n"
"  font-size: 16px;")
        self.okay_bt.setObjectName("okay_bt")
        self.horizontalLayout_2.addWidget(self.okay_bt)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 10)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.UIaction(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Campus Entry Log"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label.setText(_translate("MainWindow", "E-Mail"))
        self.label_3.setText(_translate("MainWindow", "Phone No."))
        self.label_4.setText(_translate("MainWindow", "Address"))
        self.warning_lb.setText(_translate("MainWindow", "Enter Details"))
        self.reset_bt.setText(_translate("MainWindow", "Reset"))
        self.okay_bt.setText(_translate("MainWindow", "Okay"))

    def UIaction(self, MW):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

