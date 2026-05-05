from PIL.ImageOps import grayscale
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QListWidget,
                             QHBoxLayout, QVBoxLayout,
                             QWidget, QPushButton, QComboBox, QLabel)


class PhotoEditorApp(QWidget):
    def __init__(self):
        super().__init__()

        # App Settings
        self.setWindowTitle("Photo Editor")
        self.resize(900, 700)

        # All app widgets/objects
        btn_folder = QPushButton("Folder")
        file_list = QListWidget()

        btn_left = QPushButton("Left")
        btn_right = QPushButton("Right")
        mirror = QPushButton("Mirror")
        sharpness = QPushButton("Sharpen")
        gray = QPushButton("Gray")
        saturation = QPushButton("Saturation")
        contrast = QPushButton("Contrast")
        blur = QPushButton("Blur")

        # Dropdown box
        filter_box = QComboBox()
        filter_box.addItem("Original")
        filter_box.addItem("Left")
        filter_box.addItem("Right")
        filter_box.addItem("Mirror")
        filter_box.addItem("Sharpen")
        filter_box.addItem("Gray")
        filter_box.addItem("Saturation")
        filter_box.addItem("Contrast")
        filter_box.addItem("Blur")

        picture_box = QLabel("Image will appear here...")

        # App Design



if __name__ == "__main__":
    app = QApplication([])
    main_window = PhotoEditorApp()
    main_window.show()
    app.exec_()