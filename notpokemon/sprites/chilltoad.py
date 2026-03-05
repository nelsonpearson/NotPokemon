from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class ChilltoadSprite(SpriteRenderer):
    """Pixel art sprite for Chilltoad -- a wide bulky ice toad with ice crystal growths on its back."""

    PALETTE = {
        'T': QColor('#AED6F1'),   # pale ice blue body
        'B': QColor('#5DADE2'),   # darker blue-gray back / ice crystals
        'W': QColor('#FFFFFF'),   # white crystal tips
        'C': QColor('#EBF5FB'),   # cream belly
        'K': QColor('#1A5276'),   # dark outline
        'E': QColor('#111111'),   # small dark eye
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #0         1         2         3
        #01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '.............WW...WW............',  # row  3  crystal tips
        '............WBBW.WBBW...........',  # row  4  crystal tops
        '...........WBBBWWBBBW...........',  # row  5  crystals
        '..........WBBBBBBBBBBW..........',  # row  6  crystal base row
        '........KKBBBBBBBBBBBBKK........',  # row  7  back top + crystals
        '.......KTTBBBBBBBBBBBBTTK.......',  # row  8  back / body top
        '......KTTTBBBBBBBBBBBTTTK.......',  # row  9  body
        '.....KTTTTTBBBBBBBBBTTTTTK......',  # row 10  body wide
        '....KTTTTTTBBBBBBBBTTTTTTK......',  # row 11  widest back
        '....KTTTTTTTBBBBBTTTTTTTTTK.....',  # row 12  body
        '....KTTTTTTTBBBBBTTTTTTTTTKK....',  # row 13  belly starts
        '....KTTTTTTCCCCCCTTTTTTTTK......',  # row 14  cream belly
        '....KTTTTTCCCCCCCCTTTTTTTK......',  # row 15  belly
        '....KTTTTCCCCCCCCCCTTTTTTK......',  # row 16  belly wide
        '...KTTTTCCCCCCCCCCCTTTTTTKK.....',  # row 17  belly wide
        '...KTTTCCCCCCCCCCCCCTTTTTTK.....',  # row 18  belly
        '...KTTCCCCCCCCCCCCCCTTTTTTKK....',  # row 19  lower belly
        '...KTTTCCCCCCCCCCCCCCTTTTTK.....',  # row 20  lower belly
        '...KKKKTTTCCCCCCCCTTTTKKKKK.....',  # row 21  bottom body + legs top
        '..KTTK.KTTCCCCCCTTTK.KTTK.......',  # row 22  legs
        '..KTTK.KTTTTTTTTTTK..KTTK.......',  # row 23  legs mid
        '.KTTTK.KTTTTTTTTTK...KTTTK......',  # row 24  front/rear feet
        '.KKKKKKKKKKKKKKKKKKKKKKKKKK.....',  # row 25  toe webbing
        '................................',  # row 26
        '................................',  # row 27
        '................................',  # row 28
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
