import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5 import uic


class Mywid(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.add.clicked.connect(self.ifclicked)
        self.flag = False

    def ifclicked(self):
        self.flag = True
        self.update()


    def paintEvent(self, event):
        if self.flag:
            qp = QPainter(self)
            qp.begin(self)
            self.drawellipse(qp)
            self.flag = False
            qp.end()

    def drawellipse(self, qp):
        size = self.size()
        for i in range(10):
            qp.setBrush(Qt.yellow)
            qp.setPen(Qt.yellow)
            z = random.randint(50, 150)
            x = random.randint(1, size.width() - z)
            y = random.randint(1, size.height() - (z + 50))
            qp.drawEllipse(x, y, z, z)





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Mywid()
    ex.show()
    sys.exit(app.exec_())

