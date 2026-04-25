# Imports
from PyQt5.QtWidgets import (QApplication, QGridLayout,
                             QHBoxLayout, QVBoxLayout,
                             QWidget, QPushButton, QLineEdit)

# App Settings
app = QApplication([])
window1 = QWidget()
window1.setWindowTitle("Calculator")
window1.resize(500,700)

# All Objects
text_box = QLineEdit()
grid = QGridLayout()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

clear = QPushButton("C")
delete = QPushButton("<")

row = 0
col = 0

for text in buttons:
    button = QPushButton(text)
    #button.clicked.connect()
    grid.addWidget(button, row, col)
    col +=1

    if col > 3:
        col = 0
        row += 1

# Design
master_layout1 = QVBoxLayout()
master_layout1.addWidget(text_box)
master_layout1.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout1.addLayout(button_row)

# Show/Run
window1.show()
app.exec_()