from PyQt5 import QtCore, QtGui, QtWidgets

'''This is the Loading SCreen Page
the below class uses Qwidget to create this window
'''

class Ui_splashScreen(object):
    def setupUi(self, splashScreen):
        splashScreen.setObjectName("splashScreen")
        splashScreen.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(splashScreen)
        self.centralwidget.setStyleSheet("background-color:#000;")
        self.centralwidget.setObjectName("centralwidget")
        self.dropshadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropshadowFrame.setGeometry(QtCore.QRect(0, 0, 680, 400))
        self.dropshadowFrame.setStyleSheet("QFrame{\n"
"color: #c92a2a;\n"
"border-radius:10px;\n"
"}")
        self.dropshadowFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.dropshadowFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dropshadowFrame.setObjectName("dropshadowFrame")
        self.label_title = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_title.setGeometry(QtCore.QRect(0, 50, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: #c92a2a;")
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_Description = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_Description.setGeometry(QtCore.QRect(10, 120, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Description.setFont(font)
        self.label_Description.setStyleSheet("color: rgb(241, 241, 241);")
        self.label_Description.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Description.setObjectName("label_Description")
        self.progressBar = QtWidgets.QProgressBar(self.dropshadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"Background-color:#000;\n"
"color: rgb(200, 200, 200);\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 2, 255), stop:1 rgba(255, 97, 97, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_loading.setGeometry(QtCore.QRect(0, 310, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: #fff;")
        self.label_loading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_credits.setGeometry(QtCore.QRect(0, 350, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(241, 241, 241);")
        self.label_credits.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        splashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splashScreen)
        QtCore.QMetaObject.connectSlotsByName(splashScreen)

    def retranslateUi(self, splashScreen):
        _translate = QtCore.QCoreApplication.translate
        splashScreen.setWindowTitle(_translate("splashScreen", "MainWindow"))
        self.label_title.setText(_translate("splashScreen", "<strong>OUR</strong> APP NAME"))
        self.label_Description.setText(_translate("splashScreen", "<strong>APP</strong> Description"))
        self.label_loading.setText(_translate("splashScreen", "Loading..."))
        self.label_credits.setText(_translate("splashScreen", "<strong>Created</strong> Harish Narayana.G   "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splashScreen = QtWidgets.QMainWindow()
    ui = Ui_splashScreen()
    ui.setupUi(splashScreen)
    splashScreen.show()
    sys.exit(app.exec())
