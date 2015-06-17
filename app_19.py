# Import required modules
import sys
from PySide.QtGui import QApplication, QMainWindow, QStatusBar, QTextEdit,\
    QAction, QIcon, QKeySequence, QMessageBox


class MainWindow(QMainWindow):
    """ Our Main Window class
    """
    def __init__(self):
        """ Constructor Function
        """
        QMainWindow.__init__(self)
        self.setWindowTitle("A Simple Text Editor")
        self.setWindowIcon(QIcon('iconos/prueba.png'))
        self.setGeometry(300, 250, 400, 300)

    def SetupComponents(self):
        """ Function to setup status bar, central widget, menu bar
        """
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()

        # Invoques toolbar creation and after that, reuses menu actions from
        # createActions() to create toolbar bottons.
        self.CreateToolBar()
        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.copyAction)
        self.mainToolBar.addAction(self.pasteAction)

        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.copyAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.pasteAction)
        self.helpMenu.addAction(self.aboutAction)

    # Slots called when the menu actions are triggered
    def newFile(self):
        self.textEdit.setText('')

    def exitFile(self):
        self.close()

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor",
                          "This example demonstrates the use " "of Menu Bar")

    def createActions(self):
        """ Function to create actions for menus
        """

        self.newAction = QAction(QIcon('iconos/new.png'), '&New', self,
                                 shortcut=QKeySequence.New,
                                 statusTip="Create a New File",
                                 triggered=self.newFile)
        self.exitAction = QAction(QIcon('iconos/exit.png'), 'E&xit', self,
                                  shortcut="Ctrl+Q",
                                  statusTip="Exit the Application",
                                  triggered=self.exitFile)
        self.copyAction = QAction(QIcon('iconos/copy.png'), 'C&opy', self,
                                  shortcut="Ctrl+C", statusTip="Copy",
                                  triggered=self.textEdit.copy)
        self.pasteAction = QAction(QIcon('iconos/paste.png'), '&Paste', self,
                                   shortcut="Ctrl+V", statusTip="Paste",
                                   triggered=self.textEdit.paste)
        self.aboutAction = QAction(QIcon('iconos/about.png'), 'A&bout', self,
                                   statusTip="Displays info about text editor",
                                   triggered=self.aboutHelp)

    # Actual menu bar item creation
    def createMenus(self):
        """ Function to create actual menu bar
        """
        # self.menubar() invoca una funcion nativa de la clase padre
        # QMainWindow la cual crea una barra de menu nativa al sistema de
        # ventanas en el que se ejecuta el programa, recordar el problema de
        # no buscar los menus en la barra de menus de Unity, donde estaban
        # "escondidos". El primer llamado a la funcion crea la barra y las
        # multiples invocaciones subsiguientes añaden los nuevos menus

        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def CreateToolBar(self):
        """ Function to create tool bar
        """
        self.mainToolBar = self.addToolBar('Main')

if __name__ == '__main__':
    # Exception Handling
    try:
        # QApplication.setStyle('plastique')
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetupComponents()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])

    except SystemExit:
        print("Closing Window...")

    except Exception:
        print(sys.exc_info()[1])
