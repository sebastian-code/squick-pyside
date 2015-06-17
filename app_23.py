import sys
from PySide.QtGui import QWidget, QFormLayout, QApplication, QLabel, QLineEdit


class MainWindow(QWidget):
    """ Our Main Window class
    """
    def __init__(self):
        """ Constructor Function
        """
        QWidget.__init__(self)
        self.setWindowTitle("Form Layout")
        self.setGeometry(300, 250, 400, 300)

    def SetLayout(self):
        formLayout = QFormLayout(self)
        labelUsername = QLabel("Username")
        txtUsername = QLineEdit()
        labelPassword = QLabel("Password")
        txtPassword = QLineEdit()
        formLayout.addRow(labelUsername, txtUsername)
        formLayout.addRow(labelPassword, txtPassword)
        self.setLayout(formLayout)

if __name__ == '__main__':
    # Exception Handling
    try:
        # QApplication.setStyle('plastique')
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])

    except SystemExit:
        print("Closing Window...")

    except Exception:
        print(sys.exc_info()[1])
