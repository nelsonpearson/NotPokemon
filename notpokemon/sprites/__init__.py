from notpokemon.sprites.base import SpriteRenderer
from notpokemon.sprites.emberaptor import EmberaptorSprite
from notpokemon.sprites.tidalotter import TidalotterSprite
from notpokemon.sprites.thornhare import ThornhareSprite
from notpokemon.sprites.voltlynx import VoltlynxSprite
from notpokemon.sprites.glacifox import GlacifoxSprite
from notpokemon.sprites.dunecobra import DunecobraSprite
from notpokemon.sprites.cindermole import CindermoleSprite
from notpokemon.sprites.lavabull import LavabullSprite
from notpokemon.sprites.emberwolf import EmberwolfSprite
from notpokemon.sprites.pyrotoad import PyrotoadSprite
from notpokemon.sprites.bubblewhal import BubblewhalSprite
from notpokemon.sprites.coralsnap import CoralSnapSprite
from notpokemon.sprites.tideshark import TidesharkSprite
from notpokemon.sprites.mistdeer import MistdeerSprite
from notpokemon.sprites.mossboar import MossboarSprite
from notpokemon.sprites.leafwing import LeafwingSprite
from notpokemon.sprites.bramblebear import BramblebearSprite
from notpokemon.sprites.zapfinch import ZapfinchSprite
from notpokemon.sprites.stormhound import StormhoundSprite
from notpokemon.sprites.bolttiger import BolttigerSprite
from notpokemon.sprites.frostmoth import FrostmothSprite
from notpokemon.sprites.glacimoose import GlacimooseSprite
from notpokemon.sprites.chilltoad import ChilltoadSprite
from notpokemon.sprites.mudbison import MudbisonSprite
from notpokemon.sprites.stonecrab import StonecrabSprite

SPRITE_REGISTRY: dict[str, SpriteRenderer] = {
    "emberaptor": EmberaptorSprite(),
    "tidalotter": TidalotterSprite(),
    "thornhare": ThornhareSprite(),
    "voltlynx": VoltlynxSprite(),
    "glacifox": GlacifoxSprite(),
    "dunecobra": DunecobraSprite(),
    "cindermole": CindermoleSprite(),
    "lavabull": LavabullSprite(),
    "emberwolf": EmberwolfSprite(),
    "pyrotoad": PyrotoadSprite(),
    "bubblewhal": BubblewhalSprite(),
    "coralsnap": CoralSnapSprite(),
    "tideshark": TidesharkSprite(),
    "mistdeer": MistdeerSprite(),
    "mossboar": MossboarSprite(),
    "leafwing": LeafwingSprite(),
    "bramblebear": BramblebearSprite(),
    "zapfinch": ZapfinchSprite(),
    "stormhound": StormhoundSprite(),
    "bolttiger": BolttigerSprite(),
    "frostmoth": FrostmothSprite(),
    "glacimoose": GlacimooseSprite(),
    "chilltoad": ChilltoadSprite(),
    "mudbison": MudbisonSprite(),
    "stonecrab": StonecrabSprite(),
}


def get_sprite(creature_id: str) -> SpriteRenderer:
    return SPRITE_REGISTRY[creature_id]
