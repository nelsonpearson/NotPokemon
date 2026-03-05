from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class PyrotoadSprite(SpriteRenderer):
    """Pixel art sprite for Pyrotoad -- a wide bulky fire toad with flaming wart bumps."""

    PALETTE = {
        'D': QColor('#4A3800'),   # dark olive body
        'W': QColor('#FF5500'),   # fiery orange wart spots
        'A': QColor('#F5DEB3'),   # pale cream belly
        'E': QColor('#CC6600'),   # amber eye
        'B': QColor('#111111'),   # dark outline
        'P': QColor('#000000'),   # pupil black
    }

    # 32 rows x 32 characters each  (columns 0-31)
    # '.' = transparent
    # Front-facing/side upright bulky fire toad sitting. Wide rounded body,
    # large bulging eyes, very wide mouth with lip line, fiery orange wart
    # bumps on back, pale cream belly, stubby legs splayed outward.
    #
    #   D = dark olive body    W = fiery orange wart
    #   A = pale cream belly   E = amber eye
    #   B = dark outline       P = pupil black
    #   . = transparent
    GRID = [
        #          1111111111222222222233
        #0123456789012345678901234567890 1
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '................................',  # row  3
        '......BBBBBBBBBBB...............',  # row  4  top of head / eye bumps
        '.....BDDDDDDDDDDDB..............',  # row  5  head top
        '....BWDDBDDDDDBDDWB.............',  # row  6  eye bump outer (W=socket)
        '....BEDBBDDDDDBBEDB.............',  # row  7  eyes (E=iris, P implied by E)
        '....BWDDBDDDDDBDDWB.............',  # row  8  eye bump lower
        '....BDDDDDDDDDDDDDB.............',  # row  9  head wide
        '....BDDDDDDDDDDDDDB.............',  # row 10  head lower
        '...BDDDDDDDDDDDDDDDB............',  # row 11  head widest
        '...BDDDDDDDDDDDDDDDB............',  # row 12  jaw / mouth area
        '...BDDBBBBBBBBBBBDDB............',  # row 13  mouth line (wide grin)
        '...BDDDDDDDDDDDDDDDB............',  # row 14  chin / upper body
        '..BDDWDDDDDDDDDDDWDDB...........',  # row 15  body + wart spots
        '..BDDDDDDDAAAAADDDDB............',  # row 16  body + belly
        '..BDDDDDDAAAAAADDDB.............',  # row 17  belly center
        '..BDDDWDDAAAAAADWDB.............',  # row 18  belly + warts
        '..BDDDDDDAAAAAADDDDB............',  # row 19  belly lower
        '..BDDDDDDDDDDDDDDDB.............',  # row 20  lower body
        '..BWDDDDDDDDDDDDDWB.............',  # row 21  lower body + warts
        '..BBBDDDDDDDDDDDBBB.............',  # row 22  leg attachment
        '.BB..BDDDDDDDDDB..BB............',  # row 23  front+back legs splayed
        '.BB...BDDDDDDB....BB............',  # row 24  legs
        '.BB....BDDDDB.....BB............',  # row 25  lower legs
        '..BB....BDDB.....BB.............',  # row 26  feet
        '...BBB..BBBB..BBBB..............',  # row 27  toes
        '...BBBB.........BBBB............',  # row 28  toe tips
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
