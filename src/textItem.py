__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



################################################################################

class TextItem(QGraphicsTextItem):
    LEFT = -1
    CENTER = 0
    RIGHT = 1
    FONT_SIZE_SMALL = 11
    FONT_SIZE_LARGE = 20
    FONT_FAMILY = 'Helvetica'

################################################################################

    def __init__(self, text, variation, pos, parent=None):
        super().__init__(text, parent)
        self._variation = variation
        self._originalPos = pos
        self.setDefaultTextColor(Qt.green)
        if self._variation == self.LEFT or self._variation == self.RIGHT:
            fontSize = self.FONT_SIZE_SMALL
        elif self._variation == self.CENTER:
            fontSize = self.FONT_SIZE_LARGE
        else:
            fontSize = None
        self.setFont(QFont(self.FONT_FAMILY, fontSize))
        self._updatePosition()

################################################################################

    def setPlainText(self, text):
        """

        """

        super().setPlainText(text)
        self._updatePosition()

################################################################################

    def _updatePosition(self):
        """

        """

        self.setPos(self._originalPos)
        if self._variation == self.LEFT:
            self.moveBy(0, -self.boundingRect().height()/2)
        elif self._variation == self.CENTER:
            self.moveBy(-self.boundingRect().width()/2, -self.boundingRect().height()/2)
        elif self._variation == self.RIGHT:
            self.moveBy(-self.boundingRect().width(), -self.boundingRect().height()/2)

################################################################################