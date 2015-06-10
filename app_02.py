# Import the necessary modules required
import sys
from PySide.QtCore import *
from PySide.QtGui import *

# Main Function
if __name__ == '__main__':
    # Create the main application
    myApp = QApplication(sys.argv)
    # Create a Label and set its properties
    try:
        appLabel = QLabel()
        appLabel.setText("Hello, World!!!\n Look at my first app using PySide")
        appLabel.setAlignment(Qt.AlignCenter)
        appLabel.setWindowTitle("My First Application")
        appLabel.setGeometry(300, 300, 250, 175)
        # Show the Label
        appLabel.show()
        # Execute the Application and Exit
        myApp.exec_()
        sys.exit()

    except NameError:
        print("Name Error:", sys.exc_info()[1])
        pass
