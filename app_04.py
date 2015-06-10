# Import required modules
import sys
from PySide.QtGui import QApplication, QWidget, QIcon


class SampleWindow(QWidget):
    """ Our main window class
    """
    def __init__(self):
        """ Constructor Function
        """
        QWidget.__init__(self)
        self.setWindowTitle("Icon Sample")
        self.setGeometry(300, 300, 200, 150)

    def setIcon(self):
        """ Function to set Icon
        """
        appIcon = QIcon('favicon.jpg')
        self.setWindowIcon(appIcon)

if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        myWindow.setIcon()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])

    except SystemExit:
        print("Closing Window...")

    except Exception:
        print(sys.exc_info()[1])
