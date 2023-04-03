from PyQt5 import QtCore, QtGui, QtWidgets
'''This is the Login Page
the below class uses Qwidget to create this window

'''

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(609, 556)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("#label {\n"
"background-image:url(bg.jpg);\n"
"border-top-left-radius:50px;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.label_2.setStyleSheet("background-color:#fff;\n"
"border-bottom-right-radius:50px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(340, 60, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#000;\n"
"")
        self.label_3.setObjectName("label_3")
        
        self.invalid = QtWidgets.QLabel(self.widget)
        self.invalid.setGeometry(QtCore.QRect(295,100,190,40))
        font1 = QtGui.QFont()
        font1.setPointSize(11)
        self.invalid.setFont(font1)
        self.invalid.setText('Incorrect Mail or Password')
        self.invalid.setStyleSheet('color:red')
        
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(295, 150, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color:#fff;\n"
"color:rgba(103, 103, 103, 240);\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"padding-bottom:7px\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(295, 215, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"background-color:#fff;\n"
"color:rgba(103, 103, 103, 240);\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"padding-bottom:7px\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(295, 295, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("\n"
"QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0.568, x2:0, y2:0.994318, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(255, 97, 97, 255));\n"
"\n"
"color:#fff;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"#pushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0.568, x2:0, y2:0.994318, stop:0 rgba(0, 0, 2, 255), stop:1 rgba(255, 97, 97, 255));\n"
"}\n"
"\n"
"#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0.568, x2:0, y2:0.994318, stop:0 rgba(0, 0, 2, 255), stop:1 rgba(0, 97, 97, 255));\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(295, 330, 190, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_2.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Mail"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_4.setText(_translate("Form", "Not a User ? "))
        self.pushButton_2.setText(_translate("Form", "Sign Up for free"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
