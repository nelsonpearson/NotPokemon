from PySide6.QtCore import Qt, Signal, QTimer, QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QSizePolicy,
)

from notpokemon.constants import TYPE_COLORS
from notpokemon.models.creature import Creature
from notpokemon.sprites import get_sprite
from notpokemon.views.widgets.hp_bar import HpBar
from notpokemon.views.widgets.sprite_widget import SpriteWidget
from notpokemon.views.widgets.move_button import MoveButton
from notpokemon.views.widgets.type_badge import TypeBadge
from notpokemon.views.widgets.message_log import MessageLog


class BattleView(QWidget):
    move_selected = Signal(int)
    animation_finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._player_sprite: SpriteWidget | None = None
        self._opponent_sprite: SpriteWidget | None = None
        self._player_hp_bar: HpBar | None = None
        self._opponent_hp_bar: HpBar | None = None
        self._player_name_label: QLabel | None = None
        self._opponent_name_label: QLabel | None = None
        self._player_type_badge: TypeBadge | None = None
        self._opponent_type_badge: TypeBadge | None = None
        self._move_buttons: list[MoveButton] = []
        self._message_log: MessageLog | None = None
        self._battle_number_label: QLabel | None = None
        self._setup_ui()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(4)
        main_layout.setContentsMargins(16, 8, 16, 8)

        # Battle number label
        self._battle_number_label = QLabel("")
        self._battle_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._battle_number_label.setStyleSheet(
            "color: #8899aa; font-family: monospace; font-size: 12px; background: transparent;"
        )
        main_layout.addWidget(self._battle_number_label)

        # === Arena area ===
        arena = QFrame()
        arena.setStyleSheet("QFrame { background-color: #0d1526; border-radius: 8px; }")
        arena_layout = QVBoxLayout(arena)
        arena_layout.setContentsMargins(16, 8, 16, 8)

        # Opponent info row (top) — right-aligned to sit above the opponent sprite
        opp_info = QHBoxLayout()
        self._opponent_name_label = QLabel("Opponent")
        self._opponent_name_label.setStyleSheet(
            "color: #ffffff; font-family: monospace; font-size: 14px; font-weight: bold; background: transparent;"
        )
        self._opponent_type_badge = TypeBadge()
        self._opponent_hp_bar = HpBar()
        self._opponent_hp_bar.setFixedWidth(180)
        opp_info.addStretch()
        opp_info.addWidget(self._opponent_hp_bar)
        opp_info.addWidget(self._opponent_type_badge)
        opp_info.addWidget(self._opponent_name_label)
        arena_layout.addLayout(opp_info)

        # Sprites row
        sprites_layout = QHBoxLayout()
        sprites_layout.setContentsMargins(20, 0, 20, 0)

        # Player sprite (bottom-left) - faces right (normal orientation)
        self._player_sprite = SpriteWidget(scale=4)
        # Opponent sprite (top-right) - faces left (flipped)
        self._opponent_sprite = SpriteWidget(scale=4, flipped=True)

        sprites_layout.addWidget(self._player_sprite, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
        sprites_layout.addStretch()
        sprites_layout.addWidget(self._opponent_sprite, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        arena_layout.addLayout(sprites_layout)

        # Player info row (bottom) — left-aligned to sit below the player sprite
        player_info = QHBoxLayout()
        self._player_name_label = QLabel("Player")
        self._player_name_label.setStyleSheet(
            "color: #ffffff; font-family: monospace; font-size: 14px; font-weight: bold; background: transparent;"
        )
        self._player_type_badge = TypeBadge()
        self._player_hp_bar = HpBar()
        self._player_hp_bar.setFixedWidth(180)
        player_info.addWidget(self._player_name_label)
        player_info.addWidget(self._player_type_badge)
        player_info.addWidget(self._player_hp_bar)
        player_info.addStretch()
        arena_layout.addLayout(player_info)

        main_layout.addWidget(arena, stretch=1)

        # === Message log ===
        self._message_log = MessageLog()
        main_layout.addWidget(self._message_log)

        # === Move buttons ===
        moves_layout = QHBoxLayout()
        moves_layout.setSpacing(8)
        for i in range(4):
            btn = MoveButton(i)
            btn.move_clicked.connect(self._on_move_clicked)
            self._move_buttons.append(btn)
            moves_layout.addWidget(btn)
        main_layout.addLayout(moves_layout)

    def setup_battle(self, player: Creature, opponent: Creature,
                     battle_num: int = 1, total_battles: int = 5):
        # Set names and types
        self._player_name_label.setText(player.name)
        self._opponent_name_label.setText(opponent.name)
        self._player_type_badge.set_element(player.element)
        self._opponent_type_badge.set_element(opponent.element)

        # Set HP bars
        self._player_hp_bar.set_hp(player.current_hp, player.max_hp, animate=False)
        self._opponent_hp_bar.set_hp(opponent.current_hp, opponent.max_hp, animate=False)

        # Set sprites
        player_renderer = get_sprite(player.id)
        opponent_renderer = get_sprite(opponent.id)
        self._player_sprite.set_renderer(player_renderer, flipped=False)
        self._opponent_sprite.set_renderer(opponent_renderer, flipped=True)

        # Set moves
        for i, move in enumerate(player.moves):
            if i < len(self._move_buttons):
                self._move_buttons[i].set_move(move)
                self._move_buttons[i].setEnabled(True)
                self._move_buttons[i].setVisible(True)

        # Hide extra buttons if creature has < 4 moves
        for i in range(len(player.moves), 4):
            self._move_buttons[i].setVisible(False)

        # Battle number
        self._battle_number_label.setText(f"Battle {battle_num} of {total_battles}")

        # Clear log
        self._message_log.clear_log()
        self._message_log.add_message(
            f"A wild {opponent.name} appeared!", "#f39c12"
        )

    def update_hp(self, target: str, current_hp: int, max_hp: int):
        if target == "player":
            self._player_hp_bar.set_hp(current_hp, max_hp, animate=True)
        else:
            self._opponent_hp_bar.set_hp(current_hp, max_hp, animate=True)

    def show_message(self, text: str, color: str = "#e0e0e0"):
        self._message_log.add_message(text, color)

    def show_effectiveness(self, text: str, effective_type: str):
        self._message_log.add_effectiveness(text, effective_type)

    def set_moves_enabled(self, enabled: bool):
        for btn in self._move_buttons:
            btn.setEnabled(enabled)

    def play_attack_animation(self, is_player: bool, callback=None):
        sprite = self._player_sprite if is_player else self._opponent_sprite
        direction = 30 if is_player else -30

        anim = QPropertyAnimation(sprite, b"offset_x")
        anim.setDuration(150)
        anim.setKeyValueAt(0, 0)
        anim.setKeyValueAt(0.5, direction)
        anim.setKeyValueAt(1.0, 0)
        anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        if callback:
            anim.finished.connect(callback)
        anim.start()
        # Keep reference so it isn't garbage collected
        self._current_anim = anim

    def play_damage_flash(self, is_player: bool, callback=None):
        sprite = self._player_sprite if is_player else self._opponent_sprite

        anim = QPropertyAnimation(sprite, b"opacity")
        anim.setDuration(300)
        anim.setKeyValueAt(0, 1.0)
        anim.setKeyValueAt(0.25, 0.3)
        anim.setKeyValueAt(0.5, 1.0)
        anim.setKeyValueAt(0.75, 0.3)
        anim.setKeyValueAt(1.0, 1.0)
        if callback:
            anim.finished.connect(callback)
        anim.start()
        self._current_anim = anim

    def play_faint_animation(self, is_player: bool, callback=None):
        sprite = self._player_sprite if is_player else self._opponent_sprite

        group = QSequentialAnimationGroup(self)

        fade = QPropertyAnimation(sprite, b"opacity")
        fade.setDuration(400)
        fade.setStartValue(1.0)
        fade.setEndValue(0.0)
        group.addAnimation(fade)

        slide = QPropertyAnimation(sprite, b"offset_y")
        slide.setDuration(400)
        slide.setStartValue(0)
        slide.setEndValue(50)
        group.addAnimation(slide)

        if callback:
            group.finished.connect(callback)
        group.start()
        self._current_anim = group

    def _on_move_clicked(self, move_index: int):
        self.move_selected.emit(move_index)
