import sys
from typing import Optional

from pomodoro import Pomodoro
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui import UI

"""
TODO : When the timer stops, make a beep and change the background image.
TODO : Add button to the left of the play button to switch background randomly
TODO : Add settings button and refactor to make this StackedLayout
TODO : Create a simple spotify widget to the right of the screen
TODO : Refactor themes. Delete slider and create a name label instead
"""


class MainWindow(QMainWindow, UI):
    """
    Main window class for the Pomodoro application.
    """

    def __init__(self, pomodoro: Pomodoro):
        """
        Initialize the main window.

        Args:
            pomodoro (Pomodoro): The Pomodoro instance.
        """
        super().__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setMinimumHeight(550)

        self.theme = "dark"
        # Set the dark theme
        self.setTheme(self.theme)

        self.short_break = True
        self.offset: Optional[QMouseEvent] = None
        self.pomodoro = pomodoro

        self.setup_ui(self)

        self.start_stop_button.clicked.connect(self.start_stop_timer)
        self.toggle_break.clicked.connect(self.switch_break)
        self.close_label.mousePressEvent = self.close_window
        self.timer_widget.timer_finished.connect(self.on_timer_finished)

    def setTheme(self, theme_name: str):
        """
        Set the application theme.

        Args:
            theme_name (str): The name of the theme.
        """
        # Set the application style to Fusion
        with open(f"./styles/{theme_name}.qss", "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def start_stop_timer(self):
        """
        Start or stop the timer based on its current state.
        """
        if self.timer_widget.is_timer_running():
            self.start_stop_button.setIcon(self.icon_play)
            self.timer_widget.stop_timer()
            self.timer_widget.reset_timer()
        else:
            self.start_stop_button.setIcon(self.icon_reset)
            self.timer_widget.start_timer()
        self.timer_widget.update()

    def resizeEvent(self, event):
        """
        Resize the window and the background image.

        Args:
            event: The resize event.
        """
        # Resize the QLabel to fit the window
        self.background_image.resize(event.size())

        # Resize the QMovie to fit the window
        self.background_movie.setScaledSize(event.size())

    def switch_break(self):
        """
        Switch between short break and long break.
        """
        self.short_break = not self.short_break

    def on_timer_finished(self):
        """
        Handle the timer finished event.
        """
        self.timer_widget.new_segment(*self.pomodoro.next_segment())

    def close_window(self, event):
        """
        Close the window.

        Args:
            event: The mouse press event.
        """
        self.close()

    def mousePressEvent(self, event: QMouseEvent):
        """
        Handle the mouse press event.

        Args:
            event (QMouseEvent): The mouse press event.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        """
        Handle the mouse move event.

        Args:
            event (QMouseEvent): The mouse move event.
        """
        if self.draggable:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """
        Handle the mouse release event.

        Args:
            event (QMouseEvent): The mouse release event.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = False
            self.offset = None


if __name__ == "__main__":

    app = QApplication(sys.argv)
    pomodoro = Pomodoro()
    window = MainWindow(pomodoro)
    window.show()
    sys.exit(app.exec())
