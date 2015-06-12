# Import required modules
import sys, time
from PySide.QtGui import QApplication, QMainWindow, QStatusBar


class MainWindow(QMainWindow):
    """ Our Main Window """
    def __init__(self):
        """ Constructor Fucntion
        """
        QMainWindow.__init__(self)
        self.setWindowTitle("Main Window")
        self.setGeometry(300, 250, 400, 300)

    def createStatusBar(self):
        """ Function to create Status Bar
        """
        self.myStatusBar = QStatusBar()
        self.myStatusBar.showMessage('Ready', 2000)
        self.setStatusBar(self.myStatusBar)

if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.createStatusBar()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])

    except SystemExit:
        print("Closing Window...")

    except Exception:
        print(sys.exc_info()[1])
