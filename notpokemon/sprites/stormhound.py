from PySide6.QtGui import QColor, QPainter

from notpokemon.sprites.base import SpriteRenderer


class StormhoundSprite(SpriteRenderer):
    """Sprite for Stormhound – an electric hound with lightning stripe and cloud fur puffs."""

    PALETTE = {
        'O': QColor('#111111'),   # dark outline
        'G': QColor('#626567'),   # steel gray body
        'Y': QColor('#FFD700'),   # bright yellow lightning stripe
        'W': QColor('#F2F3F4'),   # white fur puffs
        'D': QColor('#2C2C2C'),   # dark charcoal snout/paws
        'B': QColor('#3498DB'),   # blue eye
    }

    # 32x32 pixel grid — '.' is transparent
    # Medium hound in side profile facing right. Pointed ears. Cloud-like
    # fur puffs on shoulders. Lightning stripe along body. Crackling tail.
    #
    # Palette key:
    #   O = outline (#111111)  G = steel gray (#626567)
    #   Y = lightning (#FFD700) W = white puff (#F2F3F4)
    #   D = dark snout (#2C2C2C) B = blue eye (#3498DB)
    #   . = transparent
    GRID = [
        # 0         1         2         3
        # 01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '.........OO.....................',  # row  2  ear tips
        '........OGGO....................',  # row  3  pointed ears
        '........OGGGO...................',  # row  4
        '.......OOGGGOOO.................',  # row  5  ear base
        '......OWWWGGGGGO................',  # row  6  shoulder puff + head
        '.....OWWWWWGGGGGOO..............',  # row  7  cloud puff
        '.....OWWWWWGGGGGBGO.............',  # row  8  eye
        '....OWWWWWWGGGGGGGOO............',  # row  9
        '....OWWWWWWGGGGGGDDO............',  # row 10  snout
        '....OWWWWWWGGGGGGDDDO...........',  # row 11  snout ext
        '.....OOOOOOGGGGGDDDDOO..........',  # row 12  neck/snout merge
        '......OGGGGGGGGGGDOO............',  # row 13
        '.....OYGGGGGGGGGGGOO............',  # row 14  lightning stripe
        '....OYYGGGGGGGGGGGGO............',  # row 15
        '....OYYYGGGGGGGGGGGOO...........',  # row 16
        '...OYYYYGGGGGGGGGGGGOO..........',  # row 17  body stripe wide
        '...OYYYYYGGGGGGGGGGGGO..........',  # row 18
        '...OYYYYYGGGGGGGGGGGOO..........',  # row 19
        '...OYYYYYGGGGGGGGGGOYYOO........',  # row 20  tail start
        '....OYYYYGGGGGGGGGOYYYY.........',  # row 21  tail crackling
        '....OYYYGGGGGGGGGOYYYYY.........',  # row 22
        '.....OYYGGGGGGGG.OYYYYY.........',  # row 23
        '.....OOOGGGGGGG...OYYYY.........',  # row 24  belly
        '....OGGGOOO..OOO...OYYY.........',  # row 25  leg separation
        '....OGGGO....OGGO...OYO.........',  # row 26  upper legs
        '....ODGGO....ODGGO..............',  # row 27  dark paws start
        '....ODDGO....ODDGO..............',  # row 28
        '....ODDDO....ODDDO..............',  # row 29  paw pads
        '....OOOOO....OOOOO..............',  # row 30  feet base
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
