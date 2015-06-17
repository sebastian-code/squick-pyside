import sys
from PySide.QtGui import QWidget, QPushButton, QGridLayout, QApplication


class MainWindow(QWidget):
    """ Our Main Window class
    """
    def __init__(self):
        """ Constructor Function
        """
        QWidget.__init__(self)
        self.setWindowTitle("Grid Layout")
        self.setGeometry(300, 250, 400, 300)

    def SetLayout(self):
        gridLayout = QGridLayout(self)
        gButton1 = QPushButton('Button 1', self)
        gButton2 = QPushButton('Button 2', self)
        gButton3 = QPushButton('Button 3', self)
        gButton4 = QPushButton('Button 4', self)
        gButton5 = QPushButton('Button 5', self)
        gridLayout.addWidget(gButton1, 0, 0)
        gridLayout.addWidget(gButton2, 0, 1)
        gridLayout.addWidget(gButton3, 1, 0, 1, 2)
        gridLayout.addWidget(gButton4, 2, 0)
        gridLayout.addWidget(gButton5, 2, 1)
        self.setLayout(gridLayout)

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
