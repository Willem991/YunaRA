import sys

from PyQt6.QtWidgets import QApplication
from app.gui.screens.main_window import MainWindow
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("app/resources/images/yunara.png"))

with open("./app/resources/styles/main.qss", "r") as file:
    app.setStyleSheet(file.read())

window = MainWindow()
window.setWindowTitle("YunaRA")
window.show()

app.exec()