from typing import Optional

import qtawesome
from constants import (
    BREAK_ACCENT_COLOR,
    BREAK_BASE_COLOR,
    FONT,
    FONT_FAMILY,
    WORKING_ACCENT_COLOR,
    WORKING_BASE_COLOR,
)
from PyQt6.QtCore import QPropertyAnimation, QSize, Qt, QTimer, pyqtProperty, pyqtSignal
from PyQt6.QtGui import QBrush, QColor, QFont, QLinearGradient, QMovie, QPainter, QPen
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget


class TimerWidget(QWidget):
    """
    A custom widget that displays a timer with a progress arc and remaining time.
    """

    timer_finished = pyqtSignal()

    def __init__(self, parent: Optional[QWidget] = None, time_input: int = 1):
        """
        Initialize the TimerWidget.

        Args:
            parent: The parent widget.
            time_input: The initial time in minutes.
        """
        super().__init__(parent)
        self.parent = parent
        self.init_time = parent.pomodoro.next_segment()[0] * 60
        self.time_left = self.init_time
        self.total_time = self.init_time
        self.timer = QTimer()
        self.is_running = False
        self.timer.timeout.connect(self.update_timer)
        self.segment_label = ""
        self.current_base_color = WORKING_BASE_COLOR
        self.current_accent_color = WORKING_ACCENT_COLOR

        self.setFixedSize(300, 300)

    def paintEvent(self, event):
        """
        Paint the TimerWidget.

        Args:
            event: The paint event.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Create a linear gradient
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, self.current_base_color)  # Red at the start
        gradient.setColorAt(1.0, self.current_accent_color)  # Green at the end

        # Set the pen with the gradient
        pen = QPen(QBrush(gradient), 10)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        pen.setWidth(20)
        painter.setPen(pen)

        # Draw the progress arc
        painter.drawArc(
            10,
            10,
            self.width() - 20,
            self.height() - 20,
            90 * 16,
            int(360 * 16 * (self.time_left / self.total_time)),
        )

        if self.parent.theme == "light":
            pen = QPen(QColor(0, 0, 0), 10)
        else:
            pen = QPen(QColor(255, 255, 255), 10)
        painter.setPen(pen)
        # Draw the remaining time
        painter.setFont(QFont(FONT_FAMILY, 50))
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        painter.drawText(
            self.rect().adjusted(0, 0, 0, -self.height() // 5),
            Qt.AlignmentFlag.AlignCenter,
            f"{minutes:02}:{seconds:02}",
        )

        # Draw additional text below the time text
        painter.setFont(FONT)
        painter.drawText(
            self.rect().adjusted(0, self.height() // 4 + 10, 0, 0),
            Qt.AlignmentFlag.AlignCenter,
            self.segment_label,
        )

    def start_timer(self):
        """
        Start the timer.
        """
        self.timer.start(1000)  # update every second
        self.is_running = True
        self.segment_label = "Working\n😒"

    def stop_timer(self):
        """
        Stop the timer.
        """
        self.timer.stop()
        self.is_running = False

    def reset_timer(self):
        """
        Reset the timer to the initial time.
        """
        self.time_left = self.init_time

    def is_timer_running(self) -> bool:
        """
        Check if the timer is running.

        Returns:
            True if the timer is running, False otherwise.
        """
        return self.is_running

    def update_timer(self):
        """
        Update the timer by decreasing the time left and emitting the timer_finished signal if the time is up.
        """
        self.time_left -= 1
        if self.time_left <= 0:
            self.timer_finished.emit()

        self.update()  # trigger a repaint

    def new_segment(self, time: int, segment_name: str):
        """
        Set a new segment with the specified time and segment name.

        Args:
            time: The time in minutes for the new segment.
            segment_name: The name of the new segment.
        """
        self.time_left = time * 60
        self.total_time = time * 60
        if "break" in segment_name.lower():
            self.segment_label = segment_name + "\n😎"
            self.current_base_color = BREAK_BASE_COLOR
            self.current_accent_color = BREAK_ACCENT_COLOR
        else:
            self.segment_label = segment_name + "\n😒"
            self.current_base_color = WORKING_BASE_COLOR
            self.current_accent_color = WORKING_ACCENT_COLOR


class AnimatedToggleButton(QPushButton):
    """
    A custom toggle button with animation.
    """

    def __init__(self, parent: Optional[QWidget] = None):
        """
        Initialize the AnimatedToggleButton.

        Args:
            parent: The parent widget.
        """
        super().__init__(parent)
        self.setCheckable(True)

        self._offset = 0

        # Create the animation
        self._animation = QPropertyAnimation(self, b"offset", self)
        self._animation.setDuration(100)  # Duration in milliseconds
        self._animation.setStartValue(0)
        self._animation.setEndValue(1)

        self.clicked.connect(self._animate)

    def _animate(self):
        """
        Animate the button when clicked.
        """
        if self.isChecked():
            self._animation.setDirection(QPropertyAnimation.Direction.Forward)
        else:
            self._animation.setDirection(QPropertyAnimation.Direction.Backward)
        self._animation.start()

    def paintEvent(self, event):
        """
        Paint the AnimatedToggleButton.

        Args:
            event: The paint event.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        # Draw the background
        background = QColor(200, 200, 200)
        painter.setBrush(QBrush(background))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 12, 12)

        # Draw the circle
        circle_color = WORKING_ACCENT_COLOR
        painter.setBrush(QBrush(circle_color))
        painter.setPen(Qt.PenStyle.NoPen)

        offset = (
            self._animation.currentValue()
            if self._animation.state() == QPropertyAnimation.State.Running
            else int(self.isChecked())
        )
        circle_x = int(offset * (self.width() - self.height()))  # Convert to int
        painter.drawEllipse(circle_x + 3, 3, self.height() - 6, self.height() - 6)

    def sizeHint(self) -> QSize:
        """
        Get the size hint of the AnimatedToggleButton.

        Returns:
            The size hint.
        """
        return QSize(50, 24)

    @pyqtProperty(float)
    def offset(self) -> float:
        """
        Get the offset property of the AnimatedToggleButton.

        Returns:
            The offset value.
        """
        return self._offset

    @offset.setter
    def offset(self, value: float):
        """
        Set the offset property of the AnimatedToggleButton.

        Args:
            value: The offset value.
        """
        self._offset = value
        self.update()


