from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QRunnable, QObject, pyqtSignal
from pathlib import Path
import shutil
import os
import pymupdf



class FileLoaderSignals(QObject):
    finished = pyqtSignal(str, str, str)
    error = pyqtSignal(str)

class FileLoader(QRunnable):
    def __init__(self, filepaths: list[str]):
        super().__init__()
        self.filepaths = filepaths
        self.signals = FileLoaderSignals()

    def run(self):
        
        for path in self.filepaths:

            extension = Path(path).suffix
            filename = os.path.basename(path)
            destination = os.path.join(
                            "app",
                            "resources",
                            "books",
                            filename
                        )
            path_dest = Path(destination)
            pix_dest = os.path.join(
                            "app",
                            "resources",
                            "images",
                            "books",
                            path_dest.name + ".png"
                        )
            
            #Copying book file from directory into app
            try:
                if extension in [".pdf", ".epub"]:
                    
                    shutil.copyfile(path, destination)

                else:
                    raise Exception("Incorrect File Type")
                
            except Exception as e:
                QMessageBox.critical(
                    None,
                    "Upload Failed",
                    f"Could not read the file:\n\n{path}\n\n{e}"
                )   

                self.signals.error.emit(
                    f"Could not load {path}\n\n{e}"
                )

            #Creating png to be displayed with book object
            if extension == ".pdf":
                try:
                    with pymupdf.open(destination) as doc:
                        first_page = doc[0]
                        pix = first_page.get_pixmap()
                        pix.save(pix_dest)

                except Exception as e:
                    path_dest.unlink(missing_ok=True)
                    QMessageBox.critical(
                        None,
                        "Upload Failed",
                        f"Could not read the file:\n\n{path}\n\n{e}"
                    )   
                    break

            elif extension == ".epub":
                pass

            else:
                path_dest.unlink(missing_ok=True)
                QMessageBox.critical(
                    None,
                    "Upload Failed",
                    "Incorrect File Type"
                )   

                self.signals.error.emit(
                    f"Could not load {path}\n\n{e}"
                )

            self.signals.finished.emit(
                    pix_dest,
                    path_dest.stem,
                    destination
                )

