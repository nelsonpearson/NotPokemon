from PySide6.QtGui import QColor, QPainter

from notpokemon.sprites.base import SpriteRenderer


class GlacifoxSprite(SpriteRenderer):
    """Sprite for Glacifox -- a crystalline arctic fox sitting elegantly."""

    PALETTE = {
        'O': QColor('#2F4F4F'),   # dark outline
        'B': QColor('#B0E0E6'),   # powder blue body
        'L': QColor('#E0FFFF'),   # light cyan belly / highlights
        'S': QColor('#4682B4'),   # steel blue markings
        'W': QColor('#FFFFFF'),   # white (tail tip, eye white)
        'P': QColor('#000000'),   # pupil black
    }

    # 32x32 pixel grid -- '.' is transparent
    # Front-facing sitting arctic fox with ice-crystal forehead markings
    # and a large fluffy white-tipped tail curving around the left side.
    #
    # Palette key:
    #   O = dark outline    B = powder blue body    L = light cyan highlight
    #   S = steel blue mark W = white (eye/tail)    P = pupil
    #   . = transparent
    GRID = [
        # 0         1         2         3
        # 01234567890123456789012345678901
        '................................',  # row  0
        '........O.............O.........',  # row  1  ear tips
        '.......OSO...........OSO........',  # row  2  ears inner steel blue
        '......OBSBO.........OBSBO.......',  # row  3  ears
        '......OBSBO.........OBSBO.......',  # row  4  ears
        '.....OBBSBBO.......OBBSBBO......',  # row  5  ears wider
        '....OOBBBBOOOOOOOOOOBBBBBOO.....',  # row  6  ears connect to head
        '.....OBBBBBBBBBBBBBBBBBBBO......',  # row  7  head top
        '....OBBBBBBBBBBBBBBBBBBBBBBO....',  # row  8  head widest
        '....OBBBBBBBLSLBBBBBBBBBBBO.....',  # row  9  crystal marking top
        '....OBBBBBSLWLSBBBBBBBBBBBO.....',  # row 10  crystal diamond center
        '....OBBBBBBBLSBBBBBBBBBBBBO.....',  # row 11  crystal marking bottom
        '....OBWPBBBBBBBBBBBBBWPBBBO.....',  # row 12  eyes (W=white P=pupil)
        '....OBBBBBBBBBBBBBBBBBBBBBO.....',  # row 13  face
        '.....OBBBBBBBBBSBBBBBBBBO.......',  # row 14  nose (steel blue)
        '.....OBBBBBBBBBBBBBBBBBBO.......',  # row 15  lower face
        '......OBBBBBLLLLLBBBBBBO........',  # row 16  muzzle highlight
        '.......OOBBBBBBBBBBBOO..........',  # row 17  jaw narrows
        '........OBBBBBBBBBBBO...........',  # row 18  neck
        '.......OBBBBBBBBBBBBBBO.........',  # row 19  upper chest
        '......OBBBBBLLLLLLLBBBBBO.......',  # row 20  body with belly
        '.....OBBBBLLLLLLLLLLLBBBBBO.....',  # row 21  body wider belly
        '.....OBBBBLLLLLLLLLLBBBBBBO.....',  # row 22  body widest
        '.....OBBBBBLLLLLLLLBBBBBBBO.....',  # row 23  belly narrowing
        '......OOBBBBBBLLLBBBBBBOO.......',  # row 24  lower body
        '...OWWOOBBBBBBBBBBBBBOOBBBO.....',  # row 25  tail start + hips
        '..OWWWWOBBBBBBBBBBBBBOOBBBBO....',  # row 26  fluffy tail + legs
        '.OWWWWWWOBBOOO...OOOBBBBBBO.....',  # row 27  tail wider + legs
        '.OWWWWWWOO..........OBBBBBO.....',  # row 28  tail tip white + feet
        '..OOWWWOO..........OBBBBBBO.....',  # row 29  tail base + paws
        '...OOOOO...........OOOOOOOO.....',  # row 30  ground line
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
