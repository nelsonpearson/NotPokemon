from PySide6.QtGui import QColor, QPainter

from notpokemon.sprites.base import SpriteRenderer


class LeafwingSprite(SpriteRenderer):
    """Sprite for Leafwing – a large butterfly with leaf-shaped wings facing viewer."""

    PALETTE = {
        'G': QColor('#27AE60'),   # bright leaf green wings
        'V': QColor('#1A6B3A'),   # darker vein lines
        'Y': QColor('#F1C40F'),   # golden wing edge trim
        'B': QColor('#7D6608'),   # small brown body
        'O': QColor('#111111'),   # black eye/outline
    }

    # 32x32 pixel grid — '.' is transparent
    # Large butterfly facing viewer with leaf-shaped wings spread open.
    # Symmetrical design with leaf vein patterns on wings.
    #
    # Palette key:
    #   G = leaf green (#27AE60)  V = dark vein (#1A6B3A)
    #   Y = gold trim (#F1C40F)   B = brown body (#7D6608)
    #   O = black outline (#111111) . = transparent
    GRID = [
        # 0         1         2         3
        # 01234567890123456789012345678901
        '................................',  # row  0
        '....YYY..................YYY....',  # row  1  upper wing tips
        '...YGGGY...............YGGGY....',  # row  2
        '..YGGGVGY.............YGGGVGY...',  # row  3  vein starts
        '..YGGVVGGY...........YGGVVGGY...',  # row  4
        '.YGGGVVGGGY.........YGGGVVGGGY..',  # row  5
        '.YGGGGVGGGGY.......YGGGGVGGGGY..',  # row  6
        '.YGGGGVGGGGYO.....OYGGGGVGGGGY..',  # row  7  body begins
        '.YGGGGGVGGGGOBBBBBOGGGGVGGGGGY..',  # row  8
        '.YGGGGGGVGGGOBBBBBOGGGGVGGGGY...',  # row  9
        '.YGGGGGGVGGGOBBBBBOGGGGVGGGY....',  # row 10  upper body
        '..YGGGGGVGGYOBBBBBOYGGGVGGGGY...',  # row 11
        '..YGGGGGVGGYOBBBBBOYGGGVGGGY....',  # row 12
        '...YGGVVGGYOBBBBBBOYGGVVGGY.....',  # row 13  widest point
        '...YGGVGGYOBBBBBBBOYGVGGGY......',  # row 14
        '....YVGGYOBBBBBBBOYVGGY.........',  # row 15  lower wing top
        '....YGGYOBBBBBBBOYGGY...........',  # row 16
        '...YGGGY.OBBBBBBOY.YGGY.........',  # row 17
        '..YGGGVY..OBBBBBOY..YVGGY.......',  # row 18
        '..YGGVGY...OBBBBOY...YGVGY......',  # row 19
        '.YGGGVGGY...OBBBOY...YGGVGY.....',  # row 20  lower wings
        '.YGGGGVGGY...OOO....YGGGGVY.....',  # row 21
        '.YGGGGVGGGY.......YGGGGVGGY.....',  # row 22
        '..YGGGVGGGY.......YGGVGGGY......',  # row 23
        '..YGGVVGGGY.......YGGVVGGY......',  # row 24
        '...YGVVGGY.........YGVVGY.......',  # row 25  lower wing tips
        '....YVVGY...........YVVGY.......',  # row 26
        '.....YVY.............YVY........',  # row 27
        '.....YY...............YY........',  # row 28
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
