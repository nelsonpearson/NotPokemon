from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class MudbisonSprite(SpriteRenderer):
    """Pixel art sprite for Mudbison -- an enormous hulking earth bison with a massive front hump and shaggy fur."""

    PALETTE = {
        'D': QColor('#4A3728'),   # dark muddy brown body
        'F': QColor('#8B6914'),   # tan-brown shaggy fur
        'U': QColor('#2C1A0E'),   # dark mud patches / deep shadow
        'H': QColor('#D4C5A9'),   # pale horn
        'V': QColor('#1A0E00'),   # dark hoof / outline
        'E': QColor('#CC7700'),   # amber eye
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #0         1         2         3
        #01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '.......HH.......................',  # row  3  horn tip
        '.......HHH......................',  # row  4  horn
        '......VHHHV.....................',  # row  5  horn base
        '......VFFFV.....................',  # row  6  shaggy forehead fur
        '.....VFFFDDV....................',  # row  7  head top
        '....VFFDDEVDV...................',  # row  8  eye row (E=amber eye)
        '....VFFDDDDDDV..................',  # row  9  face
        '....VFDDDDDDDUV.................',  # row 10  snout + dark shadow
        '....VFDDUUDDDUV.................',  # row 11  muzzle mud
        '.....VFDUUUDDV..................',  # row 12  lower snout
        '......VVFFFVV...................',  # row 13  chin fur / neck
        '.....VFFFDDDDV..................',  # row 14  neck
        '....VFFFFDDDDDDV................',  # row 15  neck + hump starts
        '...VFFFFFDDDDDDDDV..............',  # row 16  front hump rise
        '..VFFFFFFDDDDDDDDDDV............',  # row 17  hump peak
        '..VFFFFFFFDDDDDDDDDDDV..........',  # row 18  hump + body
        '..VFFFFFUDDDDDDDDDDDDDDV........',  # row 19  body + dark mud patch
        '..VFFFUUDDDDDDDDDDDDDDDV........',  # row 20  belly area
        '..VFFUUDDDDDDDDDDDDDDDDV........',  # row 21  lower body
        '..VFFUDDDDDDDDDDDDDDDDVV........',  # row 22  lower body
        '..VFFUDDDDDDDDDDDDDDDV..........',  # row 23  rump
        '..VFFFDDDDDDDDDDDDDDV...........',  # row 24  hind rump
        '..VFFV.VFDDDDDDV.VFFV.VFFV......',  # row 25  shaggy leg tops
        '..VDDV.VDDDDDDV..VDDV.VDDV......',  # row 26  legs
        '..VDDV.VDDDDDDV..VDDV.VDDV......',  # row 27  lower legs
        '..VVVV.VVVVVVV...VVVV.VVVV......',  # row 28  hooves
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
