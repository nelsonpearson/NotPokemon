from PySide6.QtGui import QColor, QPainter

from notpokemon.sprites.base import SpriteRenderer


class ThornhareSprite(SpriteRenderer):
    """Sprite for Thornhare – a nature rabbit with leaf-shaped green ears."""

    PALETTE = {
        'O': QColor('#2F2F2F'),   # outline
        'G': QColor('#228B22'),   # ear green
        'D': QColor('#006400'),   # ear vein / dark green
        'B': QColor('#8B4513'),   # body brown
        'T': QColor('#D2B48C'),   # belly tan
        'W': QColor('#FFFFFF'),   # eye white / cotton tail
        'P': QColor('#000000'),   # pupil
    }

    # 32x32 pixel grid — '.' is transparent
    # Upright sitting rabbit facing right with leaf-shaped green ears
    #
    # Palette key:
    #   O = outline       G = ear green     D = dark green vein
    #   B = body brown    T = belly tan     W = white (eye/tail)
    #   P = pupil black   . = transparent
    GRID = [
        # 0         1         2         3
        # 0123456789012345678901234567890 1
        '................................',  # row  0
        '................................',  # row  1
        '..........O..........O..........',  # row  2  ear tips
        '.........OGO........OGO.........',  # row  3
        '.........OGGO......OGGO.........',  # row  4
        '........OGDGO.....OGDGO.........',  # row  5
        '........OGDGGO...OGDGGO.........',  # row  6
        '.......OGGDGGO..OGGDGGO.........',  # row  7
        '.......OGGGDGGOOGGGDGGO.........',  # row  8
        '......OGGGGGGGGGGGGGGGO.........',  # row  9
        '.......OGGGGGGGGGGGGGO..........',  # row 10
        '........OOOGGGGGGGGOOO..........',  # row 11
        '..........OOOBBBBOOO............',  # row 12  head begins
        '.........OBBBBBBBBBO............',  # row 13
        '........OBBBBWPBBBBO............',  # row 14  eye
        '........OBBBBBBBBBBBO...........',  # row 15
        '........OBBBBBBBBBBBOP..........',  # row 16  nose dot
        '.........OBBBBBBBBBO............',  # row 17
        '........OOBBBBBBBBBOO...........',  # row 18  neck
        '.......OBBBBBTTTBBBBBO..........',  # row 19
        '......OBBBBTTTTTBBBBBBO.........',  # row 20
        '......OBBBTTTTTTTBBBBBO.........',  # row 21
        '.....OOBBTTTTTTTTTBBBOO.........',  # row 22
        '.....OBBBBTTTTTTTBBBBOO.........',  # row 23
        '....OOBBBBBTTTTBBBBBOOWW........',  # row 24  tail
        '....OBBBBBBBBBBBBBBBOO..WW......',  # row 25
        '....OBBBOOO.....OOOBBBO.WO......',  # row 26
        '...OOBBO.........OOBBOO.........',  # row 27  legs
        '...OBBBO..........OBBBO.........',  # row 28
        '..OBBBBBO........OBBBBBO........',  # row 29  big back feet
        '..OOOOOOO........OOOOOOO........',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
