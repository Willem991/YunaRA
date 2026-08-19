from PyQt6.QtWidgets import QMainWindow

from app.settings import AppSettings
from app.gui.menus.main_menu import MainMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting the size of the app on startup
        
        self.settings = AppSettings()

        self.resize(1200, 800)

        self.settings.restore_window(self)

        # Adding in the Main Menu

        menu = MainMenu(self)
        MainMenu.addSubMenuItem(menu.file_menu, "print", print, "hello")

    def closeEvent(self, event):
        self.settings.save_window(self)
        event.accept()