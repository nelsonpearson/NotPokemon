from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property
from PySide6.QtGui import QPainter, QColor, QLinearGradient
from PySide6.QtWidgets import QWidget

from notpokemon.constants import HP_GREEN, HP_YELLOW, HP_RED


class HpBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._fraction = 1.0
        self._max_hp = 100
        self._current_hp = 100
        self.setFixedHeight(20)
        self.setMinimumWidth(120)

        self._animation = QPropertyAnimation(self, b"fraction")
        self._animation.setDuration(600)
        self._animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

    def _get_fraction(self) -> float:
        return self._fraction

    def _set_fraction(self, value: float):
        self._fraction = max(0.0, min(1.0, value))
        self.update()

    fraction = Property(float, _get_fraction, _set_fraction)

    def set_hp(self, current_hp: int, max_hp: int, animate: bool = True):
        self._max_hp = max_hp
        self._current_hp = current_hp
        target = current_hp / max_hp if max_hp > 0 else 0

        if animate:
            self._animation.stop()
            self._animation.setStartValue(self._fraction)
            self._animation.setEndValue(target)
            self._animation.start()
        else:
            self._fraction = target
            self.update()

    def _bar_color(self) -> QColor:
        if self._fraction > 0.5:
            return HP_GREEN
        elif self._fraction > 0.25:
            return HP_YELLOW
        else:
            return HP_RED

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()
        h = self.height()

        # Background
        painter.setBrush(QColor(40, 40, 40))
        painter.setPen(QColor(80, 80, 80))
        painter.drawRoundedRect(0, 0, w - 1, h - 1, 4, 4)

        # Fill
        fill_w = int((w - 4) * self._fraction)
        if fill_w > 0:
            color = self._bar_color()
            gradient = QLinearGradient(2, 2, 2, h - 4)
            gradient.setColorAt(0, color.lighter(120))
            gradient.setColorAt(1, color)
            painter.setBrush(gradient)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRoundedRect(2, 2, fill_w, h - 4, 3, 3)

        # HP text
        painter.setPen(QColor(255, 255, 255))
        hp_text = f"{max(0, self._current_hp)}/{self._max_hp}"
        painter.drawText(0, 0, w, h, Qt.AlignmentFlag.AlignCenter, hp_text)

        painter.end()
