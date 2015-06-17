import sys
from PySide.QtGui import QWidget, QPushButton, QHBoxLayout, QApplication


class MainWindow(QWidget):
    """ Our Main Window class
    """
    def __init__(self):
        """ Constructor Function
        """
        QWidget.__init__(self)
        self.setWindowTitle("Horizontal Layout")
        self.setGeometry(300, 250, 400, 300)

    def SetLayout(self):
        """ Function to add buttons and set the layout
        """
        horizontalLayout = QHBoxLayout(self)
        hButton1 = QPushButton('Button 1', self)
        hButton2 = QPushButton('Button 2', self)
        hButton3 = QPushButton('Button 3', self)
        hButton4 = QPushButton('Button 4', self)
        horizontalLayout.addWidget(hButton1)
        horizontalLayout.addWidget(hButton2)
        horizontalLayout.addWidget(hButton3)
        horizontalLayout.addWidget(hButton4)
        self.setLayout(horizontalLayout)

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
