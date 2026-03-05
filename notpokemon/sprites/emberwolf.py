from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class EmberwolfSprite(SpriteRenderer):
    """Pixel art sprite for Emberwolf -- a lean fire wolf in a lunging run pose."""

    PALETTE = {
        'R': QColor('#CC3300'),   # deep orange-red body
        'F': QColor('#FFB300'),   # bright yellow-orange flame tips
        'T': QColor('#E8C090'),   # light tan belly
        'E': QColor('#FF6600'),   # dark amber eye
        'B': QColor('#111111'),   # black outline
        'S': QColor('#8B1A00'),   # shadow / darker shading
    }

    # 32 rows x 32 characters each  (columns 0-31)
    # '.' = transparent
    # Side-profile lean fire wolf in a forward lunging run, facing right.
    # Flame-tipped arcing tail rises up from left side. Flame mane spikes on
    # upper back. Open snarling jaw on right. Four legs mid-stride.
    #
    #   R = deep orange-red body   F = flame yellow-orange tip
    #   T = light tan belly        E = amber eye
    #   B = black outline          S = shadow/darker shading
    #   . = transparent
    GRID = [
        #          1111111111222222222233
        #0123456789012345678901234567890 1
        '................................',  # row  0
        '...FF...........................',  # row  1  flame tail tip
        '..FFF...........................',  # row  2  flame
        '.BFFB...........................',  # row  3  flame upper
        '.BFFB...........................',  # row  4  flame
        '.BRRB...........................',  # row  5  tail upper
        '..BRRB..........................',  # row  6  tail arc
        '...BRRB.........................',  # row  7  tail
        '....BRRB.......BBBBB............',  # row  8  tail + mane spikes
        '.....BRRB.....BRRRRRSB..........',  # row  9  tail + upper body
        '......BRRB...BRRRRRRRSB.........',  # row 10  tail + back
        '.......BRRBB.BRRRTRRRRSB........',  # row 11  tail joins body + belly
        '........BRRRRRRRRTTRRRSBB.......',  # row 12  body + belly
        '.........BRRRRRTTTTRRRRSBB......',  # row 13  body widest + belly
        '..........BRRRTTTTTRRRSB........',  # row 14  belly center
        '...........BRSTTTTTRRSB.........',  # row 15  belly lower
        '..........BBBRRTTTRRBB..........',  # row 16  underside
        '...BBBBB....BRRRRRSB............',  # row 17  mane spikes + lower body
        '..BRRRRSB....BSSSSB.............',  # row 18  mane/neck + leg root
        '.BRRRERRSB....BB................',  # row 19  head + eye (E)
        'BRRRRRRRSB..BB..................',  # row 20  head + snout upper
        '.BRRRRRBB..BB...................',  # row 21  lower jaw / snout
        '..BBBRB...BB.BB.................',  # row 22  teeth + front legs
        '.......BB..B...B................',  # row 23  paw + back leg
        '.......BB..BB..BB...............',  # row 24  lower paws
        '........B...B...B...............',  # row 25  paw tips
        '........BBB.BB..BB..............',  # row 26  claws
        '................................',  # row 27
        '................................',  # row 28
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
