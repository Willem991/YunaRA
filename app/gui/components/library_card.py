from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStyle, QStyleOption
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
import uuid

class LibraryCard(QWidget):
    def __init__(self, img_url: str, title: str, file_url:str):
        super().__init__()

        self.setObjectName(str(uuid.uuid4()))
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

        # Child widgets
        title_lbl = QLabel(self.title)

        # Add child widgets
        #self.lay_out.addWidget(title_lbl)
        self.lay_out.addWidget(self.image_label)

        self.setLayout(self.lay_out)

    def delete_book(self):
        Path(self.img_url).unlink()
        Path(self.file_url).unlink()
        self.setParent(None)
        self.deleteLater()

    # Allows custom widgets to use css
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)