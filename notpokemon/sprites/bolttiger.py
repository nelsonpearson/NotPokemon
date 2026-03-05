from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class BolttigerSprite(SpriteRenderer):
    """Pixel art sprite for Bolttiger -- a powerful electric tiger with lightning-bolt stripe patterns."""

    PALETTE = {
        'Y': QColor('#FFB300'),   # golden yellow body
        'K': QColor('#111111'),   # black lightning stripes / outline
        'C': QColor('#FFF8DC'),   # cream belly
        'E': QColor('#FFD700'),   # bright yellow eye
        'W': QColor('#FFFFFF'),   # white whisker pixels
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #0         1         2         3
        #01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '.............KKK................',  # row  3  ear top
        '............KYYYK...............',  # row  4  ear
        '...........KYYKYK...............',  # row  5  ear interior
        '...........KYYYYK...............',  # row  6  ear base
        '..........KKYYYYYKKK............',  # row  7  top skull
        '.........KKYYYYYYYKYK...........',  # row  8  forehead
        '........KYYYYKYYYYYYYYYK........',  # row  9  face top + stripe
        '.......KYYYYKEYKKYYYYYK.........',  # row 10  eye row
        '.......KYYYKKKKKYYYYYYK.........',  # row 11  nose bridge
        '.......KYYYCCCKYYYYYYK..........',  # row 12  cream cheek / muzzle
        '......KKWCCCKCCKYYYYK...........',  # row 13  whiskers + chin
        '......KYYCCCCCKYYYYK............',  # row 14  jaw
        '.......KKYYYKYYYYYYK............',  # row 15  neck + stripe
        '.......KYYYYYYYYYYYYK...........',  # row 16  neck
        '......KYYKYYYYYYYYKYYYK.........',  # row 17  shoulder + bolt stripe
        '.....KYYYYYKYYYKYYKYYYYK........',  # row 18  body stripe zigzag
        '....KYYYYYYKYKKYYCCYYYYYK.......',  # row 19  body + cream belly
        '....KYYYYYKKYYKYCCCYYYYYYK......',  # row 20  body + belly wide
        '....KYYYKYYYKYYCCCYYYYYYYK......',  # row 21  belly wide
        '....KYYKYYYYYYYCCCYYYYYYKK......',  # row 22  lower body
        '.....KYYKYYYYYYCKYYYYYYK........',  # row 23  hips
        '.....KYYYYYYYYYKYYYYYK..........',  # row 24  rump + tail base
        '......KYYYKK..KYYYK..KYYYYKK....',  # row 25  legs + tail -- MUST BE 32
        '......KYYK....KYYK....KYYYK.....',  # row 26  mid legs + tail
        '......KYKK....KYKK....KYYKK.....',  # row 27  lower legs
        '......KKK.....KKK.....KKKK......',  # row 28  paws
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
