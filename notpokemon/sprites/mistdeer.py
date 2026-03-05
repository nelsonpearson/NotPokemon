from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class MistdeerSprite(SpriteRenderer):
    """Pixel art sprite for Mistdeer -- an elegant deer with ice-crystal antlers."""

    PALETTE = {
        'M': QColor('#AED6F1'),   # pale blue-white body
        'S': QColor('#85C1E9'),   # light gray-blue shading
        'A': QColor('#1A8FBF'),   # crystal antler blue
        'D': QColor('#2C3E50'),   # dark hoof/nose/outline
        'E': QColor('#555555'),   # soft eye
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #01234567890123456789012345678901
        '................................',  # row  0
        '......A......A..................',  # row  1  antler outermost tips
        '.....A.A....A.A.................',  # row  2  antler branch tips
        '.....A.A....A.A.................',  # row  3  antler branches
        '......A......A..................',  # row  4  antler branch join
        '.....AAA....AAA.................',  # row  5  antler lower branch
        '......A......A..................',  # row  6  antler stem
        '.......AAAAAA...................',  # row  7  antler base connecting
        '........DMMMD...................',  # row  8  head top
        '.......DMMMMD...................',  # row  9  head upper
        '.......DMMSMD...................',  # row 10  head with shading + ear
        '.......DMMEMED..................',  # row 11  eye row (E=eye)
        '........DMMMD......D............',  # row 12  lower face + ear tip
        '.........DMMDD..................',  # row 13  muzzle
        '.........DMMD...................',  # row 14  chin / nose area
        '..........DDD...................',  # row 15  nose (using D)
        '........DMMMMMD.................',  # row 16  neck upper
        '.......DMMMMMMMD................',  # row 17  neck lower / body upper start
        '......DSSMMMMMMMD...............',  # row 18  body upper with shading
        '.....DSSMMMMMMMMMD..............',  # row 19  body main
        '.....DSSMMMMMMMMSSD.............',  # row 20  body widest
        '.....DSSMMMMMMMSSSSD............',  # row 21  body with shading
        '......DSSMMMMMMSSSD.............',  # row 22  body lower
        '.......DSSMMMMSSD...............',  # row 23  body tapering
        '........DMMMMMD.................',  # row 24  rump
        '........DMMD.DMMD...............',  # row 25  upper legs
        '.........DMD..DMD...............',  # row 26  legs
        '.........DMD..DMD...............',  # row 27  legs mid
        '.........DSD..DSD...............',  # row 28  lower legs shading
        '.........DDD..DDD...............',  # row 29  hooves
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
