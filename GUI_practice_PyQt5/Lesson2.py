# Imports
from PyQt5.QtWidgets import (QApplication, QGridLayout,
                             QHBoxLayout, QVBoxLayout,
                             QWidget, QPushButton, QLineEdit)
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()

        # App Settings
        self.setWindowTitle("Calculator")
        self.resize(500, 600)

        # All Objects
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 15))


        self.grid = QGridLayout()

        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            # CSS button List
            button.setStyleSheet("QPushButton { font: 11pt Comic Sans MS; padding: 7px; }")
            self.grid.addWidget(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("C")
        self.delete = QPushButton("<")
        # CSS Buttons (c <)
        self.clear.setStyleSheet("QPushButton { font: 11pt Comic Sans MS; padding: 7px; }")
        self.delete.setStyleSheet("QPushButton { font: 11pt Comic Sans MS; padding: 7px; }")

        # Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(10,10,10,10) # CSS for layout

        self.setLayout(master_layout)

        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    # Functions
    def button_click(self):

        button = self.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                self.text_box.setText("Error")
                print("Error:", e)

        elif text == "C":
            self.text_box.clear()

        elif text == "<":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)

if __name__ == "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget { background-color: #f0f0f8 }") # CSS for main win
    main_window.show()
    app.exec_()