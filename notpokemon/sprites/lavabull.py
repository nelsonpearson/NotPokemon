from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class LavabullSprite(SpriteRenderer):
    """Pixel art sprite for Lavabull -- a massive fire bull with lava-crack hide."""

    PALETTE = {
        'D': QColor('#5C1A00'),   # dark red-brown body
        'L': QColor('#FF6600'),   # bright orange lava cracks
        'H': QColor('#F5E0C0'),   # pale horn
        'F': QColor('#2A1A00'),   # dark hoof
        'E': QColor('#FF4500'),   # ember eye
        'B': QColor('#111111'),   # black outline
    }

    # 32 rows x 32 characters each  (columns 0-31)
    # '.' = transparent
    # Side-profile heavy fire bull facing right. Wide upward horns, massive body,
    # thick four legs with dark hooves, glowing orange lava cracks across hide,
    # ember-orange eye, closed muzzle.
    #
    #   D = dark red-brown body    L = lava orange crack
    #   H = pale horn              F = dark hoof
    #   E = ember eye              B = black outline
    #   . = transparent
    GRID = [
        #          1111111111222222222233
        #0123456789012345678901234567890 1
        '................................',  # row  0
        '................................',  # row  1
        '.....BB.....BBB.................',  # row  2  horn tips
        '....BHHB....BHHB................',  # row  3  horns
        '....BHHB....BHHB................',  # row  4  horns
        '.....BHHBB.BHHB.................',  # row  5  horn convergence
        '......BBBBBBBB..................',  # row  6  horn bases / forehead
        '.....BDDDDDDDB..................',  # row  7  head top
        '....BDDDDDDDDDDB................',  # row  8  head
        '....BDDDELDDDDDB................',  # row  9  eye (E) + lava (L)
        '....BDDDDDDDDDB.................',  # row 10  lower head
        '....BDDDDDDDDDBB................',  # row 11  muzzle
        '.....BDDDDDDDDDB................',  # row 12  muzzle lower
        '..BBBDDDDDDDDDDDDBB.............',  # row 13  neck wide
        '.BDDDDDDDDDDDDDDDDDB............',  # row 14  upper body / chest
        '.BDDDDLDDDDDDDDDDLDB............',  # row 15  body + lava cracks
        'BDDDDDDDDDDDDDDDDDDDDB..........',  # row 16  body widest
        'BDDDDLDDDDDDDLDDDDDDDB..........',  # row 17  body + lava cracks
        '.BDDDDDDDDDDDDDDDDDDB...........',  # row 18  body lower
        '.BDDDLDDDDDDDDLDDDDB............',  # row 19  lower body + lava
        '..BDDDDDDDDDDDDDDDB.............',  # row 20  underbelly
        '...BBBBBDDDDDDBBBBB.............',  # row 21  leg tops
        '....BDDDB.BBDDDDB...............',  # row 22  upper legs front/back
        '....BDDDB..BDDDDB...............',  # row 23  legs mid
        '....BDDDB..BDDDDB...............',  # row 24  legs lower
        '....BDDDB..BDDDDB...............',  # row 25  legs lower 2
        '....BFFBB..BBFFBB...............',  # row 26  hooves top
        '....BFFB....BFFB................',  # row 27  hooves
        '.....BBB.....BBB................',  # row 28  hoof base
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
