from PySide6.QtGui import QColor, QPainter

from notpokemon.sprites.base import SpriteRenderer


class DunecobraSprite(SpriteRenderer):
    """Sprite for Dunecobra -- an earth cobra with a wide hood and sandy coloring."""

    PALETTE = {
        'B': QColor('#D2691E'),   # chocolate brown body
        'S': QColor('#F4A460'),   # sandy belly / lighter scales
        'D': QColor('#8B4513'),   # darker brown hood outline
        'G': QColor('#FFD700'),   # gold eye spots on hood
        'R': QColor('#FF0000'),   # tongue red
        'W': QColor('#FFFFFF'),   # eye white
        'K': QColor('#000000'),   # pupil / outline
    }

    # 32x32 pixel grid -- '.' is transparent
    # Coiled cobra facing right with raised hood, eye spots, forked tongue
    #
    # Palette key:
    #   B = brown body     S = sandy scales    D = dark outline
    #   G = gold spots     R = red tongue      W = white eye
    #   K = black pupil    . = transparent
    GRID = [
        # 0         1         2         3
        # 01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '..............DDD...............',  # row  2  hood tip
        '.............DBBBD..............',  # row  3  hood top
        '............DBBBBBD.............',  # row  4  hood widening
        '...........DBBSBBBBD............',  # row  5  hood wider
        '..........DBBSGGSBBBD...........',  # row  6  hood with gold spots
        '.........DBBSGBBGSBBBD..........',  # row  7  hood widest - eye spots
        '.........DBBSGBBGSBBBD..........',  # row  8  hood widest continued
        '..........DBBSGGSBBBD...........',  # row  9  hood narrowing - gold
        '...........DBBBSBBBD............',  # row 10  hood narrowing
        '...........DBBWKBBBD............',  # row 11  eye row (W=white K=pupil)
        '............DBBBBBDDRR..........',  # row 12  snout + forked tongue
        '............DDBBBDD.R...........',  # row 13  lower jaw + tongue tip
        '.............DBBBD..............',  # row 14  neck top
        '.............DSBSD..............',  # row 15  neck with scales
        '............DSBBBSD.............',  # row 16  neck to body
        '...........DSBBBBSD.............',  # row 17  body widening
        '..........DBBBSSBBBD............',  # row 18  upper coil
        '.........DBBBS..SBBBD...........',  # row 19  coil curve right
        '.........DBBD....DBBBD..........',  # row 20  coil gap
        '..........DD......DBBD..........',  # row 21  first coil ends
        '..................DBSD..........',  # row 22  body continues right
        '.............DDDDBBBSD..........',  # row 23  second coil begins
        '...........DDBBBBBSBD...........',  # row 24  coil back left
        '..........DBBBS.SBBBD...........',  # row 25  second coil
        '..........DBBSD..DBBD...........',  # row 26  coil curve
        '...........DBD....DBD...........',  # row 27  coil narrowing
        '...........DSD....DSD...........',  # row 28  tail segments
        '............DD....DD............',  # row 29  tail tip area
        '............D......D............',  # row 30  tail ends
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
