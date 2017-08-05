__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QGraphicsObject
from PyQt5.QtGui import QPainterPath, QPen, QFont, QBrush
from PyQt5.QtCore import pyqtSignal as Signal, QRectF, QPointF, Qt
from random import randint



################################################################################

class GenerateButton(QGraphicsObject):
    WIDTH = 150
    HEIGHT = 40
    PEN_WIDTH_NORMAL = 3
    PEN_WIDTH_HOVER = 6
    FONT_SIZE = 20
    FONT_FAMILY = 'Helvetica'
    FONT = QFont(FONT_FAMILY, FONT_SIZE)
    A_DEFAULT = QPointF(-WIDTH/2, -HEIGHT/2)
    B_DEFAULT = QPointF(WIDTH/2, -HEIGHT/2)
    C_DEFAULT = QPointF(WIDTH/2, HEIGHT/2)
    D_DEFAULT = QPointF(-WIDTH/2, HEIGHT/2)
    BOUNDING_RECT_DEFAULT = QRectF(A_DEFAULT, C_DEFAULT)
    clicked = Signal()

################################################################################

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptHoverEvents(True)
        self._hover = False
        self._penMargin = self.PEN_WIDTH_NORMAL/2
        self._boundingRect = self.BOUNDING_RECT_DEFAULT
        self._shape = QPainterPath()
        self._shape.moveTo(self.A_DEFAULT)
        self._shape.lineTo(self.B_DEFAULT)
        self._shape.lineTo(self.C_DEFAULT)
        self._shape.lineTo(self.D_DEFAULT)
        self._shape.lineTo(self.A_DEFAULT)
        self._pen = QPen(QBrush(Qt.NoBrush), self.PEN_WIDTH_NORMAL, Qt.SolidLine, Qt.SquareCap, Qt.MiterJoin)
        self._pen.setColor(Qt.green)

################################################################################

    def paint(self, painter, option, widget):
        """

        """

        painter.setPen(self._pen)
        painter.drawPath(self._shape)
        painter.setFont(self.FONT)
        painter.drawText(self.boundingRect(), Qt.AlignCenter, 'Generate')

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
        a =  QPointF(-self.WIDTH/2-randint(0, int(self.HEIGHT/3)),
                     -self.HEIGHT/2-randint(0, int(self.HEIGHT/3)))
        b = QPointF(self.WIDTH/2+randint(0, int(self.HEIGHT/3)),
                    -self.HEIGHT/2-randint(0, int(self.HEIGHT/3)))
        c = QPointF(self.WIDTH/2+randint(0, int(self.HEIGHT/3)),
                    self.HEIGHT/2+randint(0, int(self.HEIGHT/3)))
        d = QPointF(-self.WIDTH/2-randint(0, int(self.HEIGHT/3)),
                    self.HEIGHT/2+randint(0, int(self.HEIGHT/3)))
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
        self._boundingRect = self.BOUNDING_RECT_DEFAULT
        self._shape = QPainterPath()
        self._shape.moveTo(self.A_DEFAULT)
        self._shape.lineTo(self.B_DEFAULT)
        self._shape.lineTo(self.C_DEFAULT)
        self._shape.lineTo(self.D_DEFAULT)
        self._shape.lineTo(self.A_DEFAULT)
        super().hoverLeaveEvent(event)

################################################################################

    def mousePressEvent(self, event):
        """

        """

        self.clicked.emit()
        super().mousePressEvent(event)

################################################################################