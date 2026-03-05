from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class EmberaptorSprite(SpriteRenderer):
    """Pixel art sprite for Emberaptor -- a fierce but cute fire raptor dinosaur."""

    PALETTE = {
        'O': QColor('#FF4500'),   # orange-red body
        'L': QColor('#FF6347'),   # lighter belly / underside
        'G': QColor('#FFD700'),   # golden crest / eye accent
        'D': QColor('#CC3300'),   # darker outline / shadow
        'W': QColor('#FFFFFF'),   # eye white
        'B': QColor('#000000'),   # pupil / hard outline
        'R': QColor('#E03000'),   # deep red tail tip
        'T': QColor('#FF8C00'),   # mid-orange tail transition
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '..............GG................',  # row  3  crest tip
        '.............GOG................',  # row  4  crest
        '............GOGG................',  # row  5  crest base
        '...........DOOOOD...............',  # row  6  top of head
        '..........DOOOOOOB..............',  # row  7  head upper
        '..........DOOWBOOOD.............',  # row  8  eye row (W=white, B=pupil)
        '..........DOOOOOOOBB............',  # row  9  head lower + beak start
        '...........DOOOOO.BBB...........',  # row 10  jaw + beak tip
        '...........DDOOOOD..............',  # row 11  neck top
        '............DOOOOD..............',  # row 12  neck
        '...........DOOOOODD.............',  # row 13  neck to body
        '..........DOOOOOOOD.............',  # row 14  upper body
        '.........DOOOOLOOOD.............',  # row 15  body with belly
        '........DOOOLLLLOODD............',  # row 16  body wider
        '........DOOOLLLLOOOD............',  # row 17  body widest
        '.......DDOOOLLLLOOOD............',  # row 18  body + arm area
        '.......DOOOOLLLLOOODB...........',  # row 19  body + forearm
        '......DDOOOOLLLOOOD.BB..........',  # row 20  body + claw
        '......DTOOOOLLLOOOD.............',  # row 21  tail start + body
        '.....DTTOOOOOLLOOOD.............',  # row 22  tail + lower body
        '....DRTTOOOOOOOOOD..............',  # row 23  tail + body taper
        '...DRRTTOOOOOOOOD...............',  # row 24  tail mid
        '..DRRRTTDOOOOOOD................',  # row 25  tail + hips
        '..DRRRD..DDODDD.................',  # row 26  tail tip + upper legs
        '..DDD.....DOOBD.................',  # row 27  tail end + legs
        '..........DOOBD.................',  # row 28  legs
        '..........DB.BD.................',  # row 29  ankles
        '.........BBB.BBB................',  # row 30  feet / claws
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
