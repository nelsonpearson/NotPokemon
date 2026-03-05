from __future__ import annotations

import random
from dataclasses import dataclass, field


ALL_CREATURE_IDS = [
    # Original 6
    "emberaptor", "tidalotter", "thornhare",
    "voltlynx", "glacifox", "dunecobra",
    # Fire
    "cindermole", "lavabull", "emberwolf", "pyrotoad",
    # Water
    "bubblewhal", "coralsnap", "tideshark", "mistdeer",
    # Nature
    "mossboar", "leafwing", "bramblebear",
    # Electric
    "zapfinch", "stormhound", "bolttiger",
    # Ice
    "frostmoth", "glacimoose", "chilltoad",
    # Earth
    "mudbison", "stonecrab",
]


@dataclass
class GameState:
    player_creature_id: str | None = None
    opponents_defeated: list[str] = field(default_factory=list)
    current_opponent_index: int = 0
    _opponent_queue: list[str] = field(default_factory=list)

    def get_opponent_queue(self) -> list[str]:
        return self._opponent_queue

    def build_opponent_queue(self):
        """Shuffle opponents so each run is a different order."""
        queue = [cid for cid in ALL_CREATURE_IDS if cid != self.player_creature_id]
        random.shuffle(queue)
        self._opponent_queue = queue

    def get_current_opponent_id(self) -> str | None:
        if self.current_opponent_index < len(self._opponent_queue):
            return self._opponent_queue[self.current_opponent_index]
        return None

    def advance_opponent(self):
        current_id = self._opponent_queue[self.current_opponent_index]
        self.opponents_defeated.append(current_id)
        self.current_opponent_index += 1

    @property
    def is_champion(self) -> bool:
        return self.current_opponent_index >= len(self._opponent_queue)

    def reset(self):
        self.player_creature_id = None
        self.opponents_defeated.clear()
        self.current_opponent_index = 0
        self._opponent_queue = []
