from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class GlacimooseSprite(SpriteRenderer):
    """Pixel art sprite for Glacimoose -- a large ice moose with massive ice-crystal antlers."""

    PALETTE = {
        'M': QColor('#85929E'),   # blue-gray body
        'I': QColor('#A9CCE3'),   # ice blue antlers
        'L': QColor('#D5D8DC'),   # lighter belly
        'D': QColor('#2C3E50'),   # dark hoof / snout
        'K': QColor('#1A252F'),   # dark eye / outline
        'H': QColor('#E8F8FF'),   # icy highlight on antler
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #0         1         2         3
        #01234567890123456789012345678901
        '................................',  # row  0
        '......IH....IH..................',  # row  1  antler tips
        '.....IHHI..IHHI.................',  # row  2  antler tips
        '....IHHII.IHHII.................',  # row  3  antler branch
        '....IIIIIIIIIIII................',  # row  4  antler main beam
        '.....IIHHHHHIII.................',  # row  5  antler mid
        '.....IIHHHHIIII.................',  # row  6  antler base
        '......IIIIIII...................',  # row  7  antler joins head
        '......KMMMMK....................',  # row  8  top of skull
        '.....KMMMMMMK...................',  # row  9  forehead
        '....KMMKMMMMMMK.................',  # row 10  eye row (K=eye)
        '....KMMMMDDDMMMK................',  # row 11  snout area
        '....KMMMMDDDDDMK................',  # row 12  snout / nose
        '.....KMMMMDDDDKK................',  # row 13  lower jaw dark snout
        '......KKMMMMMK..................',  # row 14  neck top
        '.......KMMMMMMK.................',  # row 15  neck
        '......KMMMMMMMMMK...............',  # row 16  shoulder
        '.....KMMMMMMMMMMMMK.............',  # row 17  body front
        '....KMMLLLMMMMMMMMMMK...........',  # row 18  body + belly
        '....KMMLLLLMMMMMMMMMMK..........',  # row 19  belly
        '....KMMLLLLMMMMMMMMMMMK.........',  # row 20  belly wide
        '....KMMLLLMMMMMMMMMMMMK.........',  # row 21  lower body
        '.....KMMMMMMMMMMMMMMMMK.........',  # row 22  rump area
        '.....KMMMMMMMMMMMMMMK...........',  # row 23  rump taper
        '......KMMMMMMMMMMMMK...........K',  # row 24  tail nub right edge
        '....KMMK.KMMK...KMMK...KMMK.....',  # row 25  front/rear legs top
        '....KDDK.KDDK...KDDK...KDDK.....',  # row 26  leg mid dark
        '....KDDK.KDDK...KDDK...KDDK.....',  # row 27  lower legs
        '....KKKK.KKKK...KKKK...KKKK.....',  # row 28  hooves
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
