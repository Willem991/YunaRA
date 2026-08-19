from PyQt6.QtCore import QSettings


class AppSettings:
    def __init__(self):
        self.settings = QSettings("Yuna's tools", "YunaRA")

    #Saving the size and state of the main application window

    def save_window(self, window):
        self.settings.setValue("window/geometry", window.saveGeometry())
        self.settings.setValue("window/state", window.saveState())

    def restore_window(self, window):
        geometry = self.settings.value("window/geometry")
        state = self.settings.value("window/state")

        if geometry:
            window.restoreGeometry(geometry)

        if state:
            window.restoreState(state)