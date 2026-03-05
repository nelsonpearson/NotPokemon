from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPainter, QFont, QColor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel,
    QPushButton, QFrame, QSizePolicy,
)

from notpokemon.constants import TYPE_COLORS, HIGHLIGHT_COLOR
from notpokemon.models.creature import Creature
from notpokemon.views.widgets.sprite_widget import SpriteWidget
from notpokemon.views.widgets.type_badge import TypeBadge
from notpokemon.sprites import get_sprite


class CreatureCard(QFrame):
    clicked = Signal(str)

    def __init__(self, creature: Creature, parent=None):
        super().__init__(parent)
        self._creature = creature
        self._selected = False
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(230, 260)
        self._setup_ui()
        self._update_style()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(4)
        layout.setContentsMargins(8, 8, 8, 8)

        # Sprite
        sprite = SpriteWidget(get_sprite(self._creature.id), scale=3, parent=self)
        layout.addWidget(sprite, alignment=Qt.AlignmentFlag.AlignCenter)

        # Name
        name_label = QLabel(self._creature.name)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setStyleSheet("color: #ffffff; font-family: monospace; font-size: 14px; font-weight: bold; background: transparent;")
        layout.addWidget(name_label)

        # Type badge
        badge = TypeBadge(self._creature.element, self)
        layout.addWidget(badge, alignment=Qt.AlignmentFlag.AlignCenter)

        # Stats
        stats_widget = QWidget()
        stats_widget.setStyleSheet("background: transparent;")
        stats_layout = QGridLayout(stats_widget)
        stats_layout.setSpacing(2)
        stats_layout.setContentsMargins(4, 2, 4, 2)

        stat_names = ["HP", "ATK", "DEF", "SPD"]
        stat_values = [
            self._creature.max_hp,
            self._creature.attack,
            self._creature.defense,
            self._creature.speed,
        ]

        for i, (name, value) in enumerate(zip(stat_names, stat_values)):
            label = QLabel(name)
            label.setStyleSheet("color: #8899aa; font-family: monospace; font-size: 10px; background: transparent;")
            stats_layout.addWidget(label, i, 0)

            bar = StatBar(value, parent=stats_widget)
            stats_layout.addWidget(bar, i, 1)

            val_label = QLabel(str(value))
            val_label.setStyleSheet("color: #cccccc; font-family: monospace; font-size: 10px; background: transparent;")
            val_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            stats_layout.addWidget(val_label, i, 2)

        layout.addWidget(stats_widget)

    def set_selected(self, selected: bool):
        self._selected = selected
        self._update_style()

    def _update_style(self):
        if self._selected:
            self.setStyleSheet(f"""
                CreatureCard {{
                    background-color: #1e2d4d;
                    border: 3px solid {HIGHLIGHT_COLOR.name()};
                    border-radius: 8px;
                }}
            """)
        else:
            self.setStyleSheet("""
                CreatureCard {
                    background-color: #16213e;
                    border: 2px solid #2c3e6b;
                    border-radius: 8px;
                }
                CreatureCard:hover {
                    border-color: #4a6fa5;
                    background-color: #1a2844;
                }
            """)

    def mousePressEvent(self, event):
        self.clicked.emit(self._creature.id)
        super().mousePressEvent(event)


class StatBar(QWidget):
    def __init__(self, value: int, max_value: int = 100, parent=None):
        super().__init__(parent)
        self._value = value
        self._max_value = max_value
        self.setFixedSize(80, 10)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()
        h = self.height()

        # Background
        painter.setBrush(QColor(30, 30, 30))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, w, h, 3, 3)

        # Fill
        fill_w = int(w * min(1.0, self._value / self._max_value))
        if fill_w > 0:
            frac = self._value / self._max_value
            if frac > 0.7:
                color = QColor("#2ecc71")
            elif frac > 0.4:
                color = QColor("#f1c40f")
            else:
                color = QColor("#e74c3c")
            painter.setBrush(color)
            painter.drawRoundedRect(0, 0, fill_w, h, 3, 3)

        painter.end()


class SelectionView(QWidget):
    creature_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._cards: dict[str, CreatureCard] = {}
        self._selected_id: str | None = None
        self._confirm_btn: QPushButton | None = None
        self._layout = QVBoxLayout(self)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def set_creatures(self, creatures: list[Creature]):
        # Clear existing
        while self._layout.count():
            item = self._layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self._cards.clear()
        self._selected_id = None

        # Header
        header = QLabel("Choose Your Creature")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet(
            "color: #f39c12; font-family: monospace; font-size: 22px; "
            "font-weight: bold; background: transparent; margin: 10px;"
        )
        self._layout.addWidget(header)

        # Grid of cards (2 rows x 3 cols)
        grid_widget = QWidget()
        grid_widget.setStyleSheet("background: transparent;")
        grid_layout = QGridLayout(grid_widget)
        grid_layout.setSpacing(12)

        for i, creature in enumerate(creatures):
            row = i // 3
            col = i % 3
            card = CreatureCard(creature, self)
            card.clicked.connect(self._on_card_clicked)
            grid_layout.addWidget(card, row, col)
            self._cards[creature.id] = card

        self._layout.addWidget(grid_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        # Confirm button
        self._confirm_btn = QPushButton("CONFIRM")
        self._confirm_btn.setFixedSize(180, 44)
        self._confirm_btn.setEnabled(False)
        self._confirm_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: #2c3e6b;
                color: #8899aa;
                border: 2px solid #3d5291;
                border-radius: 8px;
                font-family: monospace;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:enabled {
                color: #e0e0e0;
                border-color: #f39c12;
            }
            QPushButton:enabled:hover {
                background-color: #3d5291;
                color: #ffffff;
            }
        """)
        self._confirm_btn.clicked.connect(self._on_confirm)
        self._layout.addWidget(self._confirm_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def _on_card_clicked(self, creature_id: str):
        self._selected_id = creature_id
        for cid, card in self._cards.items():
            card.set_selected(cid == creature_id)
        if self._confirm_btn:
            self._confirm_btn.setEnabled(True)

    def _on_confirm(self):
        if self._selected_id:
            self.creature_selected.emit(self._selected_id)
