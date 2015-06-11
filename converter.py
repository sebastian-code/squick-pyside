import sys
from PySide.QtCore import *
from PySide.QtGui import *
import requests

"""
Noqomo Currency Converter

This is the main application script

author: Noqomo
website: http://www.noqomo.com
last edited: July 2013
"""


class Form(QDialog):
    # inialization of QDialog
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # grab latest rates and date
        date = self.getdata()
        rates = sorted(self.rates.keys())

        # data set
        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 1000000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")

        # theme layout
        grid = QGridLayout()
        # must specify position with grid layout
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

        self.setWindowTitle("Noqomo Currency Converter")

        # behvaiour signals
        self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)

    def updateUi(self):
        # update the GUI when new country is selected along with conversion
        to = self.toComboBox.currentText()
        from_ = self.fromComboBox.currentText()

        amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
        self.toLabel.setText("%0.2f" % amount)

    def getdata(self):
        self.rates = {}
        # grab the data set from the the Bank of Canada exchange
        try:
            date = "Unknown"

            fl = requests("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")
            fh = fl.read()

            # iterate through file
            for line in fh:
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing")):
                    continue

                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]

                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass

            return "Exchange rates date: " + date
        except Exception as e:
            return "Failed to download: \n%s" % e

# initialize application
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
