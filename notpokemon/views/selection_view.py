from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout, QLabel,
    QPushButton, QFrame, QScrollArea,
)

from notpokemon.constants import HIGHLIGHT_COLOR
from notpokemon.models.creature import Creature
from notpokemon.views.widgets.sprite_widget import SpriteWidget
from notpokemon.views.widgets.type_badge import TypeBadge
from notpokemon.sprites import get_sprite

COLS = 4          # cards per row
CARD_W = 165      # 4 × 165 + 3 × 14 = 702px — fits 800px window
CARD_H = 185
H_GAP = 14
V_GAP = 14


class CreatureCard(QFrame):
    clicked = Signal(str)

    def __init__(self, creature: Creature, parent=None):
        super().__init__(parent)
        self._creature = creature
        self._selected = False
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(CARD_W, CARD_H)
        self._setup_ui()
        self._update_style()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(2)
        layout.setContentsMargins(6, 5, 6, 5)

        sprite = SpriteWidget(get_sprite(self._creature.id), scale=2, parent=self)
        layout.addWidget(sprite, alignment=Qt.AlignmentFlag.AlignCenter)

        name_label = QLabel(self._creature.name)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setStyleSheet(
            "color: #ffffff; font-family: monospace; font-size: 11px; "
            "font-weight: bold; background: transparent;"
        )
        layout.addWidget(name_label)

        badge = TypeBadge(self._creature.element, self)
        layout.addWidget(badge, alignment=Qt.AlignmentFlag.AlignCenter)

        stats_widget = QWidget()
        stats_widget.setStyleSheet("background: transparent;")
        stats_layout = QGridLayout(stats_widget)
        stats_layout.setSpacing(1)
        stats_layout.setContentsMargins(2, 1, 2, 1)

        stat_names = ["HP", "ATK", "DEF", "SPD"]
        stat_values = [
            self._creature.max_hp,
            self._creature.attack,
            self._creature.defense,
            self._creature.speed,
        ]
        stat_max = [210, 110, 110, 120]

        for i, (sname, sval, smax) in enumerate(zip(stat_names, stat_values, stat_max)):
            lbl = QLabel(sname)
            lbl.setStyleSheet(
                "color: #8899aa; font-family: monospace; font-size: 8px; background: transparent;"
            )
            stats_layout.addWidget(lbl, i, 0)

            bar = StatBar(sval, smax, parent=stats_widget)
            stats_layout.addWidget(bar, i, 1)

            val_lbl = QLabel(str(sval))
            val_lbl.setStyleSheet(
                "color: #cccccc; font-family: monospace; font-size: 8px; background: transparent;"
            )
            val_lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
            stats_layout.addWidget(val_lbl, i, 2)

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
                    border-radius: 6px;
                }}
            """)
        else:
            self.setStyleSheet("""
                CreatureCard {
                    background-color: #16213e;
                    border: 2px solid #2c3e6b;
                    border-radius: 6px;
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
        self.setFixedSize(65, 8)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()

        painter.setBrush(QColor(30, 30, 30))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, w, h, 2, 2)

        fill_w = int(w * min(1.0, self._value / self._max_value))
        if fill_w > 0:
            frac = self._value / self._max_value
            color = QColor("#2ecc71") if frac > 0.65 else (
                QColor("#f1c40f") if frac > 0.35 else QColor("#e74c3c")
            )
            painter.setBrush(color)
            painter.drawRoundedRect(0, 0, fill_w, h, 2, 2)

        painter.end()


class SelectionView(QWidget):
    creature_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._cards: dict[str, CreatureCard] = {}
        self._selected_id: str | None = None
        self._confirm_btn: QPushButton | None = None

        outer = QVBoxLayout(self)
        outer.setSpacing(6)
        outer.setContentsMargins(10, 8, 10, 8)

        header = QLabel("Choose Your Creature")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet(
            "color: #f39c12; font-family: monospace; font-size: 20px; "
            "font-weight: bold; background: transparent;"
        )
        outer.addWidget(header)

        # Scrollable card grid
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self._scroll.setStyleSheet("""
            QScrollArea { border: none; background: transparent; }
            QScrollBar:vertical {
                background: #0d1526; width: 8px; border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #2c3e6b; border-radius: 4px; min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0px; }
        """)

        self._grid_container = QWidget()
        self._grid_container.setStyleSheet("background: transparent;")
        self._grid_layout = QGridLayout(self._grid_container)
        self._grid_layout.setHorizontalSpacing(H_GAP)
        self._grid_layout.setVerticalSpacing(V_GAP)
        self._grid_layout.setContentsMargins(8, 8, 8, 8)

        self._scroll.setWidget(self._grid_container)
        outer.addWidget(self._scroll, stretch=1)

        self._confirm_btn = QPushButton("CONFIRM")
        self._confirm_btn.setFixedSize(180, 40)
        self._confirm_btn.setEnabled(False)
        self._confirm_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: #2c3e6b; color: #8899aa;
                border: 2px solid #3d5291; border-radius: 8px;
                font-family: monospace; font-size: 14px; font-weight: bold;
            }
            QPushButton:enabled { color: #e0e0e0; border-color: #f39c12; }
            QPushButton:enabled:hover { background-color: #3d5291; color: #ffffff; }
        """)
        self._confirm_btn.clicked.connect(self._on_confirm)
        outer.addWidget(self._confirm_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def set_creatures(self, creatures: list[Creature]):
        while self._grid_layout.count():
            item = self._grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self._cards.clear()
        self._selected_id = None
        if self._confirm_btn:
            self._confirm_btn.setEnabled(False)

        for i, creature in enumerate(creatures):
            card = CreatureCard(creature, self._grid_container)
            card.clicked.connect(self._on_card_clicked)
            self._grid_layout.addWidget(card, i // COLS, i % COLS)
            self._cards[creature.id] = card

        self._scroll.verticalScrollBar().setValue(0)

    def _on_card_clicked(self, creature_id: str):
        self._selected_id = creature_id
        for cid, card in self._cards.items():
            card.set_selected(cid == creature_id)
        if self._confirm_btn:
            self._confirm_btn.setEnabled(True)
        self._scroll.ensureWidgetVisible(self._cards[creature_id])

    def _on_confirm(self):
        if self._selected_id:
            self.creature_selected.emit(self._selected_id)
