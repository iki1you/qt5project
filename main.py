import sys
from random import randint

from PyQt5 import uic

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Минипланировщик')
        self.pushButton.clicked.connect(self.runAction)
        self.obj = []

    def runAction(self):
        self.obj.append(Circle(randint(10, 300), randint(10, 300),
                               randint(10, 300), randint(10, 300)))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for i in self.obj:
            i.draw(painter)
            self.update()
        painter.end()


class Circle:
    def __init__(self, cx, cy, x, y):
        self.cx = cx
        self.cy = cy
        self.x = x
        self.y = y

    def draw(self, painter):
        painter.setPen(QPen(QColor(Qt.yellow)))
        radius = int(((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.cx - radius, self.cy - radius, 2 * radius, 2 * radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
