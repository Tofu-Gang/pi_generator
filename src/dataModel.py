__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QRectF, QPointF, Qt
from math import pi, sin
from src.triangleButton import TriangleButton
from src.generateButton import GenerateButton
from src.textItem import TextItem
from src.scaleTextItem import ScaleTextItem
from src.pi import PiGenerator



################################################################################

class DataModel(QGraphicsScene):
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
        self._generator = PiGenerator()
        self.setSceneRect(QRectF(QPointF(-self.SCENE_WIDTH/2, -self.SCENE_HEIGHT/2),
                                 QPointF(self.SCENE_WIDTH/2, self.SCENE_HEIGHT/2)))

        # scale type
        self.addItem(TextItem('Scale', TextItem.CENTER, self.SCALE_TYPE_LABEL_POS))
        scaleTypeLeftButton = TriangleButton(TriangleButton.LEFT)
        scaleTypeLeftButton.setPos(self.SCALE_TYPE_LEFT_BUTTON_POS)
        scaleTypeLeftButton.clicked.connect(self._generator.setPreviousScaleType)
        self.addItem(scaleTypeLeftButton)
        scaleTypeRightButton = TriangleButton(TriangleButton.RIGHT)
        scaleTypeRightButton.setPos(self.SCALE_TYPE_RIGHT_BUTTON_POS)
        scaleTypeRightButton.clicked.connect(self._generator.setNextScaleType)
        self.addItem(scaleTypeRightButton)

        self._scaleTypeSelectedTextItem = TextItem(self._generator.scaleType, TextItem.CENTER, self.SCALE_TYPE_CENTER_POS)
        self._scaleTypeLeftTextItem = TextItem(self._generator.previousScaleType, TextItem.LEFT, self.SCALE_TYPE_LEFT_POS)
        self._scaleTypeRightTextItem = TextItem(self._generator.nextScaleType, TextItem.RIGHT, self.SCALE_TYPE_RIGHT_POS)
        self.addItem(self._scaleTypeSelectedTextItem)
        self.addItem(self._scaleTypeLeftTextItem)
        self.addItem(self._scaleTypeRightTextItem)

        # root note
        rootNoteLeftButton = TriangleButton(TriangleButton.LEFT)
        rootNoteLeftButton.setPos(self.ROOT_NOTE_LEFT_BUTTON_POS)
        rootNoteLeftButton.clicked.connect(self._generator.setPreviousRootNote)
        self.addItem(rootNoteLeftButton)
        rootNoteRightButton = TriangleButton(TriangleButton.RIGHT)
        rootNoteRightButton.setPos(self.ROOT_NOTE_RIGHT_BUTTON_POS)
        rootNoteRightButton.clicked.connect(self._generator.setNextRootNote)
        self.addItem(rootNoteRightButton)

        self._rootNoteSelectedTextItem = TextItem(self._generator.rootNote, TextItem.CENTER, self.ROOT_NOTE_CENTER_POS)
        self._rootNoteLeftTextItem = TextItem(self._generator.previousRootNote, TextItem.LEFT, self.ROOT_NOTE_LEFT_POS)
        self._rootNoteRightTextItem = TextItem(self._generator.nextRootNote, TextItem.RIGHT, self.ROOT_NOTE_RIGHT_POS)
        self.addItem(self._rootNoteSelectedTextItem)
        self.addItem(self._rootNoteLeftTextItem)
        self.addItem(self._rootNoteRightTextItem)

        # scale
        self._scaleItem = ScaleTextItem()
        self._scaleItem.setScale(self._generator.scale)
        self._scaleItem.setPos(self.SCALE_POS)
        self.addItem(self._scaleItem)

        # solo length
        self._soloLengthLabelTextItem = TextItem('Solo length', TextItem.LEFT, self.SOLO_LENGTH_LABEL_POS)
        self.addItem(self._soloLengthLabelTextItem)
        self._soloLengthMaxLabelTextItem = TextItem('Max length: '+str(self._generator.maxSoloLength), TextItem.RIGHT, self.SOLO_LENGTH_MAX_POS)
        self.addItem(self._soloLengthMaxLabelTextItem)
        self._soloLengthTextItem = TextItem(str(self._generator.soloLength), TextItem.CENTER, self.SOLO_LENGTH_POS)
        self.addItem(self._soloLengthTextItem)
        soloLengthLeftButton = TriangleButton(TriangleButton.LEFT)
        soloLengthLeftButton.setPos(self.SOLO_LENGTH_LEFT_BUTTON_POS)
        soloLengthLeftButton.clicked.connect(self._generator.decreaseSoloLength)
        self.addItem(soloLengthLeftButton)
        soloLengthRightButton = TriangleButton(TriangleButton.RIGHT)
        soloLengthRightButton.setPos(self.SOLO_LENTGH_RIGHT_BUTTON_POS)
        soloLengthRightButton.clicked.connect(self._generator.increaseSoloLength)
        self.addItem(soloLengthRightButton)

        # generate button
        generateButton = GenerateButton()
        generateButton.setPos(self.GENERATE_BUTTON_POS)
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

        scaleTypeLeftButton.clicked.connect(self._updateTextItems)
        scaleTypeRightButton.clicked.connect(self._updateTextItems)
        rootNoteLeftButton.clicked.connect(self._updateTextItems)
        rootNoteRightButton.clicked.connect(self._updateTextItems)
        soloLengthLeftButton.clicked.connect(self._updateTextItems)
        soloLengthRightButton.clicked.connect(self._updateTextItems)
        generateButton.clicked.connect(self._updateTextItems)

################################################################################

    def _solo(self):
        """

        """

        solo = ''
        scale = self._generator.scale.split()[:-1]
        usedNumbers = self._generator.usedNumbers
        segment = self._generator.soloSegment()
        scaleMap = {}
        for i in range(len(usedNumbers)):
            scaleMap[usedNumbers[i]] = scale[i]
        for number in segment:
            solo += str(scaleMap[int(number)])
            solo += ' '
        return solo

################################################################################

    def _updateTextItems(self):
        """

        """

        self._scaleTypeSelectedTextItem.setPlainText(self._generator.scaleType)
        self._scaleTypeLeftTextItem.setPlainText(self._generator.previousScaleType)
        self._scaleTypeRightTextItem.setPlainText(self._generator.nextScaleType)
        self._rootNoteSelectedTextItem.setPlainText(self._generator.rootNote)
        self._rootNoteLeftTextItem.setPlainText(self._generator.previousRootNote)
        self._rootNoteRightTextItem.setPlainText(self._generator.nextRootNote)
        self._scaleItem.setScale(self._generator.scale)
        self._soloLengthTextItem.setPlainText(str(self._generator.soloLength))
        temp = self._soloLengthMaxLabelTextItem.toPlainText().split()
        temp[2] = str(self._generator.maxSoloLength)
        text = ''
        for part in temp:
            text += ' '
            text += part
        self._soloLengthMaxLabelTextItem.setPlainText(text)

        solo = self._solo().split()
        lines = [solo[i:i+self.SOLO_NOTES_PER_LINE] for i in range(0, len(solo), self.SOLO_NOTES_PER_LINE)]
        lines = [' '.join(line) for line in lines]
        for item in self._soloAreas[7]:
            item.setPlainText('')
        for i in range(len(lines)):
            self._soloAreas[len(lines)-1][i].setPlainText(lines[i])

################################################################################

    def drawBackground(self, painter, rect):
        """

        """

        painter.fillRect(rect, Qt.black)

################################################################################