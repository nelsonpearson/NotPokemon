from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class TidesharkSprite(SpriteRenderer):
    """Pixel art sprite for Tideshark -- a sleek torpedo-shaped shark in side profile."""

    PALETTE = {
        'S': QColor('#2E86C1'),   # steel blue-gray body
        'W': QColor('#EBF5FB'),   # white belly
        'F': QColor('#1A5276'),   # dark blue-gray fins
        'P': QColor('#111111'),   # black eye
        'E': QColor('#FFFFFF'),   # eye white dot
        'D': QColor('#0A2540'),   # dark outline
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '..............DDD...............',  # row  3  dorsal fin tip
        '.............DFFDD..............',  # row  4  dorsal fin upper
        '............DFFFDD..............',  # row  5  dorsal fin
        '...........DFFFFD...............',  # row  6  dorsal fin base
        '..........DSSSSSSSSSSDD.........',  # row  7  body top
        '.........DSSSSSSSSSSSSSDD.......',  # row  8  body upper / snout start
        '........DSSSSSSSSSSSSSSSSDD.....',  # row  9  body widening
        '.......DSSPSSSSSSSSSSSSSSSSDD...',  # row 10  eye row (P=pupil)
        '......DSSEWSSSSSSSSSSSSSSSSSSDD.',  # row 11  eye white dot (E=white)
        '.....DSSSSSSSSSSSSSSSSSSSSSSSSD.',  # row 12  body widest / snout tip
        '.....DWWWWWWWWWWWWWWSSSSSSSSSSD.',  # row 13  belly starts white
        '......DWWWWWWWWWWWWWSSSSSSSSDD..',  # row 14  belly
        '.......DWWWWWWWWWWWSSSSSSSSSDD..',  # row 15  belly narrowing
        '........DWWWWWWWWWSSSSSSSSDD....',  # row 16  belly further
        '.........DWWWWWWWSSSSSSSSDD.....',  # row 17  belly lower
        '..........DWWWWWSSSSSSSSDD......',  # row 18  lower body
        '..........DFFFFFFSSSSSSDD.......',  # row 19  pectoral fin
        '..........DFFFFFFSSSSDD.........',  # row 20  pectoral fin lower
        '...........DFFFFSSSDD...........',  # row 21  pectoral fin base
        '............DSSSSSSDD...........',  # row 22  lower body tapering
        '.............DSSSSDD............',  # row 23  body narrowing
        '..............DSSDD....DDD......',  # row 24  tail base + tail upper fin
        '...............DDD....DFFDD.....',  # row 25  tail connection + tail upper
        '..............DDD.....DFFFD.....',  # row 26  tail lower + tail fin
        '.............DFDD......DFFD.....',  # row 27  tail lower fin
        '............DFFDD......DFDD.....',  # row 28  tail flukes
        '............DDDD........DDD.....',  # row 29  tail tip
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
