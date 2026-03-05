import sys
import platform

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont, QFontDatabase

from notpokemon.controllers.game_controller import GameController


def _mono_family() -> str:
    system = platform.system()
    if system == "Darwin":
        return "Menlo"
    elif system == "Windows":
        return "Consolas"
    return QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont).family()


def main():
    app = QApplication(sys.argv)

    mono = _mono_family()

    # Set default font
    font = QFont(mono, 11)
    app.setFont(font)

    # Global stylesheet
    app.setStyleSheet("""
        QWidget {
            background-color: #1a1a2e;
        }
        QToolTip {
            background-color: #16213e;
            color: #e0e0e0;
            border: 1px solid #2c3e6b;
            font-family: monospace;
            font-size: 11px;
            padding: 4px;
        }
    """)

    controller = GameController()
    controller.start()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
