__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QRectF, QPointF, Qt
from math import pi, sin
from random import randint
from src.scales import SCALE_TYPES, ROOT_NOTES, SCALES
from src.triangleButton import TriangleButton
from src.generateButton import GenerateButton
from src.textItem import TextItem
from src.scaleTextItem import ScaleTextItem



################################################################################

class DataModel(QGraphicsScene):
    SCALE_TYPE_DEFAULT_INDEX = 0
    ROOT_NOTE_DEFAULT_INDEX = 3

    SCENE_WIDTH = 798
    SCENE_HEIGHT = 598

    TRIANGLE_BUTTON_SIDE = 30
    TRIANGLE_BUTTON_H = TRIANGLE_BUTTON_SIDE*sin(60*pi/180)

    SCALE_TYPE_LEFT_BUTTON_POS = QPointF(-300, -SCENE_HEIGHT/2+SCENE_HEIGHT/10+SCENE_HEIGHT/20)
    SCALE_TYPE_RIGHT_BUTTON_POS = QPointF(300, -SCENE_HEIGHT/2+SCENE_HEIGHT/10+SCENE_HEIGHT/20)
    SCALE_TYPE_LABEL_POS = QPointF(0, -SCENE_HEIGHT/2+SCENE_HEIGHT/20)
    SCALE_TYPE_CENTER_POS = QPointF(0, -SCENE_HEIGHT/2+SCENE_HEIGHT/10+SCENE_HEIGHT/20)
    SCALE_TYPE_LEFT_POS = QPointF(SCALE_TYPE_LEFT_BUTTON_POS.x()+TRIANGLE_BUTTON_H, -SCENE_HEIGHT/2+SCENE_HEIGHT/10+SCENE_HEIGHT/20)
    SCALE_TYPE_RIGHT_POS = QPointF(SCALE_TYPE_RIGHT_BUTTON_POS.x()-TRIANGLE_BUTTON_H, -SCENE_HEIGHT/2+SCENE_HEIGHT/10+SCENE_HEIGHT/20)

    ROOT_NOTE_LEFT_BUTTON_POS = QPointF(-150, -SCENE_HEIGHT/2+SCENE_HEIGHT/5+SCENE_HEIGHT/20)
    ROOT_NOTE_RIGHT_BUTTON_POS = QPointF(150, -SCENE_HEIGHT/2+SCENE_HEIGHT/5+SCENE_HEIGHT/20)
    ROOT_NOTE_CENTER_POS = QPointF(0, -SCENE_HEIGHT/2+SCENE_HEIGHT/5+SCENE_HEIGHT/20)
    ROOT_NOTE_LEFT_POS = QPointF(ROOT_NOTE_LEFT_BUTTON_POS.x()+TRIANGLE_BUTTON_H, -SCENE_HEIGHT/2+SCENE_HEIGHT/5+SCENE_HEIGHT/20)
    ROOT_NOTE_RIGHT_POS = QPointF(ROOT_NOTE_RIGHT_BUTTON_POS.x()-TRIANGLE_BUTTON_H, -SCENE_HEIGHT/2+SCENE_HEIGHT/5+SCENE_HEIGHT/20)
    SCALE_POS = QPointF(0, -SCENE_HEIGHT/2+3*SCENE_HEIGHT/10+SCENE_HEIGHT/20)

    SOLO_LENGTH_LABEL_POS = QPointF(-200, -SCENE_HEIGHT/10+SCENE_HEIGHT/20)
    SOLO_LENGTH_MAX_POS = QPointF(220, -SCENE_HEIGHT/10+SCENE_HEIGHT/20)
    SOLO_LENGTH_LEFT_BUTTON_POS = QPointF(-50, -SCENE_HEIGHT/10+SCENE_HEIGHT/20)
    SOLO_LENTGH_RIGHT_BUTTON_POS = QPointF(50, -SCENE_HEIGHT/10+SCENE_HEIGHT/20)
    SOLO_LENGTH_POS = QPointF(0, -SCENE_HEIGHT/10+SCENE_HEIGHT/20)

    GENERATE_BUTTON_POS = QPointF(0, SCENE_HEIGHT/20)
    SOLO_NOTES_PER_LINE = 18
    SOLO_POS_1 = QPointF(0, SCENE_HEIGHT/10+SCENE_HEIGHT/40)
    SOLO_POS_2 = QPointF(0, SCENE_HEIGHT/10+SCENE_HEIGHT/20+SCENE_HEIGHT/40)
    SOLO_POS_3 = QPointF(0, SCENE_HEIGHT/5+SCENE_HEIGHT/40)
    SOLO_POS_4 = QPointF(0, SCENE_HEIGHT/5+SCENE_HEIGHT/20+SCENE_HEIGHT/40)
    SOLO_POS_5 = QPointF(0, 3*SCENE_HEIGHT/10+SCENE_HEIGHT/40)
    SOLO_POS_6 = QPointF(0, 3*SCENE_HEIGHT/10+SCENE_HEIGHT/20+SCENE_HEIGHT/40)
    SOLO_POS_7 = QPointF(0, 2*SCENE_HEIGHT/5+SCENE_HEIGHT/40)
    SOLO_POS_8 = QPointF(0, 2*SCENE_HEIGHT/5+SCENE_HEIGHT/20+SCENE_HEIGHT/40)

