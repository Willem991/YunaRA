from PyQt6.QtWidgets import QMenu
from typing import Callable
from PyQt6.QtWidgets import QMainWindow

class MainMenu():
    def __init__(self, window: QMainWindow, css_ID:str):
        self.menu = window.menuBar()
        self.menu.setObjectName(css_ID)

        self.file_menu = self.menu.addMenu("&File")
        self.edit_menu = self.menu.addMenu("&Edit")
        self.view_menu = self.menu.addMenu("&View")
        self.help_menu = self.menu.addMenu("&Help")

    def add_sub_menu_item(subMenu:QMenu, name:str, function:Callable, *args):
        action = subMenu.addAction(name)
        action.triggered.connect(lambda checked: function(*args))

