
from PyQt5 import QtCore, QtGui





try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1096, 399)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_5.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_5.addWidget(self.textEdit)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setMaximumSize(QtCore.QSize(550, 200))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_8.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.verticalLayout_8, 2, 2, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_7.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(Form)
        self.textEdit_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_7.addWidget(self.textEdit_2)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 2, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout.addLayout(self.verticalLayout_6, 2, 1, 1, 1)

        self.retranslateUi(Form)
        #QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), drops)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Monster Hunter 4 Ultimate Pro", None))
        self.label.setText(_translate("Form", "Weapon Damage", None))
        self.textEdit.setHtml(_translate("Form", "Not Important HTML Code", None))