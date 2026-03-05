from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class TidalotterSprite(SpriteRenderer):
    """Pixel art sprite for Tidalotter -- a cute water otter sitting upright."""

    PALETTE = {
        'B': QColor('#1E90FF'),   # body blue
        'L': QColor('#87CEEB'),   # lighter belly / face highlight
        'D': QColor('#0A0A5C'),   # dark outline
        'W': QColor('#FFFFFF'),   # eye white
        'P': QColor('#000000'),   # pupil / whisker dots
        'N': QColor('#FFB6C1'),   # nose pink
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '...........DD........DD.........',  # row  3  ear tips
        '..........DBBD......DBBD........',  # row  4  ears
        '..........DBBD....DBBD..........',  # row  5  ears base
        '..........DBBDBBBBDBBD..........',  # row  6  top of head connecting ears
        '.........DBBBBBBBBBBBBD.........',  # row  7  head upper
        '........DBBBBBBBBBBBBBBD........',  # row  8  head widest
        '........DBBBLLLBBBBBBBBD........',  # row  9  face highlight near eye
        '........DBBWPBLBBBBNBBBD........',  # row 10  eye (W=white P=pupil) + nose
        '........DBBBLLBBBBBD..P.........',  # row 11  cheek + whisker right
        '.........DBBLLBBBBBD............',  # row 12  lower face
        '......P...DBBBBBBBBD............',  # row 13  chin + whisker left
        '...........DBBBBBBD.............',  # row 14  neck top
        '..........DBBBBBBBD.............',  # row 15  neck
        '.........DBBBBBBBBBD............',  # row 16  upper chest
        '........DBBBLLLLBBBD............',  # row 17  body with belly start
        '.......DBBBLLLLLLBBBD...........',  # row 18  body wider belly
        '.......DBBBLLLLLLBBBD...........',  # row 19  body widest
        '.......DBBBLLLLLLBBBD...........',  # row 20  body belly area
        '.......DBBBBLLLLBBBBD...........',  # row 21  belly narrowing
        '........DBBBBLLBBBBD............',  # row 22  body tapering
        '........DDBBBBBBBBDD............',  # row 23  body base
        '.......DD..DBBBBBD..............',  # row 24  tail start + hips
        '......DBBD.DBBDDBBD.............',  # row 25  tail + upper legs
        '.....DBBBD..DBD.DBD.............',  # row 26  tail wider + legs
        '....DBBBBD..DBD.DBD.............',  # row 27  flat tail + legs
        '....DLLLLD..DBD.DBD.............',  # row 28  tail paddle (light) + feet
        '....DDDDDD..DDD.DDD.............',  # row 29  tail tip + paw pads
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
