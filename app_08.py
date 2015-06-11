# Import required modules
import sys
from PySide.QtGui import QApplication, QWidget, QIcon, QLabel, QToolTip, QFont
from PySide.QtGui import QPushButton, QMessageBox


class SampleWindow(QWidget):
    """ Our main window class
    """
    def __init__(self):
        """ Constructor Function
        """
        QWidget.__init__(self)
        self.setWindowTitle("Icon Sample")
        self.setGeometry(300, 300, 200, 150)
        QToolTip.setFont(QFont("Decorative", 8, QFont.Bold))
        self.setToolTip('Our Main Window')

    def setIcon(self):
        """ Function to set Icon
        """
        appIcon = QIcon('favicon.jpg')
        self.setWindowIcon(appIcon)

    def setIconModes(self):
        myIcon1 = QIcon('favicon.jpg')
        myLabel1 = QLabel('sample', self)
        pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
        myLabel1.setPixmap(pixmap1)
        myLabel1.setToolTip('Active Icon')

        myIcon2 = QIcon('favicon.jpg')
        myLabel2 = QLabel('sample', self)
        pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
        myLabel2.setPixmap(pixmap2)
        myLabel2.move(50, 0)
        myLabel2.setToolTip('Disabled Icon')

        myIcon3 = QIcon('favicon.jpg')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(100, 0)
        myLabel3.setToolTip('Selected Icon')

    def quitApp(self):
        """ Function to confirm a message from the user
        """
        userInfo = QMessageBox.question(self,
            'Confirmation',
            "This will quit the application. Do you want to Continue?",
            QMessageBox.Yes | QMessageBox.No)

        if userInfo == QMessageBox.Yes:
            myApp.quit()

        if userInfo == QMessageBox.No:
            pass

    def setButton(self):
        """ Function to add a quit button
        """
        myButton = QPushButton('Quit', self)
        myButton.move(50, 100)
        myButton.clicked.connect(self.quitApp)

if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        myWindow.setIcon()
        myWindow.setIconModes()
        myWindow.setButton()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])

    except SystemExit:
        print("Closing Window...")

    except Exception:
        print(sys.exc_info()[1])