class UI(object):
    """
    The UI class responsible for setting up the user interface.
    """

    def setup_ui(self, parent: QWidget):
        """
        Set up the user interface.

        Args:
            parent: The parent widget.
        """

        # Set background image
        background_filename = "japan"
        self.background_movie = QMovie(f"resources/{background_filename}.gif")
        self.background_movie.setSpeed(70)
        self.background_image = QLabel()
        self.background_image.setMovie(self.background_movie)
        self.background_movie.start()

        # Main Layout is vertical
        self.main_layout = QHBoxLayout()
        self.background_layout = QVBoxLayout()
        self.breaks_layout = QHBoxLayout()
        self.control_layout = QHBoxLayout()

        # Close window "button" (QLabel)
        self.close_label = QLabel()
        self.close_label.setPixmap(
            qtawesome.icon("fa5s.times", color="white").pixmap(24, 24)
        )

        # Container widget (for background purposes)
        self.background_widget = QWidget()
        self.background_widget.setObjectName("background_widget")
        self.background_widget.setStyleSheet(
            "#background_widget {background-color: #90000000; border-radius: 10px}"
        )

        self.background_widget.setLayout(self.background_layout)

        # Top row of the app
        self.short_break_label = QLabel("Short Break")
        self.long_break_label = QLabel("Long Break")
        self.short_break_label.setFont(FONT)
        self.long_break_label.setFont(FONT)
        self.toggle_break = AnimatedToggleButton()
        self.breaks_layout.addStretch()
        self.breaks_layout.addWidget(self.short_break_label)
        self.breaks_layout.addWidget(self.toggle_break)
        self.breaks_layout.addWidget(self.long_break_label)
        self.breaks_layout.addStretch()
        self.background_layout.addLayout(self.breaks_layout)
        self.background_layout.addStretch()

        # Central row of the app
        self.timer_widget = TimerWidget(parent)
        self.background_layout.addWidget(self.timer_widget)
        self.background_layout.setAlignment(
            self.timer_widget, Qt.AlignmentFlag.AlignCenter
        )

        # Bottom row of the app
        self.start_stop_button = QPushButton()
        # if parent.theme == "light":
        #     self.icon_play = qtawesome.icon("fa5s.play", color="#515151")
        #     self.icon_reset = qtawesome.icon("fa5s.undo", color="#515151")
        # if parent.theme == "dark":
        self.icon_play = qtawesome.icon("fa5s.play", color="white")
        self.icon_reset = qtawesome.icon("fa5s.undo", color="white")
        self.start_stop_button.setIcon(self.icon_play)
        self.start_stop_button.setIconSize(QSize(24, 24))
        button_size = 100
        self.start_stop_button.setMinimumSize(button_size, button_size)
        self.start_stop_button.setStyleSheet(f"border-radius: {button_size // 2}px")

        self.background_button = QPushButton()
        self.background_button.setIcon(qtawesome.icon("fa5s.images", color="white"))
        self.background_button.setIconSize(QSize(18, 18))
        button_size = 50
        self.background_button.setMinimumSize(button_size, button_size)
        self.background_button.setStyleSheet(f"border-radius: {button_size // 2}px")

        self.settings_button = QPushButton()
        self.settings_button.setIcon(qtawesome.icon("fa5s.cog", color="white"))
        self.settings_button.setIconSize(QSize(18, 18))
        button_size = 50
        self.settings_button.setMinimumSize(button_size, button_size)
        self.settings_button.setStyleSheet(f"border-radius: {button_size // 2}px")

        self.control_layout.addStretch()
        self.control_layout.addWidget(self.background_button)
        self.control_layout.setAlignment(
            self.background_button, Qt.AlignmentFlag.AlignBottom
        )
        self.control_layout.addWidget(self.start_stop_button)
        self.control_layout.addWidget(self.settings_button)
        self.control_layout.setAlignment(
            self.settings_button, Qt.AlignmentFlag.AlignBottom
        )
        self.control_layout.addStretch()

        self.background_layout.addStretch()
        self.background_layout.addLayout(self.control_layout)
        self.main_layout.addWidget(self.background_widget)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.close_label)
        self.main_layout.setAlignment(self.close_label, Qt.AlignmentFlag.AlignTop)

        # setting the central widget
        self.background_image.setLayout(self.main_layout)
        parent.setCentralWidget(self.background_image)
