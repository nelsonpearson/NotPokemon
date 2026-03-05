from PySide6.QtCore import QObject

from notpokemon.models.game_state import GameState
from notpokemon.data.creatures import create_creature, get_all_creature_ids
from notpokemon.controllers.battle_controller import BattleController
from notpokemon.views.main_window import MainWindow
from notpokemon.views.title_view import TitleView
from notpokemon.views.selection_view import SelectionView
from notpokemon.views.battle_view import BattleView
from notpokemon.views.result_view import ResultView


class GameController(QObject):
    def __init__(self):
        super().__init__()
        self._game_state = GameState()
        self._battle_controller: BattleController | None = None

        # Create main window and views
        self._window = MainWindow()
        self._title_view = TitleView()
        self._selection_view = SelectionView()
        self._battle_view = BattleView()
        self._result_view = ResultView()

        # Add screens to stack
        self._title_idx = self._window.add_screen(self._title_view, "title")
        self._selection_idx = self._window.add_screen(self._selection_view, "selection")
        self._battle_idx = self._window.add_screen(self._battle_view, "battle")
        self._result_idx = self._window.add_screen(self._result_view, "result")

        # Wire view signals
        self._title_view.start_clicked.connect(self._show_selection)
        self._selection_view.creature_selected.connect(self._on_creature_selected)
        self._result_view.next_clicked.connect(self._start_next_battle)
        self._result_view.retry_clicked.connect(self._retry_battle)
        self._result_view.quit_clicked.connect(self._return_to_title)

    def start(self):
        self._window.show_screen(self._title_idx)
        self._window.show()

    def _show_selection(self):
        creatures = [create_creature(cid) for cid in get_all_creature_ids()]
        self._selection_view.set_creatures(creatures)
        self._window.show_screen(self._selection_idx)

    def _on_creature_selected(self, creature_id: str):
        self._game_state.reset()
        self._game_state.player_creature_id = creature_id
        self._game_state.build_opponent_queue()
        self._start_next_battle()

    def _start_next_battle(self):
        opponent_id = self._game_state.get_current_opponent_id()
        if opponent_id is None:
            self._show_champion()
            return

        # Create fresh creature instances
        player = create_creature(self._game_state.player_creature_id)
        opponent = create_creature(opponent_id)

        # Clean up old battle controller
        if self._battle_controller:
            self._battle_controller.disconnect_signals()
            self._battle_controller.deleteLater()

        # Create new battle controller
        battle_num = self._game_state.current_opponent_index + 1
        total_battles = len(self._game_state.get_opponent_queue())

        self._battle_controller = BattleController(
            player, opponent, self._battle_view, parent=self
        )
        self._battle_controller.battle_won.connect(self._on_battle_won)
        self._battle_controller.battle_lost.connect(self._on_battle_lost)

        self._window.show_screen(self._battle_idx)
        self._battle_controller.start(battle_num, total_battles)

    def _on_battle_won(self):
        self._game_state.advance_opponent()
        if self._game_state.is_champion:
            self._show_champion()
        else:
            self._result_view.show_victory(is_champion=False)
            self._window.show_screen(self._result_idx)

    def _on_battle_lost(self):
        self._result_view.show_defeat()
        self._window.show_screen(self._result_idx)

    def _show_champion(self):
        self._result_view.show_victory(is_champion=True)
        self._window.show_screen(self._result_idx)

    def _retry_battle(self):
        self._start_next_battle()

    def _return_to_title(self):
        self._game_state.reset()
        self._window.show_screen(self._title_idx)
