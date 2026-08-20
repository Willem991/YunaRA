from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStyle, QStyleOption, QLabel, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt, QThreadPool
import shutil
import os

from app.services.file_loader import FileLoader
from app.gui.layouts.flow_layout import FlowLayout
from app.gui.components.library_card import LibraryCard

class AdditionCard(QWidget):
    def __init__(self, style_ID: str, library_layout: FlowLayout):
        super().__init__()

        self.setObjectName(style_ID)
        self.library = library_layout
        self.lay_out = QVBoxLayout()
        self.setFixedSize(230, 324)

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
        self.lay_out.setContentsMargins(0, 0, 0, 0)
        self.lay_out.setSpacing(0)

        self.setLayout(self.lay_out)

        #Setting up concurrency
        self.threadpool = QThreadPool()
        thread_count = self.threadpool.maxThreadCount()

    def add_library_card(self, image, title, path):
        image = os.path.abspath(image).replace("\\", "/")

        library_card = LibraryCard(
            image,
            title,
            path
        )

        self.library.insertWidget(0,library_card)

    def show_error(self, message):
        QMessageBox.critical(
            self,
            "Upload Failed",
            message
        )

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

                worker.signals.finished.connect(self.add_library_card)
                worker.signals.error.connect(self.show_error)

                self.threadpool.start(worker)

            else:
                QMessageBox.critical(
                    None,
                    "Upload Failed",
                    "The file could not be uploaded."
                )