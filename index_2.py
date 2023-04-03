from PyQt5 import QtCore, QtGui, QtWidgets
'''This is the Index or the Selection Page 
the below class uses Qwidget to create this window
'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1279, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1279, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1279, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("WhatsApp Image 2022-01-28 at 5.53.43 PM.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.Form = QtWidgets.QWidget(MainWindow)
        self.Form.setAutoFillBackground(False)
        self.Form.setStyleSheet("")
        self.Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bg = QtWidgets.QLabel(self.Form)
        self.bg.setGeometry(0,0,1280,720)
        self.bg.setMinimumSize(1280,720)
        self.bg.setMaximumSize(1280,720)
        self.bg.setPixmap(QtGui.QPixmap("back.JPG"))
        self.bg.setObjectName("bg")
        self.frame_2 = QtWidgets.QFrame(self.bg)
        self.frame_2.setGeometry(QtCore.QRect(400, 40, 451, 101))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 10, 281, 80))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Logo = QtWidgets.QPushButton(self.layoutWidget)
        self.Logo.setStyleSheet("#Logo{\n"
"background:transparent;\n"
"}")
        self.Logo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("logored.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Logo.setIcon(icon1)
        self.Logo.setIconSize(QtCore.QSize(100, 70))
        self.Logo.setObjectName("Logo")
        self.horizontalLayout.addWidget(self.Logo)
        self.APP_Name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.APP_Name.setFont(font)
        self.APP_Name.setStyleSheet("#APP_Name{\n"
"font-family: Montserrat;\n"
"color:#fff\n"
"\n"
"}")
        self.APP_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.APP_Name.setObjectName("APP_Name")
        self.horizontalLayout.addWidget(self.APP_Name)
        self.label_4 = QtWidgets.QLabel(self.bg)
        self.label_4.setPixmap(QtGui.QPixmap("back.jpg"))
        self.label_4.setGeometry(QtCore.QRect(40, 130, 1201, 551))
        self.frame_3 = QtWidgets.QFrame(self.label_4)
        self.frame_3.setGeometry(QtCore.QRect(40, 130, 1201, 450))
        self.frame_3.setStyleSheet("QFrame{\n"
"border-radius:30px;\n"
"}\n"
"/*qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(42, 166, 65, 131), stop:1 rgba(0, 0, 0, 255)*/")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap("video-removebg-preview.png")))
        self.pushButton_2.setIconSize(QtCore.QSize(100,50))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: #000;\n"
"color:#fff;\n"
"border-radius:50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#c92a2a\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setIcon(QtGui.QIcon(QtGui.QPixmap("bg-po.png")))
        self.pushButton_4.setIconSize(QtCore.QSize(100,50))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: #000;\n"
"color:#fff;\n"
"border-radius:50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#c92a2a\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:#000 ;\n"
"color:#fff;\n"
"border-radius:50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#c92a2a\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap("sus-logo.png")))
        self.pushButton.setIconSize(QtCore.QSize(100,50))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap("more5.png")))
        self.pushButton_3.setIconSize(QtCore.QSize(100,100))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: #000;\n"
"color:#fff;\n"
"border-radius:50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#c92a2a\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.bg)
        self.frame.setGeometry(QtCore.QRect(1230, 0, 50, 46))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setStyleSheet("background:transparent;")
        self.pushButton_7.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.bg)
        MainWindow.setCentralWidget(self.Form)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCpoy = QtWidgets.QAction(MainWindow)
        self.actionCpoy.setObjectName("actionCpoy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APP"))
        self.APP_Name.setText(_translate("MainWindow", "Sustain X"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.actionCpoy.setText(_translate("MainWindow", "Cpoy"))
        self.actionCpoy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.actionAbout_Us.setShortcut(_translate("MainWindow", "Ctrl+B"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
