from PyQt6.QtWidgets import QMainWindow

from app.settings import AppSettings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = AppSettings()

        self.resize(1200, 800)

        self.settings.restore_window(self)

    def closeEvent(self, event):
        self.settings.save_window(self)
        event.accept()