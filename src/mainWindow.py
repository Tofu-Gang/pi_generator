__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QMainWindow, QGraphicsView, QMessageBox
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from src.dataModel import DataModel



################################################################################

class MainWindow(QMainWindow):
    WIDTH = 800
    HEIGHT = 600

################################################################################

    def __init__(self, parent=None):
        super().__init__(parent)
        model = DataModel()
        model.aboutButtonClicked.connect(self.about)
        view = QGraphicsView(model)
        view.setRenderHint(QPainter.Antialiasing, True)
        self.setCentralWidget(view)
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.setWindowTitle('Pi told me how to solo!')

################################################################################

    def about(self):
        """

        """

        aboutDialog = QMessageBox(self)
        aboutDialog.setTextFormat(Qt.RichText)
        aboutDialog.setWindowTitle('About')
        text = '<p>External resources used:</p>' \
               '<ul>' \
               '<li>All scales based on <a href="http://www.scalerator.com/">' \
               'Scalerator</a>;</li>' \
               '<li>Pi to 1000000 decimal places taken from the ' \
               '<a href="http://newton.ex.ac.uk/research/qsystems/collabs/pi/">' \
               'University of Exeter</a>.</li>' \
               '</ul>' \
               '<p>Implemented in <a href="https://www.python.org/">Python 3</a> ' \
               'and <a href="https://riverbankcomputing.com/software/pyqt/intro">' \
               'PyQt5</a>.</p>' \
               '<p>Pi Generator is created by Tofu Gang and is published under ' \
               '<a href="https://opensource.org/licenses/MIT">MIT</a> license. ' \
               'Feel free to <a href="mailto:tofugangsw@gmail.com">contact us</a>.</p>'
        aboutDialog.setText(text)
        aboutDialog.exec_()

################################################################################