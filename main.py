import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QColor
import random


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 500, 350, 402)
        self.c = False
        self.b = QPushButton('кнопка', self)
        self.b.resize(100, 50)
        self.b.move(120, 30)
        self.b.clicked.connect(self.paint)

    def paint(self):
        self.c = True
        self.repaint()

    def paintEvent(self, event):
        if self.c:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        num = random.randint(1, 130)
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        qp.drawEllipse(QPointF(170, 250), num, num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
