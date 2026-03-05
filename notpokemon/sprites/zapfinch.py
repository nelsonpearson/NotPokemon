from PySide6.QtGui import QColor, QPainter

from notpokemon.sprites.base import SpriteRenderer


class ZapfinchSprite(SpriteRenderer):
    """Sprite for Zapfinch – a small fierce electric finch in side profile."""

    PALETTE = {
        'Y': QColor('#FFD700'),   # bright yellow body
        'D': QColor('#2C2C2C'),   # dark charcoal streaks/wing edges
        'W': QColor('#FFFFFF'),   # white eye
        'P': QColor('#111111'),   # black pupil/outline
        'K': QColor('#FF8C00'),   # orange beak
        'C': QColor('#00BFFF'),   # electric blue wing highlight
    }

    # 32x32 pixel grid — '.' is transparent
    # Small sleek bird in side profile facing right. Short beak, wings folded.
    # Bright yellow with dark charcoal streaks and electric blue wing highlight.
    #
    # Palette key:
    #   Y = yellow (#FFD700)   D = charcoal (#2C2C2C)
    #   W = white (#FFFFFF)    P = black pupil (#111111)
    #   K = orange beak (#FF8C00) C = elec. blue (#00BFFF)
    #   . = transparent
    GRID = [
        # 0         1         2         3
        # 01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '................................',  # row  2
        '...........PPPP.................',  # row  3  head top
        '..........PYYYYY................',  # row  4
        '.........PYYYYYYY...............',  # row  5
        '.........PYWPYYYYY..............',  # row  6  eye
        '........PYYYYDDDYYY.............',  # row  7  dark streak
        '........PYYYYYDDDYY.KKP.........',  # row  8  beak level
        '.......PYYYYYYDDDDYKKP..........',  # row  9  beak
        '.......PYYYYYYDDDDYYY...........',  # row 10
        '.......PYYYYDDDDDYYY............',  # row 11  body / wing top
        '......PYYYYYYDDCCYYY............',  # row 12  blue highlight
        '......PYYYYYDDDCCYYP............',  # row 13
        '......PYYYYYDDDDCYYYP...........',  # row 14
        '.....PYYYYYYDDDDDYYYYP..........',  # row 15  wing body
        '.....PYYYYYYYYDDDYYYYP..........',  # row 16
        '.....PYYYYYYYYDDYYYYP...........',  # row 17
        '.....PYYYYYYYYYYYYYP............',  # row 18  belly
        '......PYYYYYYYYYYYYP............',  # row 19
        '......PYYYYYYYYYYYY.............',  # row 20
        '.......PPYYYYYYYYYY.............',  # row 21
        '........PPYYYYYYYYP.............',  # row 22  tail start
        '.......DPYYYYYYYPP..............',  # row 23  tail feathers
        '......DDPYYYYPPP................',  # row 24
        '.....DDDPYYPP...................',  # row 25  tail tip
        '......PPPYP.....................',  # row 26  feet area
        '......PYYP.PPPP.................',  # row 27  legs/feet
        '......PPPP.PPPP.................',  # row 28
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
