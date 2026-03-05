from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class VoltlynxSprite(SpriteRenderer):
    """Pixel art sprite for Voltlynx -- a sleek electric lynx stalking its prey."""

    PALETTE = {
        'Y': QColor('#FFD700'),   # yellow lightning markings, ear tufts, tail tip
        'D': QColor('#2C2C2C'),   # dark body
        'G': QColor('#4A4A4A'),   # lighter gray fur
        'W': QColor('#FFFFFF'),   # eye white
        'B': QColor('#000000'),   # pupil / outline
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #0         1         2         3
        #01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '................................',  # row  3
        '.........Y.........Y............',  # row  4  ear tuft tips
        '........YBB.......YBB...........',  # row  5  ear tufts
        '.......BDDBB.....BDDBB..........',  # row  6  upper ears
        '.......BDDDB.....BDDDB..........',  # row  7  ears
        '........BDDDBBBBBDDDB...........',  # row  8  top of skull
        '........BDDDDDDDDDDDBB..........',  # row  9  forehead
        '........BWBDDDDDDDDDDB..........',  # row 10  eye (W=sclera, B=pupil)
        '........BDDDDDDDDDDDDBB.........',  # row 11  cheek
        '.........BDDDDDDDDDDBBBB........',  # row 12  snout + nose
        '.........BBDDDDDDDDDB...........',  # row 13  chin / jaw
        '..........BBDDDDDDB.............',  # row 14  neck narrows
        '...........BDDDDDB..............',  # row 15  neck
        '..........BDDDDDDDB.............',  # row 16  shoulders widen
        '.........BDDYDDDDDDDDB..........',  # row 17  body + bolt start
        '........BDDDDYDDDDDDDDDB........',  # row 18  body + bolt
        '.......BDDDDYYDDGGGGDDDDB.......',  # row 19  bolt zigzag + gray belly
        '.......BDDDDDYYGGGGGDDDDB.......',  # row 20  bolt + belly
        '......BDDDDDDDYYGGGDDDDDDDB.....',  # row 21  widest body + bolt
        '......BDDDDDDDDYYDDDDDDDDDB.....',  # row 22  lower body + bolt end
        '.......BDDDDDDDDYDDDDDDDDBY.....',  # row 23  hips taper + tail start
        '.......BDDDDDDDDDDDDDDDDBBYY....',  # row 24  tail curves up
        '........BDDB.BDDB..BDDDB..YY....',  # row 25  front/hind legs + tail
        '........BDB..BDB...BDDB.........',  # row 26  mid legs
        '........BDB..BDB...BBB..........',  # row 27  lower legs
        '........BBB..BBB................',  # row 28  paws
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
