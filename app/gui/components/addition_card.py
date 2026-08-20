from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStyle, QStyleOption, QLabel, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt, QThreadPool
import shutil
import os

from app.services.file_loader import FileLoader

class AdditionCard(QWidget):
    def __init__(self, style_ID: str):
        super().__init__()

        self.setObjectName(style_ID)

        self.lay_out = QVBoxLayout()

        #Def child widgets
        img = QLabel()
        img.setObjectName("add_icon")
        pixmap = QPixmap("app/resources/images/plus.png")
        resized_pixmap = pixmap.scaled(
            100, 100, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )
        img.setPixmap(resized_pixmap)

        #Add child widgets
        self.lay_out.addStretch()
        self.lay_out.addWidget(img, alignment=Qt.AlignmentFlag.AlignCenter)
        self.lay_out.addStretch() 

        self.setLayout(self.lay_out)

        #Setting up concurrency
        self.threadpool = QThreadPool()
        thread_count = self.threadpool.maxThreadCount()

    # Allows custom widgets to use css
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)

    def mouseReleaseEvent(self, e):
        dlg = QFileDialog(self)

        if dlg.exec():
            files = dlg.selectedFiles()

            if files:
                worker = FileLoader(files)
                self.threadpool.start(worker)
            else:
                QMessageBox.critical(
                    None,
                    "Upload Failed",
                    "The file could not be uploaded."
                )