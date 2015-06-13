# Import required modules
import sys
import time

from PySide.QtGui import QApplication, QMainWindow, QStatusBar, QProgressBar,\
    QLabel, QTextEdit


class MainWindow(QMainWindow):
    """ Our Main Window """
    def __init__(self):
        """ Constructor Fucntion
        """
        QMainWindow.__init__(self)
        self.setWindowTitle("Main Window")
        self.setGeometry(300, 250, 400, 300)
        self.statusLabel = QLabel('Showing Progress')
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)

    def createStatusBar(self):
        """ Function to create the status bar
        """
        self.myStatusBar = QStatusBar()
        self.myStatusBar.showMessage('', 2000)
        self.setStatusBar(self.myStatusBar)
        """
        self.progressBar.setValue(10)
        self.myStatusBar.addWidget(self.statusLabel, 1)
        self.myStatusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.myStatusBar)
        """

    def showProgress(self):
        """ Function to show progress
        """
        while(self.progressBar.value() < self.progressBar.maximum()):
            self.progressBar.setValue(self.progressBar.value() + 10)
            time.sleep(1)

        self.statusLabel.setText('Ready')

    def setupComponents(self):
        """ Setting the central widget
        """
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.createStatusBar()
        mainWindow.setupComponents()
        mainWindow.show()
        # mainWindow.showProgress()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])

    except SystemExit:
        print("Closing Window...")

    except Exception:
        print(sys.exc_info()[1])
