from __future__ import annotations

from dataclasses import dataclass, field


ALL_CREATURE_IDS = [
    "emberaptor", "tidalotter", "thornhare",
    "voltlynx", "glacifox", "dunecobra",
]


@dataclass
class GameState:
    player_creature_id: str | None = None
    opponents_defeated: list[str] = field(default_factory=list)
    current_opponent_index: int = 0

    def get_opponent_queue(self) -> list[str]:
        return [cid for cid in ALL_CREATURE_IDS if cid != self.player_creature_id]

    def get_current_opponent_id(self) -> str | None:
        queue = self.get_opponent_queue()
        if self.current_opponent_index < len(queue):
            return queue[self.current_opponent_index]
        return None

    def advance_opponent(self):
        queue = self.get_opponent_queue()
        current_id = queue[self.current_opponent_index]
        self.opponents_defeated.append(current_id)
        self.current_opponent_index += 1

    @property
    def is_champion(self) -> bool:
        return self.current_opponent_index >= len(self.get_opponent_queue())

    def reset(self):
        self.player_creature_id = None
        self.opponents_defeated.clear()
        self.current_opponent_index = 0
