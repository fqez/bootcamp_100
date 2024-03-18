import sys

from PyQt6.QtCore import QPoint, QPropertyAnimation, QRect, QSize, Qt, pyqtProperty
from PyQt6.QtGui import QBrush, QColor, QFont, QPainter
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200
FONT_SIZE = 12
FONT_WEIGHT = QFont.Weight.Bold
FONT = QFont("Fira Code", FONT_SIZE, FONT_WEIGHT)

THEMES = {
    "light": """
                QWidget {
                    background-color: #ffffff;
                    color: #000000;
                }
                QLabel {
                    color: #000000;
                }
                QLabel:hover {
                    color: #ff0000;
                }
                QLineEdit {
                    background-color: #ffffff;
                    color: #000000;
                    border: 1px solid #000000;
                    border-radius: 3px;
                }
                QLineEdit:focus {
                    border: 1px solid #0000ff;
                }
                QPushButton {
                    border-radius: 17;
                    border: 1px solid black;
                    background-color: #fff;
                }
                QPushButton:hover {
                    color: #000;
                    background-color: #f0f0f0;
                }

            """,
    "dark": """
                QWidget {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QLabel {
                    color: #ffffff;
                }
                QLabel:hover {
                    color: #ff0000;
                }
                QLineEdit {
                    background-color: #2b2b2b;
                    color: #ffffff;
                    border: 1px solid #ffffff;
                    border-radius: 3px;
                }
                QLineEdit:focus {
                    border: 1px solid #ff0000;
                }
                QPushButton {
                    border-radius: 17;
                    border: 1px solid black;
                    background-color: #2b2b2b;
                }
                QPushButton:hover {
                    color: #fff;
                    background-color: #515151;
                }
            """,
}


class AnimatedToggleButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setMaximumWidth(20)
        self.setMaximumHeight(12)

        self._offset = 0

        # Create the animation
        self._animation = QPropertyAnimation(self, b"offset", self)
        self._animation.setDuration(100)  # Duration in milliseconds
        self._animation.setStartValue(0)
        self._animation.setEndValue(1)

        self.clicked.connect(self._animate)

    def _animate(self):
        if self.isChecked():
            self._animation.setDirection(QPropertyAnimation.Direction.Forward)
        else:
            self._animation.setDirection(QPropertyAnimation.Direction.Backward)
        self._animation.start()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        # Draw the background
        background = (
            QColor(119, 119, 119) if self.isChecked() else QColor(221, 221, 221)
        )
        painter.setBrush(QBrush(background))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 12, 12)

        # Draw the circle
        circle_color = QColor(255, 255, 255) if self.isChecked() else QColor(43, 43, 43)
        painter.setBrush(QBrush(circle_color))
        painter.setPen(Qt.PenStyle.NoPen)

        offset = (
            self._animation.currentValue()
            if self._animation.state() == QPropertyAnimation.State.Running
            else int(self.isChecked())
        )
        circle_x = int(offset * (self.width() - self.height()))  # Convert to int
        painter.drawEllipse(circle_x, 0, self.height(), self.height())

    def sizeHint(self):
        return QSize(50, 24)

    @pyqtProperty(float)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
        self.update()


class ComboBoxLineEdit(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.lineEdit = QLineEdit(self)
        self.comboBox = QComboBox(self)

        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.comboBox)

        self.lineEdit.textChanged.connect(self.updateComboBox)

    def updateComboBox(self, text):
        # Update the combo box items based on the line edit text
        # This is just an example, replace with your own logic
        self.comboBox.clear()
        self.comboBox.addItem(text)
        self.comboBox.addItem(text + " item 2")
        self.comboBox.addItem(text + " item 3")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Application")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.current_theme = "light"
        self.setStyleSheet(THEMES[self.current_theme])

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.TitleLayout = QHBoxLayout()

        # creating a push button
        button = QPushButton("⇵", self)
        button.setFont(QFont("Fira Code", 16, QFont.Weight.Medium))

        # setting geometry of button
        button.setGeometry(self.width() // 2 - 20, self.height() // 2 - 10, 35, 35)

        # adding action to a button
        button.clicked.connect(self.clickme)
        button.raise_()

        self.create_title()
        self.input1 = ComboBoxLineEdit()

        self.input2 = QLineEdit("kilómetros")
        self.input2.setMinimumHeight(25)
        self.input2.setFont(FONT)
        self.input2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addWidget(self.input1)
        self.layout.addStretch(1)
        self.layout.addWidget(self.input2)
        self.layout.addStretch(1)

        self.layout.addLayout(self.TitleLayout)
        self.central_widget.setLayout(self.layout)

    def clickme(self):
        number = int(self.input1.lineEdit.text()) * 1.609
        self.input2.setText(str("{:.2f}".format(number)))

    def switch_themes(self, event):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.setStyleSheet(THEMES[self.current_theme])

    def create_title(self):
        """Create a label that closes the window when clicked."""
        close_label = QLabel("X", self)
        title_label = QLabel("Conversor", self)
        close_label.setFont(FONT)
        title_label.setFont(FONT)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        close_label.mousePressEvent = self.close_window

        self.toggle_button = AnimatedToggleButton()
        self.toggle_button.clicked.connect(self.switch_themes)

        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        h_layout.addWidget(title_label)
        h_layout.addStretch(1)

        h_layout.addWidget(self.toggle_button)
        h_layout.addWidget(close_label)

        self.layout.addLayout(h_layout)

    def close_window(self, event):
        """Close the window."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
