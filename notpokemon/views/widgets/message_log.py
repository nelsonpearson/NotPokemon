from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QTextEdit


class MessageLog(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setFixedHeight(100)
        self.setFont(QFont("monospace", 11))
        self.setStyleSheet("""
            QTextEdit {
                background-color: #0a0a1a;
                color: #e0e0e0;
                border: 2px solid #2c3e6b;
                border-radius: 4px;
                padding: 6px;
            }
        """)

    def add_message(self, text: str, color: str = "#e0e0e0"):
        self.append(f'<span style="color: {color};">{text}</span>')
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

    def add_effectiveness(self, text: str, effective_type: str):
        if effective_type == "super_effective":
            color = "#2ecc71"
        elif effective_type == "not_effective":
            color = "#e74c3c"
        else:
            color = "#e0e0e0"
        self.add_message(text, color)

    def clear_log(self):
        self.clear()
