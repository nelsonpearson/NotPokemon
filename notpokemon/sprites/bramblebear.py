from PySide6.QtGui import QColor, QPainter

from notpokemon.sprites.base import SpriteRenderer


class BramblebearSprite(SpriteRenderer):
    """Sprite for Bramblebear – a large nature bear sitting upright with thorn spikes."""

    PALETTE = {
        'O': QColor('#111111'),   # dark outline
        'F': QColor('#1E5E1E'),   # dark forest green body
        'S': QColor('#5C3317'),   # thorny brown spikes
        'L': QColor('#3A8A3A'),   # lighter green belly
        'P': QColor('#0A1A0A'),   # dark paw pads
        'E': QColor('#CC7700'),   # amber eye
    }

    # 32x32 pixel grid — '.' is transparent
    # Large bear sitting upright facing viewer. Bramble/thorn spikes on
    # shoulders and back. Round face, small ears, lighter belly.
    #
    # Palette key:
    #   O = outline (#111111)    F = forest green (#1E5E1E)
    #   S = spike brown (#5C3317) L = light belly (#3A8A3A)
    #   P = paw pad (#0A1A0A)    E = amber eye (#CC7700)
    #   . = transparent
    GRID = [
        # 0         1         2         3
        # 01234567890123456789012345678901
        '................................',  # row  0
        '.......SSSS......SSSS...........',  # row  1  spike tips
        '......SSSSS......SSSSS..........',  # row  2
        '.....SSFFSS......SSFFSS.........',  # row  3  spikes at shoulders
        '.....SFFFSS.OOOO.SSFFS..........',  # row  4  head top
        '......OOO.OFFFFFFO.OOO..........',  # row  5  ear area
        '.....OFFO.OFFFFFFO.OFFO.........',  # row  6  ears + head
        '....OFFFO.FFFFFFFFO.FFFO........',  # row  7
        '....OFFFOFFFFFFFFFOOFFFOO.......',  # row  8  top of head
        '...OFFFFFFFFFFFFFFFFFFFFO.......',  # row  9
        '...OFFFEFFFFFFFFFFFFFFEFO.......',  # row 10  eyes
        '...OFFFFFFFFFFFFFFFFFFFFOO......',  # row 11
        '...OFFFFFFFFFFFFFFFFFFFFFO......',  # row 12  snout area
        '...OOOFFFFLLLLLLFFFFOOOO........',  # row 13  belly starts
        '....OFFFFFFLLLLLLFFFFO..........',  # row 14
        '....OFFFFFFLLLLLLFFFFOO.........',  # row 15  body wide
        '....OFFFFFFLLLLLLFFFFFO.........',  # row 16
        '...SSOFFFFFFLLLLLFFFFFSSO.......',  # row 17  spikes on sides
        '..SSSOFFFFFFLLLLLFFFFF.SSO......',  # row 18
        '..SSOOFFFFFFLLLLLFFFFFF.SO......',  # row 19
        '...OOOFFFFFFLLLLLFFFFFOO........',  # row 20
        '.....OFFFFFFLLLLLFFFFFF.........',  # row 21
        '.....OFFFFFFLLLLLFFFFFF.........',  # row 22
        '....OOFFFFFFLLLLLFFFFOO.........',  # row 23  arm/paw area
        '...OFPPOFFFFFFLFFFFPPO..........',  # row 24  paw pads
        '...OPPPOFFFFFFFFFFPPO...........',  # row 25
        '...OPPPOOOOOOOOOOOPPO...........',  # row 26
        '....OOPPOOOOOOOOOPPO............',  # row 27  lower body/legs
        '....OFFFOOO....OOFFFO...........',  # row 28
        '....OFFFOO......OFFFOO..........',  # row 29
        '....OOOOO........OOOOO..........',  # row 30  paws/feet
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
