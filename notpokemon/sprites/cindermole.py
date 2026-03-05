from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class CindermoleSprite(SpriteRenderer):
    """Pixel art sprite for Cindermole -- a stocky fire mole with glowing digging claws."""

    PALETTE = {
        'D': QColor('#3D1C08'),   # dark charcoal brown body
        'A': QColor('#8C7B6B'),   # ashy gray belly
        'C': QColor('#FF6B00'),   # glowing orange claw tips
        'E': QColor('#FF4500'),   # ember-orange eye
        'B': QColor('#111111'),   # black outline
        'S': QColor('#5A3018'),   # mid brown shading
        'N': QColor('#6B4C2A'),   # snout mid-brown
    }

    # 32 rows x 32 characters each  (columns 0-31)
    # '.' = transparent
    # Side-profile fire mole facing right. Wide rounded body, tiny glowing eye,
    # rounded snout with nostrils on right, stub tail on left,
    # large front digging paws with glowing orange claw tips at bottom.
    #
    #   D = dark body brown    A = ashy belly     C = orange claw tip
    #   E = ember eye          B = black outline  S = mid shading brown
    #   N = snout mid-brown    . = transparent
    GRID = [
        #          1111111111222222222233
        #0123456789012345678901234567890 1
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '......BBBBBBBB..................',  # row  3  back arc top
        '.....BDDDDDDDDSB................',  # row  4  upper back
        '....BDDDDDDDDDSBB...............',  # row  5  back
        '....BDDDDDDDDDDDDSB.............',  # row  6  back/head merge
        '....BDDDEEDDDDDDNBB.............',  # row  7  eye (E) + snout start (N)
        '.....BDDDDDDDDNNNBB.............',  # row  8  snout mid
        '.....BDDDDDDNNNBBB..............',  # row  9  snout tip
        '......BDDDDNNBB.................',  # row 10  nostrils
        '....BDDDDDDDDDDDSB..............',  # row 11  neck/chest
        '...BDDDDDDDDDDDDDDSB............',  # row 12  upper body
        '...BDDDDDDDDDDDDDDSB............',  # row 13  body
        '..BDDDDDDDDDAAAADDSB............',  # row 14  body + belly start
        '..BDDDDDDDDAAAAADDSB............',  # row 15  belly
        '..BDDDDDDDAAAAAADDSB............',  # row 16  belly center
        '..BDDDDDDAAAAAAADDSB............',  # row 17  belly widest
        '..BDDDDDDDAAAAADDSB.............',  # row 18  belly lower
        '..BDDDDDDDDDDDDDDSB.............',  # row 19  lower body
        '...BSSDDDDDDDDDSBB..............',  # row 20  underside taper
        '....BBBDDDDDDDBBB...............',  # row 21  paw/leg tops
        '.BB....BDDDDDB....BB............',  # row 22  legs + stub tail
        '.BB.....BDDDB.....BB............',  # row 23  legs + tail
        '.BB......BDDB.....BB............',  # row 24  lower legs + tail
        '..BB.....BBBB....BBB............',  # row 25  paw tops
        '..BCCC...CCCC....BCB............',  # row 26  claw row
        '..BCCB...CCCB....BCB............',  # row 27  claw tips
        '..BBBB...BBBB....BBB............',  # row 28  claw base
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
