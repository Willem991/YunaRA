from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class LibraryCard(QWidget):
    def __init__(self, style_ID: str, img_url: str, name: str):
        super().__init__()

        self.setObjectName(style_ID)

        self.setLayout = QVBoxLayout()

        self.img = img_url
        self.name = name

        # Child widgets
        title = QLabel(name)

        # Add child widgets
        self.layout.addWidget(title)