################################################################################

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSceneRect(QRectF(QPointF(-self.SCENE_WIDTH/2, -self.SCENE_HEIGHT/2),
                                 QPointF(self.SCENE_WIDTH/2, self.SCENE_HEIGHT/2)))
        self._scaleTypeIndex = self.SCALE_TYPE_DEFAULT_INDEX
        self._rootNoteIndex = self.ROOT_NOTE_DEFAULT_INDEX
        self._soloLength = int(self._maxSoloLength()/2)
        self._solo = None

        # scale type
        self.addItem(TextItem('Scale', TextItem.CENTER, self.SCALE_TYPE_LABEL_POS))

        scaleTypeLeftButton = TriangleButton(TriangleButton.LEFT)
        scaleTypeLeftButton.setPos(self.SCALE_TYPE_LEFT_BUTTON_POS)
        scaleTypeLeftButton.clicked.connect(self._scaleTypeLeftButtonWasClicked)
        self.addItem(scaleTypeLeftButton)
        scaleTypeRightButton = TriangleButton(TriangleButton.RIGHT)
        scaleTypeRightButton.setPos(self.SCALE_TYPE_RIGHT_BUTTON_POS)
        scaleTypeRightButton.clicked.connect(self._scaleTypeRightButtonWasClicked)
        self.addItem(scaleTypeRightButton)

        self._scaleTypeSelectedTextItem = TextItem(SCALE_TYPES[self._scaleTypeIndex], TextItem.CENTER, self.SCALE_TYPE_CENTER_POS)
        self._scaleTypeLeftTextItem = TextItem(SCALE_TYPES[(self._scaleTypeIndex-1)%len(SCALE_TYPES)],
                                               TextItem.LEFT, self.SCALE_TYPE_LEFT_POS)
        self._scaleTypeRightTextItem = TextItem(SCALE_TYPES[(self._scaleTypeIndex+1)%len(SCALE_TYPES)],
                                                TextItem.RIGHT, self.SCALE_TYPE_RIGHT_POS)
        self.addItem(self._scaleTypeSelectedTextItem)
        self.addItem(self._scaleTypeLeftTextItem)
        self.addItem(self._scaleTypeRightTextItem)

        # root note
        rootNoteLeftButton = TriangleButton(TriangleButton.LEFT)
        rootNoteLeftButton.setPos(self.ROOT_NOTE_LEFT_BUTTON_POS)
        rootNoteLeftButton.clicked.connect(self._rootNoteLeftButtonWasClicked)
        self.addItem(rootNoteLeftButton)
        rootNoteRightButton = TriangleButton(TriangleButton.RIGHT)
        rootNoteRightButton.setPos(self.ROOT_NOTE_RIGHT_BUTTON_POS)
        rootNoteRightButton.clicked.connect(self._rootNoteRightButtonWasClicked)
        self.addItem(rootNoteRightButton)

        self._rootNoteSelectedTextItem = TextItem(ROOT_NOTES[self._rootNoteIndex],
                                                  TextItem.CENTER, self.ROOT_NOTE_CENTER_POS)
        self._rootNoteLeftTextItem = TextItem(ROOT_NOTES[(self._rootNoteIndex-1)%len(ROOT_NOTES)],
                                              TextItem.LEFT, self.ROOT_NOTE_LEFT_POS)
        self._rootNoteRightTextItem = TextItem(ROOT_NOTES[(self._rootNoteIndex+1)%len(ROOT_NOTES)],
                                               TextItem.RIGHT, self.ROOT_NOTE_RIGHT_POS)
        self.addItem(self._rootNoteSelectedTextItem)
        self.addItem(self._rootNoteLeftTextItem)
        self.addItem(self._rootNoteRightTextItem)

        # scale
        self._scaleItem = ScaleTextItem()
        self._scaleItem.setPos(self.SCALE_POS)
        self.addItem(self._scaleItem)

        # solo length
        self._soloLengthLabelTextItem = TextItem('Solo length', TextItem.LEFT, self.SOLO_LENGTH_LABEL_POS)
        self.addItem(self._soloLengthLabelTextItem)
        self._soloLengthMaxLabelTextItem = TextItem('Max length: '+str(self._maxSoloLength()), TextItem.RIGHT, self.SOLO_LENGTH_MAX_POS)
        self.addItem(self._soloLengthMaxLabelTextItem)
        self._soloLengthTextItem = TextItem(str(self._soloLength), TextItem.CENTER, self.SOLO_LENGTH_POS)
        self.addItem(self._soloLengthTextItem)
        self._soloLengthLeftButton = TriangleButton(TriangleButton.LEFT)
        self._soloLengthLeftButton.setPos(self.SOLO_LENGTH_LEFT_BUTTON_POS)
        self._soloLengthLeftButton.clicked.connect(self._soloLengthLeftButtonWasClicked)
        self.addItem(self._soloLengthLeftButton)
        self._soloLengthRightButton = TriangleButton(TriangleButton.RIGHT)
        self._soloLengthRightButton.setPos(self.SOLO_LENTGH_RIGHT_BUTTON_POS)
        self._soloLengthRightButton.clicked.connect(self._soloLengthRightButtonWasClicked)
        self.addItem(self._soloLengthRightButton)

        # generate button
        generateButton = GenerateButton()
        generateButton.setPos(self.GENERATE_BUTTON_POS)
        generateButton.clicked.connect(self._generateSolo)
        self.addItem(generateButton)

        # solo
        self._soloTextItem1 = TextItem('', TextItem.CENTER, self.SOLO_POS_1)
        self.addItem(self._soloTextItem1)
        self._soloTextItem2 = TextItem('', TextItem.CENTER, self.SOLO_POS_2)
        self.addItem(self._soloTextItem2)
        self._soloTextItem3 = TextItem('', TextItem.CENTER, self.SOLO_POS_3)
        self.addItem(self._soloTextItem3)
        self._soloTextItem4 = TextItem('', TextItem.CENTER, self.SOLO_POS_4)
        self.addItem(self._soloTextItem4)
        self._soloTextItem5 = TextItem('', TextItem.CENTER, self.SOLO_POS_5)
        self.addItem(self._soloTextItem5)
        self._soloTextItem6 = TextItem('', TextItem.CENTER, self.SOLO_POS_6)
        self.addItem(self._soloTextItem6)
        self._soloTextItem7 = TextItem('', TextItem.CENTER, self.SOLO_POS_7)
        self.addItem(self._soloTextItem7)
        self._soloTextItem8 = TextItem('', TextItem.CENTER, self.SOLO_POS_8)
        self.addItem(self._soloTextItem8)
        self._soloAreas = ((self._soloTextItem3,),
                           (self._soloTextItem3, self._soloTextItem4),
                           (self._soloTextItem3, self._soloTextItem4,
                            self._soloTextItem5),
                           (self._soloTextItem2, self._soloTextItem3,
                            self._soloTextItem4, self._soloTextItem5),
                           (self._soloTextItem2, self._soloTextItem3,
                            self._soloTextItem4, self._soloTextItem5,
                            self._soloTextItem6),
                           (self._soloTextItem2, self._soloTextItem3,
                            self._soloTextItem4, self._soloTextItem5,
                            self._soloTextItem6, self._soloTextItem7),
                           (self._soloTextItem1, self._soloTextItem2,
                            self._soloTextItem3, self._soloTextItem4,
                            self._soloTextItem5, self._soloTextItem6,
                            self._soloTextItem7),
                           (self._soloTextItem1, self._soloTextItem2,
                            self._soloTextItem3, self._soloTextItem4,
                            self._soloTextItem5, self._soloTextItem6,
                            self._soloTextItem7, self._soloTextItem8))
        self._generateSolo()

