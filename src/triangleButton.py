__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QGraphicsObject
from PyQt5.QtGui import QPainterPath, QPen, QBrush
from PyQt5.QtCore import pyqtSignal as Signal, QRectF, QPointF, Qt
from math import pi, sin
from random import randint



################################################################################

class TriangleButton(QGraphicsObject):
    LEFT = -1
    RIGHT = 1
    SIDE = 30
    H = SIDE * sin(60*pi/180)
    A_LEFT_DEFAULT = QPointF(H/2, -SIDE/2)
    A_RIGHT_DEFAULT = QPointF(-H/2, -SIDE/2)
    B_LEFT_DEFAULT = QPointF(H/2, SIDE/2)
    B_RIGHT_DEFAULT = QPointF(-H/2, SIDE/2)
    C_LEFT_DEFAULT = QPointF(-H/2, 0)
    C_RIGHT_DEFAULT = QPointF(H/2, 0)
    BOUNDING_RECT_LEFT_DEFAULT = QRectF(QPointF(C_LEFT_DEFAULT.x(), A_LEFT_DEFAULT.y()), B_LEFT_DEFAULT)
    BOUNDING_RECT_RIGHT_DEFAULT = QRectF(A_RIGHT_DEFAULT, QPointF(C_RIGHT_DEFAULT.x(), B_RIGHT_DEFAULT.y()))
    PEN_WIDTH_NORMAL = 3
    PEN_WIDTH_HOVER = 6
    clicked = Signal()

################################################################################

    def __init__(self, variation, parent=None):
        super().__init__(parent)
        self._variation = variation
        self.setAcceptHoverEvents(True)
        self._hover = False
        self._penMargin = self.PEN_WIDTH_NORMAL/2
        self._pen = QPen(QBrush(Qt.NoBrush), self.PEN_WIDTH_NORMAL, Qt.SolidLine, Qt.SquareCap, Qt.MiterJoin)
        self._pen.setColor(Qt.green)

        if self._variation == self.LEFT:
            self._boundingRect = self.BOUNDING_RECT_LEFT_DEFAULT
            self._shape = QPainterPath()
            self._shape.moveTo(self.A_LEFT_DEFAULT)
            self._shape.lineTo(self.B_LEFT_DEFAULT)
            self._shape.lineTo(self.C_LEFT_DEFAULT)
            self._shape.lineTo(self.A_LEFT_DEFAULT)
        elif self._variation == self.RIGHT:
            self._boundingRect = self.BOUNDING_RECT_RIGHT_DEFAULT
            self._shape = QPainterPath()
            self._shape.moveTo(self.A_RIGHT_DEFAULT)
            self._shape.lineTo(self.B_RIGHT_DEFAULT)
            self._shape.lineTo(self.C_RIGHT_DEFAULT)
            self._shape.lineTo(self.A_RIGHT_DEFAULT)
        else:
            self._boundingRect = None
            self._shape = None

################################################################################

    def paint(self, painter, option, widget):
        """

        """

        painter.setPen(self._pen)
        painter.drawPath(self._shape)

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
        if self._variation == self.LEFT:
            a = QPointF(self.H/2+randint(0, int(self.H/3)),
                        -self.SIDE/2-randint(0, int(self.SIDE/3)))
            b = QPointF(self.H/2+randint(0, int(self.H/3)),
                        self.SIDE/2+randint(0, int(self.SIDE/3)))
            c = QPointF(-self.H/2-randint(0, int(self.H/3)),
                        randint(-int(self.SIDE/6), int(self.SIDE/6)))
        elif self._variation == self.RIGHT:
            a = QPointF(-self.H/2-randint(0, int(self.H/3)),
                        -self.SIDE/2-randint(0, int(self.SIDE/3)))
            b = QPointF(-self.H/2-randint(0, int(self.H/3)),
                        self.SIDE/2+randint(0, int(self.SIDE/3)))
            c = QPointF(self.H/2+randint(0, int(self.H/3)),
                        randint(-int(self.SIDE/6), int(self.SIDE/6)))
        else:
            a = None
            b = None
            c = None
        self._boundingRect = QRectF(QPointF(min(a.x(), b.x(), c.x())-self._penMargin,
                                            min(a.y(), b.y(), c.y())-self._penMargin),
                                    QPointF(max(a.x(), b.x(), c.x())+self._penMargin,
                                            max(a.y(), b.y(), c.y())+self._penMargin))
        self._shape = QPainterPath()
        self._shape.moveTo(a)
        self._shape.lineTo(b)
        self._shape.lineTo(c)
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
        if self._variation == self.LEFT:
            self._boundingRect = self.BOUNDING_RECT_LEFT_DEFAULT
            a = self.A_LEFT_DEFAULT
            b = self.B_LEFT_DEFAULT
            c = self.C_LEFT_DEFAULT
        elif self._variation == self.RIGHT:
            self._boundingRect = self.BOUNDING_RECT_RIGHT_DEFAULT
            a = self.A_RIGHT_DEFAULT
            b = self.B_RIGHT_DEFAULT
            c = self.C_RIGHT_DEFAULT
        else:
            a = None
            b = None
            c = None
        self._shape = QPainterPath()
        self._shape.moveTo(a)
        self._shape.lineTo(b)
        self._shape.lineTo(c)
        self._shape.lineTo(a)
        super().hoverLeaveEvent(event)

################################################################################

    def mousePressEvent(self, event):
        """

        """

        self.clicked.emit()
        super().mousePressEvent(event)

################################################################################