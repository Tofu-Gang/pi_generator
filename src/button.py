__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QGraphicsObject
from PyQt5.QtGui import QPainterPath, QPen, QFont, QBrush
from PyQt5.QtCore import pyqtSignal as Signal, QRectF, QPointF, Qt
from random import randint



################################################################################

class Button(QGraphicsObject):
    PEN_WIDTH_NORMAL = 3
    PEN_WIDTH_HOVER = 6
    FONT_SIZE = 20
    FONT_FAMILY = 'Helvetica'
    FONT = QFont(FONT_FAMILY, FONT_SIZE)
    clicked = Signal()

################################################################################

    def __init__(self, text, width, height, parent=None):
        super().__init__(parent)
        self.setAcceptHoverEvents(True)
        self._hover = False
        self._penMargin = self.PEN_WIDTH_NORMAL/2
        self._WIDTH = width
        self._HEIGHT = height

        self._A_DEFAULT = QPointF(-self._WIDTH/2, -self._HEIGHT/2)
        self._B_DEFAULT = QPointF(self._WIDTH/2, -self._HEIGHT/2)
        self._C_DEFAULT = QPointF(self._WIDTH/2, self._HEIGHT/2)
        self._D_DEFAULT = QPointF(-self._WIDTH/2, self._HEIGHT/2)
        self._BOUNDING_RECT_DEFAULT = QRectF(self._A_DEFAULT, self._C_DEFAULT)

        self._boundingRect = self._BOUNDING_RECT_DEFAULT
        self._shape = QPainterPath()
        self._shape.moveTo(self._A_DEFAULT)
        self._shape.lineTo(self._B_DEFAULT)
        self._shape.lineTo(self._C_DEFAULT)
        self._shape.lineTo(self._D_DEFAULT)
        self._shape.lineTo(self._A_DEFAULT)
        self._pen = QPen(QBrush(Qt.NoBrush), self.PEN_WIDTH_NORMAL, Qt.SolidLine, Qt.SquareCap, Qt.MiterJoin)
        self._pen.setColor(Qt.green)
        self._text = text

################################################################################

    def paint(self, painter, option, widget):
        """

        """

        painter.setPen(self._pen)
        painter.drawPath(self._shape)
        painter.setFont(self.FONT)
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self._text)

################################################################################

    def boundingRect(self):
        """

        """

        return self._boundingRect

################################################################################

    def shape(self):
        """

        """

        return self._shape

################################################################################

    def hoverEnterEvent(self, event):
        """

        """

        self.prepareGeometryChange()
        self._hover = True
        self._pen.setWidth(self.PEN_WIDTH_HOVER)
        self._penMargin = self.PEN_WIDTH_HOVER/2
        a =  QPointF(-self._WIDTH/2-randint(0, int(self._HEIGHT/3)),
                     -self._HEIGHT/2-randint(0, int(self._HEIGHT/3)))
        b = QPointF(self._WIDTH/2+randint(0, int(self._HEIGHT/3)),
                    -self._HEIGHT/2-randint(0, int(self._HEIGHT/3)))
        c = QPointF(self._WIDTH/2+randint(0, int(self._HEIGHT/3)),
                    self._HEIGHT/2+randint(0, int(self._HEIGHT/3)))
        d = QPointF(-self._WIDTH/2-randint(0, int(self._HEIGHT/3)),
                    self._HEIGHT/2+randint(0, int(self._HEIGHT/3)))
        self._boundingRect = QRectF(QPointF(min(a.x(), d.x())-self._penMargin,
                                            min(a.y(), b.y())-self._penMargin),
                                    QPointF(max(b.x(), c.x())+self._penMargin,
                                            max(c.y(), d.y())+self._penMargin))
        self._shape = QPainterPath()
        self._shape.moveTo(a)
        self._shape.lineTo(b)
        self._shape.lineTo(c)
        self._shape.lineTo(d)
        self._shape.lineTo(a)
        super().hoverEnterEvent(event)

################################################################################

    def hoverLeaveEvent(self, event):
        """

        """

        self.prepareGeometryChange()
        self._hover = False
        self._pen.setWidth(self.PEN_WIDTH_NORMAL)
        self._penMargin = self.PEN_WIDTH_NORMAL/2
        self._boundingRect = self._BOUNDING_RECT_DEFAULT
        self._shape = QPainterPath()
        self._shape.moveTo(self._A_DEFAULT)
        self._shape.lineTo(self._B_DEFAULT)
        self._shape.lineTo(self._C_DEFAULT)
        self._shape.lineTo(self._D_DEFAULT)
        self._shape.lineTo(self._A_DEFAULT)
        super().hoverLeaveEvent(event)

################################################################################

    def mousePressEvent(self, event):
        """

        """

        self.clicked.emit()
        super().mousePressEvent(event)

################################################################################