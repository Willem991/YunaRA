from PyQt6.QtWidgets import QWidget, QVBoxLayout

class Library():
    def __init__(self,style_ID:str):
        self.widget = QWidget()
        self.widget.setObjectName(style_ID)
        self.layout = QVBoxLayout(self.widget)

    
