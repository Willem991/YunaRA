from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStyle, QStyleOption
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter

from app.gui.layouts.flow_layout import FlowLayout

class Library(QWidget):
    def __init__(self, style_ID:str):
        super().__init__()

        self.setObjectName(style_ID)


        self.lay_out = FlowLayout()

        self.setLayout(self.lay_out)

    # Allows custom widgets to use css
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)

                 

    
