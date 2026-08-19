from PyQt6.QtWidgets import QWidget, QVBoxLayout

class Sidebar():
    def __init__(self,style_ID:str):
        self.widget = QWidget()
        self.widget.setObjectName(style_ID)
        self.widget.setMinimumWidth(0)
        self.layout = QVBoxLayout(self.widget)

    
