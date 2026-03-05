from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class StonecrabSprite(SpriteRenderer):
    """Pixel art sprite for Stonecrab -- a wide heavily-armored earth crab with stone-like shell texture and large claws."""

    PALETTE = {
        'G': QColor('#7F8C8D'),   # stone gray body
        'R': QColor('#555555'),   # darker rock texture lines
        'C': QColor('#6D4C41'),   # brown-gray claw
        'S': QColor('#D5D8DC'),   # sand highlight
        'E': QColor('#111111'),   # dark eye dots / outline
        'K': QColor('#2C3E50'),   # dark outline / shadow
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
        '..KKCCCK..............KCCCK.....',  # row  4  claw tops
        '.KCCCCCCK............KCCCCCK....',  # row  5  claws open
        '.KCCSCCCCK..........KCCCSCCK....',  # row  6  claw highlight
        '.KCCCCCCCK..........KCCCCCCCK...',  # row  7  claw mid
        '..KCCCCCCK.........KCCCCCCCK....',  # row  8  claw lower
        '...KCCCCCKKKKKKKKKKCCCCCCK......',  # row  9  claws meet body
        '...KCCCCCGGGGGGGGGGCCCCCK.......',  # row 10  claw-body join
        '...KCCKKGGSSGSSGSSGKKCCK........',  # row 11  claw base + shell top
        '....KKKGGGSSGSSGSSGGGGKK........',  # row 12  shell top
        '....KGGGGGSSGSSGSSGGGGGK........',  # row 13  shell
        '....KGGRRGGSSGSSGSSGRRGGK.......',  # row 14  rock texture
        '....KGGRRGGSSGSSGSSGGRRGGK......',  # row 15  body wide + texture
        '....KGGRRGGSSGSSGSSGRRGGK.......',  # row 16  body
        '....KGGRRGGSSGSSGSSGGRRGGK......',  # row 17  wide body
        '....KGGRRGGSSGSSGSSGRRGGK.......',  # row 18  lower body
        '.....KGGGGGSSGSSGSSGGGGK........',  # row 19  belly plate
        '.....KGGGGGGGGGGGGGGGGGK........',  # row 20  underside
        '.....KKKKKKKKKKKKKKKKKKK........',  # row 21  body base edge
        '....KGGK.KGGK.KGGK.KGGK.KGGK....',  # row 22  leg tops (5 legs)
        '....KGGK.KGGK.KGGK.KGGK.KGGK....',  # row 23  legs mid
        '....KRGK.KRGK.KRGK.KRGK.KRGK....',  # row 24  lower legs texture
        '.....KKK..KKK..KKK..KKK..KKK....',  # row 25  leg tips
        '................................',  # row 26
        '................................',  # row 27
        '................................',  # row 28
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
