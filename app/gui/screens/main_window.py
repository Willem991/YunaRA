from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QStackedLayout, QWidget, QScrollArea
from PyQt6.QtCore import Qt

from app.settings import AppSettings
from app.gui.menus.main_menu import MainMenu
from app.gui.components.sidebar import Sidebar
from app.gui.components.library import Library
from app.gui.components.addition_card import AdditionCard

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

        #Creating and Adding the sidebar
        nav_bar = Sidebar("nav_bar")
        main_layout.addWidget(nav_bar, 1)

        #Creating and Adding the library
        display_layout = QStackedLayout()
        main_layout.addLayout(display_layout, 29)

        scroll_area = QScrollArea()

        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        library = Library("library")

        scroll_area.setWidget(library)

        display_layout.addWidget(scroll_area)

        addition_card = AdditionCard("add_book_card")
        library.lay_out.addWidget(addition_card)
        for i in range(0,30):
            library.lay_out.addWidget(AdditionCard("add_book_card"))

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