from notpokemon.sprites.base import SpriteRenderer
from notpokemon.sprites.emberaptor import EmberaptorSprite
from notpokemon.sprites.tidalotter import TidalotterSprite
from notpokemon.sprites.thornhare import ThornhareSprite
from notpokemon.sprites.voltlynx import VoltlynxSprite
from notpokemon.sprites.glacifox import GlacifoxSprite
from notpokemon.sprites.dunecobra import DunecobraSprite

SPRITE_REGISTRY: dict[str, SpriteRenderer] = {
    "emberaptor": EmberaptorSprite(),
    "tidalotter": TidalotterSprite(),
    "thornhare": ThornhareSprite(),
    "voltlynx": VoltlynxSprite(),
    "glacifox": GlacifoxSprite(),
    "dunecobra": DunecobraSprite(),
}


def get_sprite(creature_id: str) -> SpriteRenderer:
    return SPRITE_REGISTRY[creature_id]
