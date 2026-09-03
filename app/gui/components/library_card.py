from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStyle, QStyleOption
from PyQt6.QtGui import QPainter, QPixmap, QGuiApplication, QCursor
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect
from pathlib import Path
import uuid
import os

class LibraryCard(QWidget):
    def __init__(self, img_url: str, title: str, file_url:str):
        super().__init__()

        self.setObjectName("library_card")
        print("OBJECT NAME:", self.objectName())
        self.title = title
        self.img_url = img_url
        self.file_url = file_url
        self.setFixedSize(230, 324)

        # Image
        self.image_label = QLabel()
        self.image_label.setObjectName("card_image")

        pixmap = QPixmap(self.img_url)

        pixmap = pixmap.scaled(
            230,
            324,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lay_out = QVBoxLayout()
        self.lay_out.setContentsMargins(0, 0, 0, 0)
        self.lay_out.setSpacing(0)

        #Image Animations
        self.image_animation = QPropertyAnimation(self.image_label, b"geometry")
        self.image_animation.setDuration(100)

        # Add child widgets
        self.lay_out.addWidget(self.image_label)

        self.setLayout(self.lay_out)

    def enterEvent(self, event):
        QGuiApplication.setOverrideCursor(QCursor(Qt.CursorShape.PointingHandCursor));

        self.image_animation.stop()

        self.image_animation.setStartValue(self.image_label.geometry())
        self.image_animation.setEndValue(
            QRect(0, 0, 240, 338)
        )

        self.image_animation.start()

        super().enterEvent(event)


    def leaveEvent(self, event):
        self.image_animation.stop()

        self.image_animation.setStartValue(self.image_label.geometry())
        self.image_animation.setEndValue(
            QRect(0, 0, 230, 324)
        )

        self.image_animation.start()

        QGuiApplication.restoreOverrideCursor();

        super().leaveEvent(event)

    def delete_book(self):
        Path(self.img_url).unlink()
        Path(self.file_url).unlink()
        self.setParent(None)
        self.deleteLater()

    def mouseReleaseEvent(self, e):
        os.startfile(self.file_url)
        

    # Allows custom widgets to use css
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)