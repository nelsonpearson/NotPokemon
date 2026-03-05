from PySide6.QtGui import QColor, QPainter

from notpokemon.sprites.base import SpriteRenderer


class MossboarSprite(SpriteRenderer):
    """Sprite for Mossboar – a stocky nature boar with mossy green patches."""

    PALETTE = {
        'O': QColor('#111111'),   # dark outline
        'B': QColor('#4A2800'),   # dark brown body
        'M': QColor('#2D6A10'),   # moss green patches
        'T': QColor('#E8D5A3'),   # tan tusk
        'N': QColor('#1A0E00'),   # dark bristle mane
        'E': QColor('#CC7700'),   # amber eye
        'L': QColor('#3D2000'),   # darker brown leg shadow
    }

    # 32x32 pixel grid — '.' is transparent
    # Stocky boar facing right in side profile with mossy green patches,
    # prominent tusks, and bristly mane along spine.
    #
    # Palette key:
    #   O = outline (#111111)    B = dark brown body (#4A2800)
    #   M = moss green (#2D6A10) T = tan tusk (#E8D5A3)
    #   N = dark mane (#1A0E00)  E = amber eye (#CC7700)
    #   L = leg shadow (#3D2000) . = transparent
    GRID = [
        # 0         1         2         3
        # 01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '.........OOOO...................',  # row  3  ear tips
        '........OBBBO...................',  # row  4  ear
        '........OBBBO....ONNNNNNNO......',  # row  5  ear + mane start
        '.......OOBBBOO..ONNNNNNNNO......',  # row  6  head top + mane
        '.......OBBBBBO.ONNNNNNNNNO......',  # row  7
        '......OBBBBBBBONNNNNNNNNNNO.....',  # row  8  head merges body
        '......OBBEBBBBOMNNNNNNNNNNO.....',  # row  9  eye + mane
        '......OBBBBBBBOMMMNNNNNNNO......',  # row 10
        '.......OBBBBBBOMMMNNNNNNO.......',  # row 11  snout area
        '.......OBBBBBBBOMMMMMNNNO.......',  # row 12
        '......OBBBBBBBBOMMMMMNO.........',  # row 13  tusk level
        '.....TTOBBBBBBBBOMMMNO..........',  # row 14  tusk start
        '....TTTOOOBBBBBBOMMNO...........',  # row 15  tusk ext
        '....TTOOOOBBBBBBBBBOO...........',  # row 16  snout/tusk
        '.....OOOOBBBBBBBBBBBOO..........',  # row 17
        '......OOBBBBBBBBBBBBBOO.........',  # row 18  body middle
        '.....OBBBBBBBBBBBBBBBBBO........',  # row 19
        '.....OBBBBBMMMBBBBBBBBBO........',  # row 20  moss patch
        '.....OBBBMMMMMMBBBBBBBBO........',  # row 21
        '.....OBBMMMMMMMMBBBBBBO.........',  # row 22
        '.....OBBBMMMMMMBBBBBBO..........',  # row 23
        '.....OBBBBMMMBBBBBBOO...........',  # row 24
        '....OBBBBBBBBBBBBOO.............',  # row 25  belly
        '....OBBOOO....OOOBBO............',  # row 26  leg separation
        '....OBBO........OBBO............',  # row 27  upper legs
        '....OLBO........OLBO............',  # row 28  leg shadow
        '....OLLBO......OLLBO............',  # row 29
        '....OOOOO......OOOOO............',  # row 30  hooves
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
