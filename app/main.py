import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from app.gui.screens.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()