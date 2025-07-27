import sys

import requests

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QMessageBox, QVBoxLayout,
                             QLineEdit, QHBoxLayout, QSlider, QSpinBox, QComboBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

class Currency_App(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Enter your currency: ")
        self.error_label = QLabel(self)
        self.button = QPushButton("convert to", self)
        self.textbox = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox2.setReadOnly(True)
        self.combobox = QComboBox(self)
        self.combobox2 = QComboBox(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Currency App")
        self.setWindowIcon(QIcon("dollar.png"))
        self.textbox.setPlaceholderText("Amount")
        self.textbox2.setPlaceholderText("Amount")
        self.combobox.addItems(["USD", "EUR", "TRY", "AUD", "JPY", "GBP", "CAD"])
        self.combobox2.addItems(["TRY", "EUR", "USD", "AUD", "JPY", "GBP", "CAD"])

        hbox = QHBoxLayout()
        hbox.addWidget(self.textbox)
        hbox.addWidget(self.combobox)
        hbox.addWidget(self.button)
        hbox.addWidget(self.textbox2)
        hbox.addWidget(self.combobox2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.error_label)

        self.setLayout(vbox)

        self.button.clicked.connect(self.convert_currency)

    def convert_currency(self):
        try:
            amount = float(self.textbox.text())
            from_currency = self.combobox.currentText()
            to_currency = self.combobox2.currentText()

            API_key = "fca_live_Ny8r9cS1x5i74qZfXMfG2qPppVqVdneHpJvrd2wQ"
            url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_key}&base_currency={from_currency}&currencies={to_currency}"

            response = requests.get(url)
            data = response.json()

            rate = data["data"][to_currency]
            converted_amount = round(amount * rate, 2)

            self.textbox2.setText(str(converted_amount))
            self.error_label.setText("")

        except Exception as e:
            self.error_label.setText(f"Error: {e}")
            return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    currency_window = Currency_App()
    currency_window.show()
    sys.exit(app.exec_())