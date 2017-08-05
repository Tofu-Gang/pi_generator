__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QMainWindow, QGraphicsView
from PyQt5.QtGui import QPainter
from dataModel import DataModel



################################################################################

class MainWindow(QMainWindow):
    WIDTH = 800
    HEIGHT = 600

################################################################################

    def __init__(self, parent=None):
        super().__init__(parent)
        view = QGraphicsView(DataModel())
        view.setRenderHint(QPainter.Antialiasing, True)
        self.setCentralWidget(view)
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.setWindowTitle('Pi told me how to solo!')

################################################################################