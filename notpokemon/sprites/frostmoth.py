from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class FrostmothSprite(SpriteRenderer):
    """Pixel art sprite for Frostmoth -- an elegant ice moth with crystalline frost-patterned wings."""

    PALETTE = {
        'W': QColor('#E8F8FF'),   # ice white wings
        'B': QColor('#AED6F1'),   # pale blue frost patterns
        'S': QColor('#BDC3C7'),   # silver-gray body
        'A': QColor('#555555'),   # dark gray antennae
        'K': QColor('#111111'),   # black eye dots / outline
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #0         1         2         3
        #01234567890123456789012345678901
        '................................',  # row  0
        '...A.................A..........',  # row  1  antenna tips
        '....A...............A...........',  # row  2  antennae
        '.....A.....SSS.....A............',  # row  3  antennae + head top
        '.....AA...SKKS...AA.............',  # row  4  antennae + eyes
        '......AA..SSSS..AA..............',  # row  5  antennae merge head
        'WWWW...AASSSSSAA...WWWW.........',  # row  6  upper wing start
        'WBWWW..ASSSSSSSA..WWWBW.........',  # row  7  upper wing frost
        'WWBWWW.ASSSSSSSSA.WWWBWW........',  # row  8  upper wing frost
        'WBBWWWWSSSSSSSSSSWWWWBBW........',  # row  9  upper wing mid
        'WWBWWWWSSSSSSSSSSWWWWBWW........',  # row 10  upper wing mid
        'BWWBWWWWSSSSSSSSSWWWWBWWB.......',  # row 11  upper wing wide
        'WWWWWWWWWSSSSSSSSWWWWWWWW.......',  # row 12  widest upper wing
        'BWWWWWWWWSSSSSSSWWWWWWWWB.......',  # row 13  upper wing taper
        '.WWWBWWWWSSSSSSSWWWWBWWW........',  # row 14  upper wing taper
        '..WWWWWWWSSSSSSSWWWWWWWW........',  # row 15  upper/lower wing divide
        '..WWWWWWWSSSSSSSWWWWWWWW........',  # row 16  lower wing top
        '...BWWWWWSSSSSSSWWWWWB..........',  # row 17  lower wing
        '...WWWWWWSSSSSSSWWWWWW..........',  # row 18  lower wing
        '....BWWWWSSSSSSSSWWWB...........',  # row 19  lower wing frost
        '....WWWWWWSSSSSSWWWWW...........',  # row 20  lower wing
        '.....WWWWWWSSSSSWWWWW...........',  # row 21  lower wing narrow
        '.....BWWWWWSSSSWWWWB............',  # row 22  lower wing narrow
        '......WWWWWWSSWWWWWW............',  # row 23  wing tip area
        '......BWWWWWWWWWWB..............',  # row 24  wing tips
        '.......WWWWWWWWWW...............',  # row 25  wing tips
        '........WWWWWWWW................',  # row 26  lower wing tip
        '.........BWWWWB.................',  # row 27  lowest tips
        '................................',  # row 28
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
