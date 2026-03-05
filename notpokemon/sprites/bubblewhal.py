from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class BubblewhalSprite(SpriteRenderer):
    """Pixel art sprite for Bubblewhal -- a huge, friendly water whale."""

    PALETTE = {
        'B': QColor('#1A5276'),   # deep ocean blue body
        'L': QColor('#5DADE2'),   # lighter belly
        'W': QColor('#FFFFFF'),   # white (bubbles, eye white)
        'D': QColor('#0A2540'),   # dark blue outline
        'P': QColor('#111111'),   # dark pupil
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '.............W..................',  # row  2  bubble
        '..............W..WWW............',  # row  3  bubbles near blowhole
        '.............W.WW..W............',  # row  4  blowhole spray
        '...........DDDDD................',  # row  5  blowhole top
        '..........DBBBBBD...............',  # row  6  blowhole base / top of head
        '.........DBBBBBBBDD.............',  # row  7  head upper
        '........DBBBBBBBBBBDD...........',  # row  8  head widening
        '.......DBBBBBBBBBBBBBDD.........',  # row  9  upper body
        '......DBBBBBBBBBBBBBBBBDD.......',  # row 10  body top
        '.....DBBBBBBBBBBBBBBBBBBBDD.....',  # row 11  body widening
        '....DBBBBBBBBBBBBBBBBBBBBBBDD...',  # row 12  body wider
        '....DBBBWPBBBBBBBBBBBBBBBBBBD...',  # row 13  eye row (W=white P=pupil)
        '....DBBBBBBBBBBBBBBBBBBBBBBBD...',  # row 14  body
        '....DBBBBBBBBBBBBBBBBBBBBBBBD...',  # row 15  body widest
        '....DBBBBBBBBBBBBBBBBBBBBBBBDD..',  # row 16  body full
        '....DBBBBLLLLLLLLLLLLLLBBBBBD...',  # row 17  belly start
        '....DBBBBLLLLLLLLLLLLLLBBBBBD...',  # row 18  belly
        '.....DBBBBLLLLLLLLLLLLBBBBBD....',  # row 19  belly middle
        '.....DBBBBLLLLLLLLLLLLBBBBBD....',  # row 20  belly middle
        '......DBBBBBLLLLLLLLBBBBBBDD....',  # row 21  belly narrowing
        '.......DBBBBBBBBBBBBBBBBBBDD....',  # row 22  lower body
        '........DBBBBBBBBBBBBBBBBDD.....',  # row 23  lower body
        '.........DBBBBBBBBBBBBBBBD......',  # row 24  body narrowing
        '.....DD...DBBBBBBBBBBBBBD.......',  # row 25  pectoral fin + body
        '....DBBD...DBBBBBBBBBBBBD.......',  # row 26  fin wider
        '....DBBBD...DBBBBBBBBBBBD.......',  # row 27  fin + tail base
        '.....DDDD....DDDDBBBDDDD........',  # row 28  fin base + tail flukes
        '..........DDDD....DDDD..........',  # row 29  tail fluke tips
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
