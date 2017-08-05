__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRectF, QPointF, Qt
from src.scales import NOTES_SHARP, NOTES_FLAT



################################################################################

class ScaleTextItem(QGraphicsItem):
    HEIGHT = 40
    WIDTH = 13*HEIGHT
    FONT_SIZE = 20
    FONT_FAMILY = 'Helvetica'
    FONT = QFont(FONT_FAMILY, FONT_SIZE)
    BOUNDING_RECT = QRectF(QPointF(-WIDTH/2, -HEIGHT/2), QPointF(WIDTH/2, HEIGHT/2))

################################################################################

    def __init__(self, parent=None):
        super().__init__(parent)
        self._rects = [QRectF(QPointF(-self.WIDTH/2+(i*self.HEIGHT), -self.HEIGHT/2),
                              QPointF(-self.WIDTH/2+(i+1)*self.HEIGHT, self.HEIGHT/2))
                       for i in range(13)]
        self._scale = None
        self._notes = None

################################################################################

    def setScale(self, scale):
        """

        """

        self._scale = scale.split()
        if any(['#' in note for note in scale]) and all(['b' not in note for note in self._scale]):
            notes = NOTES_SHARP.split()
        elif any(['b' in note for note in scale]) and all(['#' not in note for note in self._scale]):
            notes = NOTES_FLAT.split()
        else:
            notes = NOTES_SHARP.split()
        self._notes = notes[notes.index(self._scale[0]):]+notes[:notes.index(self._scale[0])+1]
        self.update()

################################################################################

    def paint(self, painter, option, widget):
        """

        """

        painter.setFont(self.FONT)
        for i in range(len(self._notes)):
            note = self._notes[i]
            if note in self._scale:
                painter.setPen(Qt.green)
            else:
                painter.setPen(Qt.darkRed)
            painter.drawText(self._rects[i], Qt.AlignCenter, note)

################################################################################

    def boundingRect(self):
        """

        """

        return self.BOUNDING_RECT

################################################################################