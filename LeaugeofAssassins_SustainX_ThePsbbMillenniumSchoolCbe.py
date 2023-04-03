'''
Welcome to Project Sustain-X app

Requirement To Excute the following Files:

Modules:
_________

->PyQt5
->pyrebase
->sys
->vlc
->time

'''


import pyrebase
from PyQt5 import QtCore,QtGui,QtWidgets,QtSql
from register import Ui_Form as register_form
from new import video
from PyQt5.QtWidgets import QApplication,QMainWindow,QGraphicsDropShadowEffect
from splash import Ui_splashScreen
from index_2 import Ui_MainWindow

from page_1 import Ui_MainWindow as Page1
from page_2_ import Ui_MainWindow as Page2
from page_3_ import Ui_MainWindow as Page4
from page_4_ import Ui_MainWindow as Page3
from Thank_You import Ui_Form as thanks
from login_page import Ui_Form
import sys

'''
We have connect our login authentication to Firebase throygh the python module called pyrebase.
This helps us atheniticate the login email and password provided and lets the user log in

Note: Existing Id and Password:
        admin@mail.com , admin123

'''

counter = 0
firebaseConfig = {
  "apiKey": "AIzaSyCm1UlekrTl3CU4gdFj5nWAcNEaSFGfQHQ",
  "authDomain": "authbase-75795.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "projectId": "authbase-75795",
  "storageBucket": "authbase-75795.appspot.com",
  "messagingSenderId": "123904079790",
  "appId": "1:123904079790:web:65fa1b4dba75890779ba3f",
  "measurementId": "G-W5QZY5R53R"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth  =firebase.auth()


class Thank(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = thanks()
        self.ui.setupUi(self)
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        





'''
This is the About -Us Page that inherits from PyQt5.QtWidgets.QMainWindow to display the window.
we also make an instance of page_3_ modules to edit some stuff 
'''
#About-Us

class AboutUs(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = Page4()
        self.ui.setupUi(self)
        self.ui.label_2.setText("Sustain X")
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        '''We set the title and we make the window as a frameless window .'''
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0,92,157,550))
        
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        
        self.setWindowIcon(QtGui.QIcon('LoGo.jpeg'))
        self.setWindowTitle("LEARN")
        
        QtWidgets.QSizeGrip(self.ui.siz_grip)
        
        '''
        Buttons function asigning
        
        We asign functions to buttons by creating signals and slots through the clicked meathod available in the buttons.
        
        '''
        self.ui.pushButton.clicked.connect(lambda:self.showMinimized())
        
        self.ui.pushButton_10.setText('LEARN')
        self.ui.pushButton_11.setText("Video")
        self.ui.pushButton_12.setText('About-Us')
        self.ui.pushButton_13.setText('Play-Quiz')
        self.ui.pushButton_14.setText("Thank-You")
        
        self.ui.pushButton_10.clicked.connect(lambda:self.learn())
        self.ui.pushButton_11.clicked.connect(lambda:self.video())
        self.ui.pushButton_12.clicked.connect(lambda:self.about_us())
        self.ui.pushButton_13.clicked.connect(lambda:self.more())
        #self.ui.pushButton_14.clicked.connect(lambda:self.th())
        
        self.ui.pushButton_3.clicked.connect(lambda:self.close())
        self.ui.pushButton_9.clicked.connect(lambda:self.close())
        self.ui.pushButton_2.clicked.connect(lambda:self.restore_or_maximize())
        
        '''This moveWindow FUnction is added so that we can move the window'''
        
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                    self.move(self.pos() + e.globalPos()- self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
                
        self.ui.header_frame.mouseMoveEvent = moveWindow
        
        '''This is the side tool box where the menu content is displayed'''
        
        self.ui.toolBox.setItemText(0,'Sustain-Menu')
        self.ui.toolBox.setItemText(1,'Explore-Menu')
        
        self.ui.pushButton_8.clicked.connect(self.slideLeftMenu)
        
        
    def learn(self):
        l =Learn()
        l.show()
        self.close()
        
    def video(self):
        v = Video()
        v.show()
        self.close()
        
    def more(self):
        m = More()
        m.show()
        self.close()
        
    def about_us(self):
        a = AboutUs()
        a.show()
        self.close()
        
        
    def slideLeftMenu(self,maxWidth=250,enable=True):
        if enable:
            width = self.ui.side_menu_frame.width()
            maxExtend = maxWidth
            standard = 0
            
            if width == 0:
                widthExtend = maxExtend
            else:
                widthExtend = standard
                    
            self.animation = QtCore.QPropertyAnimation(self.ui.side_menu_frame,b"minimumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.start()

    
    
    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
    
    """These Meathod is used for minimizing and maximizing the window"""
        
    def restore_or_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_2.setIcon(QtGui.QIcon("icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.pushButton_2.setIcon(QtGui.QIcon('icons/minimize-2.svg'))



'''
This is the More Page that inherits from PyQt5.QtWidgets.QMainWindow to display the window.
we also make an instance of page_4_ modules to edit some stuff 
'''
#More

class More(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = Page3()
        self.ui.setupUi(self)
        self.ui.label_2.setText("Sustain X")
        
        '''We set the title and we make the window as a frameless window .'''
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0,92,157,550))
        
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        
        
        QtWidgets.QSizeGrip(self.ui.siz_grip)
        
        '''
        Buttons function asigning
        
        We asign functions to buttons by creating signals and slots through the clicked meathod available in the buttons.
        
        '''
        
        
        self.ui.pushButton_10.setText('LEARN')
        self.ui.pushButton_11.setText("Video")
        self.ui.pushButton_12.setText('About-Us')
        self.ui.pushButton_13.setText('Play-Quiz')
        self.ui.pushButton_14.setText("Thank-You")
        
        self.ui.pushButton_10.clicked.connect(lambda:self.learn())
        self.ui.pushButton_11.clicked.connect(lambda:self.video())
        self.ui.pushButton_12.clicked.connect(lambda:self.about_us())
        self.ui.pushButton_13.clicked.connect(lambda:self.more())
        #self.ui.pushButton_14.clicked.connect()
        
        self.ui.pushButton.clicked.connect(lambda:self.showMinimized())
        self.ui.pushButton_9.clicked.connect(lambda:self.close())
        self.ui.pushButton_3.clicked.connect(lambda:self.close())
        self.ui.pushButton_2.clicked.connect(lambda:self.restore_or_maximize())
        
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
                
        self.ui.header_frame.mouseMoveEvent = moveWindow
        
        '''side Menu is displayed '''
        self.ui.toolBox.setItemText(0,'Sustain-Menu')
        self.ui.toolBox.setItemText(1,'Explore-Menu')
        
        '''These are Buttons or options for the Quiz which has been assigned to a function that shows correct or wrong depeding on the answwer the user chooses.'''
        
        #1
        self.ui.pushButton_15.clicked.connect(lambda:self.wrong_1())
        self.ui.pushButton_16.clicked.connect(lambda:self.corret_1())
        self.ui.pushButton_17.clicked.connect(lambda:self.wrong_1())
        self.ui.pushButton_18.clicked.connect(lambda:self.wrong_1())
        self.ui.label_15.setVisible(False)
        
        #2
        self.ui.pushButton_23.clicked.connect(lambda:self.wrong_2())
        self.ui.pushButton_24.clicked.connect(lambda:self.wrong_2())
        self.ui.pushButton_25.clicked.connect(lambda:self.corret_2())
        self.ui.pushButton_26.clicked.connect(lambda:self.wrong_2())
        self.ui.label_14.setVisible(False)
        
        ##3
        self.ui.pushButton_27.clicked.connect(lambda:self.corret_3())
        self.ui.pushButton_28.clicked.connect(lambda:self.wrong_3())
        self.ui.pushButton_29.clicked.connect(lambda:self.wrong_3())
        self.ui.pushButton_30.clicked.connect(lambda:self.wrong_3())
        self.ui.label_13.setVisible(False)
        
        
        ##4
        self.ui.pushButton_31.clicked.connect(lambda:self.wrong_4())
        self.ui.pushButton_32.clicked.connect(lambda:self.wrong_4())
        self.ui.pushButton_33.clicked.connect(lambda:self.corret_4())
        self.ui.pushButton_34.clicked.connect(lambda:self.wrong_4())
        self.ui.label_12.setVisible(False)
        
         ##5
        self.ui.pushButton_35.clicked.connect(lambda:self.wrong_5())
        self.ui.pushButton_36.clicked.connect(lambda:self.corret_5())
        self.ui.pushButton_37.clicked.connect(lambda:self.wrong_5())
        self.ui.pushButton_38.clicked.connect(lambda:self.wrong_5())
        self.ui.label_11.setVisible(False)
        
         ##6
        self.ui.pushButton_39.clicked.connect(lambda:self.wrong_6())
        self.ui.pushButton_40.clicked.connect(lambda:self.corret_6())
        self.ui.pushButton_41.clicked.connect(lambda:self.wrong_6())
        self.ui.pushButton_42.clicked.connect(lambda:self.wrong_6())
        self.ui.label_10.setVisible(False)
        
        ##7
        self.ui.pushButton_43.clicked.connect(lambda:self.wrong_7())
        self.ui.pushButton_44.clicked.connect(lambda:self.wrong_7())
        self.ui.pushButton_45.clicked.connect(lambda:self.corret_7())
        self.ui.pushButton_46.clicked.connect(lambda:self.wrong_7())
        self.ui.label_9.setVisible(False)
        
        ##8
        self.ui.pushButton_47.clicked.connect(lambda:self.wrong_8())
        self.ui.pushButton_48.clicked.connect(lambda:self.wrong_8())
        self.ui.pushButton_49.clicked.connect(lambda:self.corret_8())
        self.ui.pushButton_50.clicked.connect(lambda:self.wrong_8())
        self.ui.label_8.setVisible(False)
        
        ##9
        self.ui.pushButton_51.clicked.connect(lambda:self.corret_9())
        self.ui.pushButton_52.clicked.connect(lambda:self.wrong_9())
        self.ui.pushButton_53.clicked.connect(lambda:self.wrong_9())
        self.ui.pushButton_54.clicked.connect(lambda:self.wrong_9())
        self.ui.label_7.setVisible(False)
        
        
        ##10
        self.ui.pushButton_55.clicked.connect(lambda:self.corret_10())
        self.ui.pushButton_56.clicked.connect(lambda:self.wrong_10())
        self.ui.pushButton_57.clicked.connect(lambda:self.wrong_10())
        self.ui.pushButton_58.clicked.connect(lambda:self.wrong_10())
        self.ui.label_6.setVisible(False)
        
        
    
    '''The Functionality for the Quiz buttons or options that displays correct or wrong'''
            
    def corret_1(self):
        self.ui.label_15.setText("Correct !")
        self.ui.label_15.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_15.setVisible(True)
        
    def wrong_1(self):
        self.ui.label_15.setText("Wrong !")
        self.ui.label_15.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_15.setVisible(True)
        
    def corret_2(self):
        self.ui.label_14.setText("Correct !")
        self.ui.label_14.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_14.setVisible(True)
        
    def wrong_2(self):
        self.ui.label_14.setText("Wrong !")
        self.ui.label_14.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_14.setVisible(True)
        
    def corret_3(self):
        self.ui.label_13.setText("Correct !")
        self.ui.label_13.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_13.setVisible(True)
        
    def wrong_3(self):
        self.ui.label_13.setText("Wrong !")
        self.ui.label_13.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_13.setVisible(True)
    def corret_4(self):
        self.ui.label_12.setText("Correct !")
        self.ui.label_12.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_12.setVisible(True)
    def wrong_4(self):
        self.ui.label_12.setText("Wrong !")
        self.ui.label_12.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_12.setVisible(True)
    def corret_5(self):
        self.ui.label_11.setText("Correct !")
        self.ui.label_11.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_11.setVisible(True)
    def wrong_5(self):
        self.ui.label_11.setText("Wrong !")
        self.ui.label_11.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_11.setVisible(True)
    def corret_6(self):
        self.ui.label_10.setText("Correct !")
        self.ui.label_10.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_10.setVisible(True)
    def wrong_6(self):
        self.ui.label_10.setText("Wrong !")
        self.ui.label_10.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_10.setVisible(True)
    def corret_7(self):
        self.ui.label_9.setText("Correct !")
        self.ui.label_9.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_9.setVisible(True)
    def wrong_7(self):
        self.ui.label_9.setText("Wrong !")
        self.ui.label_9.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_9.setVisible(True)
    def corret_8(self):
        self.ui.label_8.setText("Correct !")
        self.ui.label_8.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_8.setVisible(True)
    def wrong_8(self):
        self.ui.label_8.setText("Wrong !")
        self.ui.label_8.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_8.setVisible(True)
    def corret_9(self):
        self.ui.label_7.setText("Correct !")
        self.ui.label_7.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_7.setVisible(True)
    def wrong_9(self):
        self.ui.label_7.setText("Wrong !")
        self.ui.label_7.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_7.setVisible(True)
    
    def corret_10(self):
        self.ui.label_6.setText("Correct !")
        self.ui.label_6.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_6.setVisible(True)
    def wrong_10(self):
        self.ui.label_6.setText("Wrong !")
        self.ui.label_6.setFont(QtGui.QFont('Segoe UI',15))
        self.ui.label_6.setVisible(True)
        
        
    def learn(self):
        l =Learn()
        l.show()
        self.close()
        
    def video(self):
        v = Video()
        v.show()
        self.close()
        
    def more(self):
        m = More()
        m.show()
        self.close()
        
    def about_us(self):
        a = AboutUs()
        a.show()
        self.close()
        
    def slideLeftMenu(self):
        width = self.ui.side_menu_frame.width()
        
             
        if width == 0:
            newWidth = 250
            self.ui.pushButton_8.setIcon(QtGui.QIcon('icons/chevron-left.svg'))
            
        else:
            newWidth = 250
            self.ui.pushButton_8.setIcon(QtGui.QIcon('icons/align-left.svg'))
            
        self.animation = QtCore.QPropertyAnimation(self.ui.side_menu_frame,b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    
    
    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
    
    
    '''This function is used to minimize or maximize the window'''
        
    def restore_or_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_2.setIcon(QtGui.QIcon("icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.pushButton_2.setIcon(QtGui.QIcon('icons/minimize-2.svg'))




'''
This is the Video Page that inherits from PyQt5.QtWidgets.QMainWindow to display the window.
we also make an instance of page_2_ modules to edit some stuff 
'''
#Video

class Video(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = Page2()
        self.ui.setupUi(self)
        self.ui.label_2.setText("Sustain X")
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        """removes the frame of window"""
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0,92,157,550))
        
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        
        self.setWindowIcon(QtGui.QIcon('LoGo.jpeg'))
        self.setWindowTitle("LEARN")
        
        QtWidgets.QSizeGrip(self.ui.siz_grip)
        
        '''side Menu Buttons Text and functionality for the buttons'''
        
        self.ui.pushButton_10.setText('LEARN')
        self.ui.pushButton_11.setText("Video")
        self.ui.pushButton_12.setText('About-Us')
        self.ui.pushButton_13.setText('Play-Quiz')
        self.ui.pushButton_14.setText("Thank-You")
        
        self.ui.pushButton_10.clicked.connect(lambda:self.learn())
        self.ui.pushButton_11.clicked.connect(lambda:self.video())
        self.ui.pushButton_12.clicked.connect(lambda:self.about_us())
        self.ui.pushButton_13.clicked.connect(lambda:self.more())
        #self.ui.pushButton_14.clicked.connect()
        
        self.ui.pushButton.clicked.connect(lambda:self.showMinimized())
        self.ui.pushButton_9.clicked.connect(lambda:self.close())
        self.ui.pushButton_3.clicked.connect(lambda:self.close())
        self.ui.pushButton_2.clicked.connect(lambda:self.restore_or_maximize())
        self.ui.pushButton_15.clicked.connect(lambda:self.vid())
        self.ui.pushButton_16.clicked.connect(lambda:self.Grap())
        
        
        
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
                
        self.ui.header_frame.mouseMoveEvent = moveWindow
        
        '''The Side Tool-Box'''
        
        self.ui.toolBox.setItemText(0,'Sustain-Menu')
        self.ui.toolBox.setItemText(1,'Explore-Menu')
        self.ui.pushButton_8.clicked.connect(self.slideLeftMenu)
        
    def learn(self):
        l =Learn()
        l.show()
        self.close()
        
    def video(self):
        v = Video()
        v.show()
        self.close()
        
    def more(self):
        m = More()
        m.show()
        self.close()
        
    def about_us(self):
        a = AboutUs()
        a.show()
        self.close()
    
    '''This is the meathod that when pressed allows you to play the graphics and video'''
        
    def Grap(self):
        video('v.mp4')
        
    def vid(self):
        video('Goal11.mp4')
        
    def slideLeftMenu(self):
        width = self.ui.side_menu_frame.width()
        
             
        if width == 0:
            newWidth = 250
            self.ui.pushButton_8.setIcon(QtGui.QIcon('icons/chevron-left.svg'))
            
        else:
            newWidth = 250
            self.ui.pushButton_8.setIcon(QtGui.QIcon('icons/align-left.svg'))
            
        self.animation = QtCore.QPropertyAnimation(self.ui.side_menu_frame,b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    
    
    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
    
    '''This Meathod is used to minimize and maximize the window'''    
    def restore_or_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_2.setIcon(QtGui.QIcon("icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.pushButton_2.setIcon(QtGui.QIcon('icons/minimize-2.svg'))





#-----------------------------------------------------------------------------------------


'''
This is the Learn Page that inherits from PyQt5.QtWidgets.QMainWindow to display the window.
we also make an instance of page_1_ modules to edit some stuff 
'''

#Learn Class
class Learn(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = Page1()
        self.ui.setupUi(self)
        
        self.ui.label_2.setText("Sustain X")
        
        '''We make the window as frame less window'''
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0,92,157,550))
        self.ui.toolBox.setItemText(0,'Sustain-Menu')
        self.ui.toolBox.setItemText(1,'Explore-Menu')
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        
        self.setWindowIcon(QtGui.QIcon('LoGo.jpeg'))
        self.setWindowTitle("LEARN")
        
        QtWidgets.QSizeGrip(self.ui.siz_grip)
        
        '''Side-menu Buttons names and functions'''
        
        self.ui.pushButton_10.setText('LEARN')
        self.ui.pushButton_11.setText("Video")
        self.ui.pushButton_12.setText('About-Us')
        self.ui.pushButton_13.setText('Play-Quiz')
        self.ui.pushButton_14.setText("Thank-You")
        
        self.ui.pushButton_10.clicked.connect(lambda:self.learn())
        self.ui.pushButton_11.clicked.connect(lambda:self.video())
        self.ui.pushButton_12.clicked.connect(lambda:self.about_us())
        self.ui.pushButton_13.clicked.connect(lambda:self.more())
        #self.ui.pushButton_14.clicked.connect()
        
        self.ui.pushButton.clicked.connect(lambda:self.showMinimized())
        self.ui.pushButton_9.clicked.connect(lambda:self.close())
        self.ui.pushButton_3.clicked.connect(lambda:self.close())
        self.ui.pushButton_2.clicked.connect(lambda:self.restore_or_maximize())
        
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
                
        self.ui.header_frame.mouseMoveEvent = moveWindow
        
        self.ui.pushButton_8.clicked.connect(self.slideLeftMenu)
        
    def learn(self):
        l =Learn()
        l.show()
        self.close()
        
    def video(self):
        v = Video()
        v.show()
        self.close()
        
    def more(self):
        m = More()
        m.show()
        self.close()
        
    def about_us(self):
        a = AboutUs()
        a.show()
        self.close()
        
    def slideLeftMenu(self):
        width = self.ui.side_menu_frame.width()
        
             
        if width == 0:
            newWidth = 250
            self.ui.pushButton_8.setIcon(QtGui.QIcon('icons/chevron-left.svg'))
            
        else:
            newWidth = 250
            self.ui.pushButton_8.setIcon(QtGui.QIcon('icons/align-left.svg'))
            
        self.animation = QtCore.QPropertyAnimation(self.ui.side_menu_frame,b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    
    
    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
        
    def restore_or_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_2.setIcon(QtGui.QIcon("icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.pushButton_2.setIcon(QtGui.QIcon('icons/minimize-2.svg'))


#--------------------------------------------------------------------------------------------

'''This  the Index page that comes after log and sign up that is from modules index_2.py '''

#MainWindow
class MainWindow(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.setText("")
        self.ui.pushButton_2.setText("")
        self.ui.pushButton_3.setText("")
        self.ui.pushButton_4.setText("")
        self.ui.pushButton.clicked.connect(self.learn)
        self.ui.pushButton_2.clicked.connect(self.video)
        self.ui.pushButton_3.clicked.connect(self.more)
        self.ui.pushButton_4.clicked.connect(self.about_us)
        self.ui.pushButton_7.clicked.connect(self.close)
        
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
    
    
        
    def learn(self):
        l =Learn()
        l.show()
        self.close()
        
    def video(self):
        v = Video()
        v.show()
        self.close()
        
    def more(self):
        m = More()
        m.show()
        self.close()
        
    def about_us(self):
        a = AboutUs()
        a.show()
        self.close()

#--------------------------------------------------------------------------------------------------------

'''The register Window where we can register our info to login , this is from register.py'''

class register(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = register_form()
        self.ui.setupUi(self)
        self.Main = QtWidgets.QMainWindow
        self.Main.setWindowFlag(self,QtCore.Qt.WindowType.FramelessWindowHint)
        self.Main.setAttribute(self,QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(self.save)
        self.ui.invalid.setVisible(False)
    
    
    '''This is used to check and verify wheather the password and confirmed password are correct'''   
    def save(self):
        mail = self.ui.lineEdit_4.text()
        pas = self.ui.lineEdit_5.text()
        confirm = self.ui.lineEdit_6.text()
        try:
            if pas == confirm:
                auth.create_user_with_email_and_password(mail,pas)
                self.l = login()
                self.l.show()
                self.close()
            else:
                self.ui.invalid.setText("Password Does not match")
                self.ui.invalid.setVisible(True)
        except:
            self.ui.invalid.setVisible(True)
            



'''The login Window where we can register our info to login , this is from login_page.py'''
class login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.Main = QtWidgets.QMainWindow
        self.Main.setWindowFlag(self,QtCore.Qt.WindowType.FramelessWindowHint)
        self.Main.setAttribute(self,QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(self.NextPage)
        self.ui.pushButton_2.clicked.connect(self.register)
        self.ui.invalid.setVisible(False)
        
        
    """This redirects to the registered page"""    
    def register(self):
        self.r = register()
        self.r.show()
        self.close()
    '''This is used to check and verift the login details with the databse and allows the users in if it is correct'''     
    def NextPage(self):
        user = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        try:
            auth.sign_in_with_email_and_password(user,password)
            self.main = MainWindow()
            self.main.show()
            self.close()
        except:
            self.ui.invalid.setVisible(True)
        
        


#--------------------------------------------------------------------------------------------------------

'''This is the Front Loading Screen  '''

#splash Screen
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_splashScreen()
        self.ui.setupUi(self)
        
        self.ui.label_credits.setText("<strong>Created By</strong> Leauge Of Assassins   ")
        
         ######################
        #REMOVE TITLE BAR
        self.Main = QtWidgets.QMainWindow
        self.Main.setWindowFlag(self,QtCore.Qt.WindowType.FramelessWindowHint)
        self.Main.setAttribute(self,QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        ######################
        
        ############
        #DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0,0,60))
        self.ui.dropshadowFrame.setGraphicsEffect(self.shadow)
        ###########
        
        #QTimer => START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress) 
        #TIMER IN MILLI
        self.timer.start(35)
        self.ui.label_Description.setText("<strong>Welcome</strong>To Application")
        
        
        QtCore.QTimer.singleShot(1500, lambda:self.ui.label_Description.setText("<strong>Loading</strong> DataBase"))
        QtCore.QTimer.singleShot(3000, lambda:self.ui.label_Description.setText("<strong>Loading</strong> User Interface"))
        
        
        
        self.show()
        
    def progress(self):
            
        global counter
            
        self.ui.progressBar.setValue(counter)
            
        if counter > 100:
            self.timer.stop()
                
            self.main = login()
            self.main.show()
                
            self.close()
                
        counter +=1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())