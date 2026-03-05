from PySide6.QtGui import QPainter, QColor

from notpokemon.sprites.base import SpriteRenderer


class CoralSnapSprite(SpriteRenderer):
    """Pixel art sprite for Coralsnap -- a wide coral-colored crab with raised claws."""

    PALETTE = {
        'C': QColor('#F08080'),   # coral pink body
        'K': QColor('#C0392B'),   # darker coral claw edges
        'H': QColor('#F5CBA7'),   # sandy cream joint highlights
        'P': QColor('#111111'),   # dark eye dots
        'D': QColor('#8B0000'),   # dark outline
    }

    # 32 rows, each exactly 32 characters
    # '.' = transparent
    GRID = [
        #01234567890123456789012345678901
        '................................',  # row  0
        '................................',  # row  1
        '...DKD.....................DKD..',  # row  2  upper claw tips
        '..DKKD....................DKKD..',  # row  3  claw upper
        '..DKCD....................DKCD..',  # row  4  claw body
        '...DKD....................DKD...',  # row  5  claw mid
        '....DD..DKD........DKD....DD....',  # row  6  claw base + smaller tips
        '....DKKDKKD...DD...DKKDKKD......',  # row  7  claws meeting / arms
        '....DKKCKKD..DCCD..DKKCKKD......',  # row  8  claw inner + arms
        '.....DKKKD..DCCCD...DKKKD.......',  # row  9  upper arm + upper body edge
        '......DKD..DCCCCD....DKD........',  # row 10  arm joint + body top
        '.......D...DCCPCD..........D....',  # row 11  eye row (P=pupil)
        '........DDDDCPCDDDDDDDDDDDD.....',  # row 12  body top edge + second eye
        '.......DCCCCCCCCCCCCCCCCCCCD....',  # row 13  body upper
        '......DCCCCCCCCCCCCCCCCCCCCCD...',  # row 14  body main
        '......DCCCHHHHHHHHHHHCCCCCCD....',  # row 15  body with cream highlight
        '......DCCCHHHHHHHHHHHHCCCCCD....',  # row 16  body belly
        '......DCCCCHHHHHHHHHHCCCCCCD....',  # row 17  body belly lower
        '......DCCCCCCCCCCCCCCCCCCCD.....',  # row 18  lower body
        '.....DDCCCCCCCCCCCCCCCCCDD......',  # row 19  body base
        '....DC..DCCCCCCCCCCCCCD...CD....',  # row 20  legs top row
        '...DCD..DCCCCCCCCCCCD....DCDD...',  # row 21  body + legs
        '..DCCD...DHHD..DHHD.....DCCD....',  # row 22  leg joints
        '..DCDD...DCCD..DCCD.....DCHD....',  # row 23  legs mid
        '..DCD....DCDD..DCDD.....DCHD....',  # row 24  legs lower
        '..DDD.....DHD...DHD......DDD....',  # row 25  leg tips / feet
        '................................',  # row 26
        '................................',  # row 27
        '................................',  # row 28
        '................................',  # row 29
        '................................',  # row 30
        '................................',  # row 31
    ]

    def _draw(self, painter: QPainter, scale: int):
        self._draw_grid(painter, scale, self.GRID, self.PALETTE)
