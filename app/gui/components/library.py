from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStyle, QStyleOption
from PyQt6.QtGui import QPainter

class Library(QWidget):
    def __init__(self, style_ID:str):
        super().__init__()

        self.setObjectName(style_ID)

        layout = QVBoxLayout()
        self.setLayout(layout)

    def paintEvent(self, event):
            opt = QStyleOption()
            opt.initFrom(self)
            p = QPainter(self)
            self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)
        

    
