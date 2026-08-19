from PyQt6.QtWidgets import QWidget, QHBoxLayout

class LibraryRow(QWidget):
    def __init__(self,style_ID:str):
        super().__init__()

        self.setObjectName(style_ID)
        self.layout = QHBoxLayout(self)