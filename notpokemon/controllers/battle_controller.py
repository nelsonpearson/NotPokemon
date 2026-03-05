from PySide6.QtCore import QObject, Signal, QTimer

from notpokemon.models.battle import BattleState, BattleEvent, EventType
from notpokemon.models.creature import Creature
from notpokemon.views.battle_view import BattleView


class BattleController(QObject):
    battle_won = Signal()
    battle_lost = Signal()

    EVENT_DELAY_MS = 600

    def __init__(self, player: Creature, opponent: Creature,
                 battle_view: BattleView, parent=None):
        super().__init__(parent)
        self._player = player
        self._opponent = opponent
        self._battle_view = battle_view
        self._battle_state = BattleState(player, opponent)
        self._event_queue: list[BattleEvent] = []
        self._processing = False

        self._battle_view.move_selected.connect(self._on_move_selected)

    def start(self, battle_num: int = 1, total_battles: int = 5):
        self._battle_view.setup_battle(
            self._player, self._opponent, battle_num, total_battles
        )
        self._battle_view.set_moves_enabled(True)

    def _on_move_selected(self, move_index: int):
        if self._processing:
            return

        self._processing = True
        self._battle_view.set_moves_enabled(False)

        player_move = self._player.moves[move_index]
        opponent_move = self._battle_state.pick_ai_move()

        events = self._battle_state.execute_turn(player_move, opponent_move)
        self._event_queue = list(events)
        self._process_next_event()

    def _process_next_event(self):
        if not self._event_queue:
            self._on_turn_complete()
            return

        event = self._event_queue.pop(0)
        self._display_event(event)

    def _display_event(self, event: BattleEvent):
        view = self._battle_view
        is_player_source = event.source == self._player.id
        is_player_target = event.target == self._player.id

        if event.event_type == EventType.MOVE_USED:
            view.show_message(event.message, "#ffffff")
            # Play attack animation for the attacker
            view.play_attack_animation(
                is_player_source,
                callback=lambda: QTimer.singleShot(200, self._process_next_event)
            )
            return

        elif event.event_type == EventType.DAMAGE:
            target_str = "player" if is_player_target else "opponent"
            target_creature = self._player if is_player_target else self._opponent
            view.show_message(event.message, "#ff6b6b")
            view.update_hp(target_str, target_creature.current_hp, target_creature.max_hp)
            view.play_damage_flash(
                is_player_target,
                callback=lambda: QTimer.singleShot(300, self._process_next_event)
            )
            return

        elif event.event_type == EventType.HEAL:
            target_str = "player" if is_player_target else "opponent"
            target_creature = self._player if is_player_target else self._opponent
            view.show_message(event.message, "#2ecc71")
            view.update_hp(target_str, target_creature.current_hp, target_creature.max_hp)

        elif event.event_type == EventType.EFFECTIVENESS:
            view.show_effectiveness(event.message, event.extra)

        elif event.event_type == EventType.STATUS_APPLIED:
            view.show_message(event.message, "#f39c12")

        elif event.event_type == EventType.STATUS_EXPIRED:
            view.show_message(event.message, "#8899aa")

        elif event.event_type == EventType.MISS:
            view.show_message(event.message, "#8899aa")

        elif event.event_type == EventType.FAINT:
            is_player_fainted = event.source == self._player.id
            view.show_message(event.message, "#e74c3c")
            view.play_faint_animation(
                is_player_fainted,
                callback=lambda: QTimer.singleShot(500, self._on_faint(is_player_fainted))
            )
            return

        QTimer.singleShot(self.EVENT_DELAY_MS, self._process_next_event)

    def _on_faint(self, is_player_fainted: bool):
        def _handler():
            self._processing = False
            if is_player_fainted:
                self.battle_lost.emit()
            else:
                self.battle_won.emit()
        return _handler

    def _on_turn_complete(self):
        if self._player.is_fainted:
            self._processing = False
            self.battle_lost.emit()
            return
        if self._opponent.is_fainted:
            self._processing = False
            self.battle_won.emit()
            return

        self._processing = False
        self._battle_view.set_moves_enabled(True)

    def disconnect_signals(self):
        try:
            self._battle_view.move_selected.disconnect(self._on_move_selected)
        except RuntimeError:
            pass
