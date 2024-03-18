import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStyleFactory,
    QVBoxLayout,
    QWidget,
)

STYLE = """
    QLineEdit {
        background-color: #000;
        color: #fff;
        border-radius: 10px;
        border: 2px solid #fff;
        margin: 10px;
    }

    QPushButton {
        background-color: #000;
        color: #fff;
        border-radius: 50px;
        border: 2px solid #fff;
    }
    QPushButton:hover {
        background-color: #fff;
        color: #000;
    }
    #error_label {
        color: red;
        font-size: 20px;
        font-family: "Monospace";
    }

"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the dark theme
        self.setDarkTheme()
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("Celsius to Farenheit Converter")

        # creating widgets
        self.celsius_input = QLineEdit()
        self.celsius_input.setPlaceholderText("Enter Celsius temperature")
        self.celsius_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        converter_button = QPushButton("Convert")
        converter_button.setFixedSize(100, 100)
        converter_button.clicked.connect(self.convert)

        self.farenheit_input = QLineEdit()
        self.farenheit_input.setPlaceholderText("Enter Farenheit temperature")
        self.farenheit_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.error_label = QLabel()
        self.error_label.setObjectName("error_label")
        self.error_label.setText("Please enter a temperature")
        self.error_label.hide()

        # setting layout
        layout = QVBoxLayout()
        # this layout is for centering the button inside the vertical layout
        button_layout = QHBoxLayout()

        layout.addWidget(self.celsius_input)

        button_layout.addStretch()
        button_layout.addWidget(converter_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        layout.addWidget(self.farenheit_input)
        layout.addWidget(self.error_label)

        # setting the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def convert(self):
        """slot for the convert button. It converts the temperature from celsius to farenheit and vice versa"""

        if celsius := self.celsius_input.text():
            farenheit = (float(celsius) * 9 / 5) + 32
            self.farenheit_input.setText(str(farenheit))
            self.error_label.hide()
        elif farenheit := self.farenheit_input.text():
            celsius = (float(farenheit) - 32) * 5 / 9
            self.celsius_input.setText(str(celsius))
            self.error_label.hide()
        else:
            self.error_label.show()

    def setDarkTheme(self):
        # Set the application style to Fusion
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        self.setStyleSheet(STYLE)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
