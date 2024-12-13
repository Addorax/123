import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRect

class UI:
    def setup_ui(self, mw):
        mw.setWindowTitle("Программа")
        mw.setGeometry(100, 100, 400, 300)

        cw = QWidget()
        mw.setCentralWidget(cw)
        lt = QVBoxLayout(cw)

        self.btn = QPushButton("Нарисовать")
        lt.addWidget(self.btn)

        self.ca = CA()
        lt.addWidget(self.ca)

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI()
        self.ui.setup_ui(self)
        self.ui.btn.clicked.connect(self.add_c)

    def add_c(self):
        self.ui.ca.add_c()
        self.ui.ca.update()

class CA(QWidget):
    def __init__(self):
        super().__init__()
        self.cs = []

    def add_c(self):
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        s = random.randint(20, 100)
        c = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 128)
        self.cs.append((x, y, s, c))

    def paintEvent(self, e):
        tp = QPainter(self)

        for x, y, s, c in self.cs:
            tp.setBrush(c)
            tp.drawEllipse(QRect(x - s // 2, y - s // 2, s, s))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MW()
    w.show()
    sys.exit(app.exec())
