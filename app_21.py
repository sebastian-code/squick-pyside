import sys
from PySide.QtGui import QWidget, QPushButton, QVBoxLayout, QApplication


class MainWindow(QWidget):
    """ Our Main Window class
    """
    def __init__(self):
        """ Constructor Function
        """
        QWidget.__init__(self)
        self.setWindowTitle("Vertical Layout")
        self.setGeometry(300, 250, 400, 300)

    def SetLayout(self):
        """ Function to add buttons and set the layout
        """
        verticalLayout = QVBoxLayout(self)
        vButton1 = QPushButton('Button 1', self)
        vButton2 = QPushButton('Button 2', self)
        vButton3 = QPushButton('Button 3', self)
        vButton4 = QPushButton('Button 4', self)
        verticalLayout.addWidget(vButton1)
        verticalLayout.addWidget(vButton2)
        verticalLayout.addStretch()
        verticalLayout.addWidget(vButton3)
        verticalLayout.addWidget(vButton4)
        self.setLayout(verticalLayout)

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
