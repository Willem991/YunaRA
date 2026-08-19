from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QStackedLayout, QWidget

from app.settings import AppSettings
from app.gui.menus.main_menu import MainMenu
from app.gui.components.sidebar import Sidebar
from app.gui.components.library import Library


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting of the app on startup
        
        #Size
        self.settings = AppSettings()
        self.resize(1200, 800)
        self.settings.restore_window(self)

        #CSS ID
        self.setObjectName("main_window")

        # Layout Setup
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(4, 4, 4, 4)
        main_layout.setSpacing(10)

        nav_bar = Sidebar("nav_bar")

        display_layout = QStackedLayout()
        library = Library("library")
        display_layout.addWidget(library.widget)

        main_layout.addWidget(nav_bar.widget, 1)
        main_layout.addLayout(display_layout, 29)


        # Adding in the main holding widget
        central_widget = QWidget()
        central_widget.setObjectName("central_widget")
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Adding in the Main Menu

        menu = MainMenu(self, "menu")
        MainMenu.add_sub_menu_item(menu.file_menu, "print", print, "hello")

    def closeEvent(self, event):
        self.settings.save_window(self)
        event.accept()