################################################################################

    def _scaleTypeLeftButtonWasClicked(self):
        """

        """

        self._scaleTypeIndex = (self._scaleTypeIndex-1)%len(SCALE_TYPES)
        self._updateTextItems()

################################################################################

    def _scaleTypeRightButtonWasClicked(self):
        """

        """

        self._scaleTypeIndex = (self._scaleTypeIndex+1)%len(SCALE_TYPES)
        self._updateTextItems()

################################################################################

    def _rootNoteLeftButtonWasClicked(self):
        """

        """

        self._rootNoteIndex = (self._rootNoteIndex-1)%len(ROOT_NOTES)
        self._updateTextItems()

################################################################################

    def _rootNoteRightButtonWasClicked(self):
        """

        """

        self._rootNoteIndex = (self._rootNoteIndex+1)%len(ROOT_NOTES)
        self._updateTextItems()

################################################################################

    def _soloLengthLeftButtonWasClicked(self):
        """

        """

        if self._soloLength > 1:
            self._soloLength -= 1
        else:
            self._soloLength = self._maxSoloLength()
        self._updateTextItems()

################################################################################

    def _soloLengthRightButtonWasClicked(self):
        """

        """

        if self._soloLength < self._maxSoloLength():
            self._soloLength += 1
        else:
            self._soloLength = 1
        self._updateTextItems()

