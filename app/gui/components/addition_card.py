from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStyle, QStyleOption
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt

class AdditionCard(QWidget):
    def __init__(self, style_ID: str):
        super().__init__()

        self.setObjectName(style_ID)

        self.lay_out = QVBoxLayout()

        #Def child widgets

        #Add child widgets
        self.lay_out.addStretch()
        self.lay_out.addWidget(QPushButton("Hello"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.lay_out.addStretch() 

        self.setLayout(self.lay_out)

    # Allows custom widgets to use css
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)