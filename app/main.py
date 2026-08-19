import sys

from PyQt6.QtWidgets import QApplication
from app.gui.screens.main_window import MainWindow

app = QApplication(sys.argv)

with open("./app/resources/styles/main.qss", "r") as file:
    app.setStyleSheet(file.read())

window = MainWindow()
window.show()

app.exec()