################################################################################

    def _generateSolo(self):
        """

        """

        self._solo = ''
        scale = SCALES[self._scaleTypeIndex][self._rootNoteIndex].split()[:-1]
        notesCount = len(scale)
        numbers = [i for i in range(10)]
        scaleMap = {}

        for _ in range(10-notesCount):
            number = randint(0, 9)
            while number not in numbers:
                number = randint(0, 9)
            numbers.remove(number)

        for i in range(len(numbers)):
            scaleMap[numbers[i]] = scale[i]

        for i in range(self._soloLength):
            number = randint(0, 9)
            while number not in numbers:
                number = randint(0, 9)
            self._solo += scaleMap[number]
            self._solo += ' '
        self._updateTextItems()

################################################################################

    def _updateTextItems(self):
        """

        """

        self._scaleTypeSelectedTextItem.setPlainText(SCALE_TYPES[self._scaleTypeIndex])
        self._scaleTypeLeftTextItem.setPlainText(SCALE_TYPES[(self._scaleTypeIndex-1)%len(SCALE_TYPES)])
        self._scaleTypeRightTextItem.setPlainText(SCALE_TYPES[(self._scaleTypeIndex+1)%len(SCALE_TYPES)])
        self._rootNoteSelectedTextItem.setPlainText(ROOT_NOTES[self._rootNoteIndex])
        self._rootNoteLeftTextItem.setPlainText(ROOT_NOTES[(self._rootNoteIndex-1)%len(ROOT_NOTES)])
        self._rootNoteRightTextItem.setPlainText(ROOT_NOTES[(self._rootNoteIndex+1)%len(ROOT_NOTES)])
        self._scaleItem.setScale(SCALES[self._scaleTypeIndex][self._rootNoteIndex])
        self._soloLengthTextItem.setPlainText(str(self._soloLength))
        temp = self._soloLengthMaxLabelTextItem.toPlainText().split()
        temp[2] = str(self._maxSoloLength())
        text = ''
        for part in temp:
            text += ' '
            text += part
        self._soloLengthMaxLabelTextItem.setPlainText(text)

        solo = self._solo.split()
        lines = [solo[i:i+self.SOLO_NOTES_PER_LINE] for i in range(0, len(solo), self.SOLO_NOTES_PER_LINE)]
        lines = [' '.join(line) for line in lines]
        for item in self._soloAreas[7]:
            item.setPlainText('')
        for i in range(len(lines)):
            self._soloAreas[len(lines)-1][i].setPlainText(lines[i])

################################################################################

    def _maxSoloLength(self):
        """

        """

        # TODO: not implemented yet
        return 128

################################################################################

    def drawBackground(self, painter, rect):
        """

        """

        painter.fillRect(rect, Qt.black)

################################################################################