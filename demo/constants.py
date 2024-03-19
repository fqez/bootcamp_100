from PyQt6.QtGui import QColor, QFont

WINDOW_WIDTH: int = 400
WINDOW_HEIGHT: int = 200
FONT_SIZE: int = 14
FONT_FAMILY: str = "Roboto"
FONT_WEIGHT: QFont.Weight = QFont.Weight.Medium
FONT: QFont = QFont(FONT_FAMILY, FONT_SIZE, FONT_WEIGHT)

WORKING_ACCENT_COLOR: QColor = QColor(255, 0, 0)
WORKING_BASE_COLOR: QColor = QColor(255, 0, 0)
BREAK_ACCENT_COLOR: QColor = QColor(0, 255, 0)
BREAK_BASE_COLOR: QColor = QColor(0, 255, 0)
