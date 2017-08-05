__author__ = 'Tofu Gang'

from PyQt5.QtWidgets import QGraphicsScene, QGraphicsObject, QGraphicsTextItem, \
    QGraphicsItem
from PyQt5.QtGui import QPainterPath, QPen, QFont
from PyQt5.QtCore import pyqtSignal as Signal, QRectF, QPointF, Qt
from math import pi, sin
from random import randint



################################################################################

class DataModel(QGraphicsScene):
    SCALE_MAJOR = 'Major'
    SCALE_PENTATONIC_MINOR = 'Pentatonic Minor'
    SCALE_BLUES = 'Blues'
    SCALE_PENTATONIC_MAJOR = 'Pentatonic Major'
    SCALE_NATURAL_MINOR = 'Natural Minor'
    SCALE_HARMONIC_MINOR = 'Harmonic Minor'
    SCALE_MELODIC_MINOR_ASC = 'Melodic Minor (asc)'
    SCALE_MELODIC_MINOR_DESC = 'Melodic Minor (desc)'
    SCALE_DORIAN = 'Dorian'
    SCALE_PHRYGIAN = 'Phrygian'
    SCALE_LYDIAN = 'Lydian'
    SCALE_MIXOLYDIAN = 'Mixolydian'
    SCALE_LOCRIAN = 'Locrian'
    SCALE_ARABIC = 'Arabic'
    SCALE_HUNGARIAN_GYPSY = 'Hungarian Gypsy'
    SCALE_WHOLE_TONE = 'Whole Tone'
    SCALE_AUGMENTED = 'Augmented'
    SCALE_PHRYGIAN_DOMINANT = 'Phrygian Dominant'

    SCALE_TYPES = (SCALE_MAJOR,
                   SCALE_PENTATONIC_MINOR,
                   SCALE_BLUES,
                   SCALE_PENTATONIC_MAJOR,
                   SCALE_NATURAL_MINOR,
                   SCALE_HARMONIC_MINOR,
                   SCALE_MELODIC_MINOR_ASC,
                   SCALE_MELODIC_MINOR_DESC,
                   SCALE_DORIAN,
                   SCALE_PHRYGIAN,
                   SCALE_LYDIAN,
                   SCALE_MIXOLYDIAN,
                   SCALE_LOCRIAN,
                   SCALE_ARABIC,
                   SCALE_HUNGARIAN_GYPSY,
                   SCALE_WHOLE_TONE,
                   SCALE_AUGMENTED,
                   SCALE_PHRYGIAN_DOMINANT)
    SCALE_TYPE_DEFAULT_INDEX = 0

    ROOT_NOTE_A = 'A'
    ROOT_NOTE_AshBb = 'A#/Bb'
    ROOT_NOTE_B = 'B'
    ROOT_NOTE_C = 'C'
    ROOT_NOTE_CshDb = 'C#/Db'
    ROOT_NOTE_D = 'D'
    ROOT_NOTE_DshEb = 'D#/Eb'
    ROOT_NOTE_E = 'E'
    ROOT_NOTE_F = 'F'
    ROOT_NOTE_FshGb = 'F#/Gb'
    ROOT_NOTE_G = 'G'
    ROOT_NOTE_GshAb = 'G#/Ab'

    ROOT_NOTES = (ROOT_NOTE_A,
                  ROOT_NOTE_AshBb,
                  ROOT_NOTE_B,
                  ROOT_NOTE_C,
                  ROOT_NOTE_CshDb,
                  ROOT_NOTE_D,
                  ROOT_NOTE_DshEb,
                  ROOT_NOTE_E,
                  ROOT_NOTE_F,
                  ROOT_NOTE_FshGb,
                  ROOT_NOTE_G,
                  ROOT_NOTE_GshAb)
    ROOT_NOTE_DEFAULT_INDEX = 3

    SCALES = (('A B C# D E F# G# A', # major
               'Bb C D Eb F G A Bb',
               'B C# D# E F# G# A# B',
               'C D E F G A B C',
               'Db Eb F Gb Ab Bb C Db',
               'D E F# G A B C# D',
               'Eb F G Ab Bb C D Eb',
               'E F# G# A B C# D# E',
               'F G A Bb C D E F',
               'F# G# A# B C# F F#',
               'G A B C D E F# G',
               'Ab Bb C Db Eb F G Ab'),
              ('A C D E G A', # pentatonic minor
               'Bb Db Eb F Ab Bb',
               'B D E F# A B',
               'C Eb F G Bb C',
               'C# E F# G# B C#',
               'D F G A C D',
               'D# F# G# A# C# D#',
               'E G A B D E',
               'F Ab Bb C Eb F',
               'F# A B C# E F#',
               'G Bb C D F G',
               'G# B C# D# F# G#'),
              ('A C D D# E G A', # blues
               'A# C# D# E F G# A#',
               'B D E F F# A B',
               'C Eb F Gb G Bb C',
               'C# E F# G G# B C#',
               'D F G G# A C D',
               'D# F# G# A A# C# D#',
               'E G A A# B D E',
               'F G# A# B C D# F',
               'F# A B C C# E F#',
               'G Bb C Db D F G',
               'G# B C# D D# F# G#'),
              ('A B C# E F# A', # pentatonic major
               'Bb C D F G Bb',
               'B C# D# F# G# B',
               'C D E G A C',
               'Db Eb F Ab Bb Db',
               'D E F# A B D',
               'Eb F G Bb C Eb',
               'E F# G# B C# E',
               'F G A C D F',
               'F# G# A# C# D# F#',
               'G A B D E G',
               'Ab Bb C Eb F Ab'),
              ('A B C D E F G A', # natural minor
               'Bb C Db Eb F Gb Ab Bb',
               'B C# D E F# G A B',
               'C D Eb F G Ab Bb C',
               'C# D# E F# G# A B C#',
               'D E F G A Bb C D',
               'D# F F# G# A# B C# D#',
               'E F# G A B C D E',
               'F G Ab Bb C Db Eb F',
               'F# G# A B C# D E F#',
               'G A Bb C D Eb F G',
               'G# A# B C# D# E F# G#'),
              ('A B C D E F G# A', # harmonic minor
               'Bb C Db Eb F Gb A Bb',
               'B C# D E F# G A# B',
               'C D Eb F G Ab B C',
               'C# D# E F# G# A C C#',
               'D E F G A A# C# D',
               'Eb F Gb Ab Bb B D Eb',
               'E F# G A B C D# E',
               'F G Ab Bb C Db E F',
               'F# G# A B C# D F F#',
               'G A Bb C D Eb Gb G',
               'G# A# B C# D# E G G#'),
              ('A B C D E F# G# A', # melodic minor (asc)
               'Bb C Db Eb F G A Bb',
               'B C# D E F# G# A# B',
               'C D Eb F G A B C',
               'C# D# E F# G# A# C C#',
               'D E F G A B C# D',
               'Eb F Gb Ab Bb C D Eb',
               'E F# G A B C# D# E',
               'F G Ab Bb C D E F',
               'F# G# A B C# D# F F#',
               'G A A# C D E F# G',
               'G# A# B C# D# F G G#'),
              ('A B C D E F G A', # melodic minor (desc)
               'Bb C Db Eb F Gb Ab Bb',
               'B C# D E F# G A B',
               'C D Eb F G Ab Bb C',
               'C# D# E F# G# A B C#',
               'D E F G A Bb C D',
               'D# F F# G# A# B C# D#',
               'E F# G A B C D E',
               'F G Ab Bb C Db Eb F',
               'F# G# A B C# D E F#',
               'G A Bb C D Eb F G',
               'G# A# B C# D# E F# G#'),
              ('A B C D E F# G A', # dorian
               'Bb C Db Eb F G Ab Bb',
               'B C# D E F# G# A B',
               'C D Eb F G A Bb C',
               'C# D# E F# G# A# B C#',
               'D E F G A B C D',
               'Eb F Gb Ab Bb C Db Eb',
               'E F# G A B C# D E',
               'F G Ab Bb C D Eb F',
               'F# G# A B C# D# E F#',
               'G A Bb C D E F G',
               'G# A# B C# D# F F# G#'),
              ('A Bb C D E F G A', # phrygian
               'A# B C# D# F F# G# A#',
               'B C D E F# G A B',
               'C Db Eb F G Ab Bb C',
               'C# D E F# G# A B C#',
               'D Eb F G A Bb C D',
               'D# E F# G# A# B C# D#',
               'E F G A B C D E',
               'F Gb Ab Bb C Db Eb F',
               'F# G A B C# D E F#',
               'G Ab Bb C D Eb F G',
               'G# A B C# D# E F# G#'),
              ('A B C# D# E F# G# A', # lydian
               'Bb C D E F G A Bb',
               'B C# D# F F# G# A# B',
               'C D E F# G A B C',
               'Db Eb F G Ab Bb C Db',
               'D E F# G# A B C# D',
               'Eb F G A Bb C D Eb',
               'E F# G# A# B C# D# E',
               'F G A B C D E F',
               'Gb Ab Bb C Db Eb F Gb',
               'G A B C# D E F# G',
               'Ab Bb C D Eb F G Ab'),
              ('A B C# D E F# G A', # mixolydian
               'Bb C D Eb F G Ab Bb',
               'B C# D# E F# G# A B',
               'C D E F G A Bb C',
               'C# D# F F# G# A# B C#',
               'D E F# G A B C D',
               'Eb F G Ab Bb C Db Eb',
               'E F# G# A B C# D E',
               'F G A Bb C D Eb F',
               'F# G# A# B C# D# E F#',
               'G A B C D E F G',
               'Ab Bb C Db Eb F Gb Ab'),
              ('A Bb C D Eb F G A', # locrian
               'A# B C# D# E F# G# A#',
               'B C D E F G A B',
               'C Db Eb F Gb Ab Bb C',
               'C# D E F# G A B C#',
               'D Eb F G Ab Bb C D',
               'D# E F# G# A B C# D#',
               'E F G A Bb C D E',
               'F F# G# A# B C# D# F',
               'F# G A B C D E F#',
               'G Ab Bb C Db Eb F G',
               'G# A B C# D E F# G#'),
              ('A A# C# D E F G# A', # arabic
               'Bb B D Eb F Gb A Bb',
               'B C D# E F# G A# B',
               'C Db E F G Ab B C',
               'C# D F F# G# A C C#',
               'D D# F# G A A# C# D',
               'D# E G G# A# B D D#',
               'E F G# A B C D# E',
               'F Gb A Bb C Db E F',
               'F# G A# B C# D F F#',
               'G G# B C D D# F# G',
               'G# A C C# D# E G G#'),
              ('A B C D# E F G# A', # hungarian gypsy
               'Bb C Db E F Gb A Bb',
               'B C# D F F# G A# B',
               'C D D# F# G G# B C',
               'C# D# E G G# A C C#',
               'D E F G# A A# C# D',
               'Eb F Gb A Bb B D Eb',
               'E F# G A# B C D# E',
               'F G Ab B C Db E F',
               'F# G# A C D# D F F#',
               'G A A# C# D D# F# G',
               'G# A# B D D# E G G#'),
              ('A B C# D# F G A', # whole tone
               'A# C D E F# G# A#',
               'B C# D# F G A B',
               'C D E F# G# A# C',
               'C# D# F G A B C#',
               'D E F# G# A# C D',
               'D# F G A B C# D#',
               'E F# G# A# C D E',
               'F G A B C# D# F',
               'F# G# A# C D E F#',
               'G A B C# D# F G',
               'G# A# C D E F# G#'),
              ('A C Db E F Ab A', # augmented
               'A# C# D F F# A A#',
               'B D D# F# G A# B',
               'C D# E G G# B C',
               'Db E F Ab A C Db',
               'D F F# A A# C# D',
               'D# F# G A# B D D#',
               'E G G# B C D# E',
               'F Ab A C Db E F',
               'F# A A# C# D F F#',
               'G A# B D D# F# G',
               'G# B C D# E G G#'),
              ('A A# C# D E F G A', # phrygian dominant
               'Bb B D Eb F Gb Ab Bb',
               'B C D# E F# G A B',
               'C Db E F G Ab Bb C',
               'C# D F F# G# A B C#',
               'D Eb Gb G A Bb C D',
               'D# E G G# A# B C# D#',
               'E F G# A B C D E',
               'F Gb A Bb C Db Eb F',
               'F# G A# B C# D E F#',
               'G Ab B C D Eb F G',
               'G# A C C# D# E F# G#'))

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
        self._solo = ''

        # scale type
        self._scaleTypeLabelTextItem = TextItem('Scale', TextItem.CENTER, self.SCALE_TYPE_LABEL_POS)
        self.addItem(self._scaleTypeLabelTextItem)

        self._scaleTypeLeftButton = TriangleButton(TriangleButton.LEFT)
        self._scaleTypeLeftButton.setPos(self.SCALE_TYPE_LEFT_BUTTON_POS)
        self._scaleTypeLeftButton.clicked.connect(self._scaleTypeLeftButtonWasClicked)
        self.addItem(self._scaleTypeLeftButton)
        self._scaleTypeRightButton = TriangleButton(TriangleButton.RIGHT)
        self._scaleTypeRightButton.setPos(self.SCALE_TYPE_RIGHT_BUTTON_POS)
        self._scaleTypeRightButton.clicked.connect(self._scaleTypeRightButtonWasClicked)
        self.addItem(self._scaleTypeRightButton)

        self._scaleTypeSelectedTextItem = TextItem(self.SCALE_TYPES[self._scaleTypeIndex], TextItem.CENTER, self.SCALE_TYPE_CENTER_POS)
        self._scaleTypeLeftTextItem = TextItem(self.SCALE_TYPES[(self._scaleTypeIndex-1)%len(self.SCALE_TYPES)],
                                               TextItem.LEFT, self.SCALE_TYPE_LEFT_POS)
        self._scaleTypeRightTextItem = TextItem(self.SCALE_TYPES[(self._scaleTypeIndex+1)%len(self.SCALE_TYPES)],
                                                TextItem.RIGHT, self.SCALE_TYPE_RIGHT_POS)
        self.addItem(self._scaleTypeSelectedTextItem)
        self.addItem(self._scaleTypeLeftTextItem)
        self.addItem(self._scaleTypeRightTextItem)

        # root note
        self._rootNoteLeftButton = TriangleButton(TriangleButton.LEFT)
        self._rootNoteLeftButton.setPos(self.ROOT_NOTE_LEFT_BUTTON_POS)
        self._rootNoteLeftButton.clicked.connect(self._rootNoteLeftButtonWasClicked)
        self.addItem(self._rootNoteLeftButton)
        self._rootNoteRightButton = TriangleButton(TriangleButton.RIGHT)
        self._rootNoteRightButton.setPos(self.ROOT_NOTE_RIGHT_BUTTON_POS)
        self._rootNoteRightButton.clicked.connect(self._rootNoteRightButtonWasClicked)
        self.addItem(self._rootNoteRightButton)

        self._rootNoteSelectedTextItem = TextItem(self.ROOT_NOTES[self._rootNoteIndex], TextItem.CENTER, self.ROOT_NOTE_CENTER_POS)
        self._rootNoteLeftTextItem = TextItem(self.ROOT_NOTES[(self._rootNoteIndex-1)%len(self.ROOT_NOTES)],
                                              TextItem.LEFT, self.ROOT_NOTE_LEFT_POS)
        self._rootNoteRightTextItem = TextItem(self.ROOT_NOTES[(self._rootNoteIndex+1)%len(self.ROOT_NOTES)],
                                               TextItem.RIGHT, self.ROOT_NOTE_RIGHT_POS)
        self.addItem(self._rootNoteSelectedTextItem)
        self.addItem(self._rootNoteLeftTextItem)
        self.addItem(self._rootNoteRightTextItem)

        # scale
        self._scaleItem = ScaleTextItem(self.SCALES[self._scaleTypeIndex][self._rootNoteIndex])
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
        self._generateButton = RectButton()
        self._generateButton.setPos(self.GENERATE_BUTTON_POS)
        self._generateButton.clicked.connect(self._generateSolo)
        self.addItem(self._generateButton)

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
        self._generateSolo()

################################################################################

    def _scaleTypeLeftButtonWasClicked(self):
        """

        """

        self._scaleTypeIndex = (self._scaleTypeIndex-1)%len(self.SCALE_TYPES)
        self._updateTextItems()

################################################################################

    def _scaleTypeRightButtonWasClicked(self):
        """

        """

        self._scaleTypeIndex = (self._scaleTypeIndex+1)%len(self.SCALE_TYPES)
        self._updateTextItems()

################################################################################

    def _rootNoteLeftButtonWasClicked(self):
        """

        """

        self._rootNoteIndex = (self._rootNoteIndex-1)%len(self.ROOT_NOTES)
        self._updateTextItems()

################################################################################

    def _rootNoteRightButtonWasClicked(self):
        """

        """

        self._rootNoteIndex = (self._rootNoteIndex+1)%len(self.ROOT_NOTES)
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
        scale = self.SCALES[self._scaleTypeIndex][self._rootNoteIndex].split()[:-1]
        notesCount = len(scale)
        excluded = []
        scaleMap = {}
        used = []
        for _ in range(10-notesCount):
            number = randint(0, 9)
            while number in excluded:
                number = randint(0, 9)
            excluded.append(number)
        for _ in range(len(scale)):
            number = randint(0, 9)
            while number in used or number in excluded:
                number = randint(0, 9)
            used.append(number)
        for i in range(len(scale)):
            scaleMap[used[i]] = scale[i]
        for i in range(self._soloLength):
            number = randint(0, 9)
            while number in excluded:
                number = randint(0, 9)
            self._solo += scaleMap[number]
            self._solo += ' '
        self._updateTextItems()

################################################################################

    def _updateTextItems(self):
        """

        """

        self._scaleTypeSelectedTextItem.setPlainText(self.SCALE_TYPES[self._scaleTypeIndex])
        self._scaleTypeLeftTextItem.setPlainText(self.SCALE_TYPES[(self._scaleTypeIndex-1)%len(self.SCALE_TYPES)])
        self._scaleTypeRightTextItem.setPlainText(self.SCALE_TYPES[(self._scaleTypeIndex+1)%len(self.SCALE_TYPES)])
        self._rootNoteSelectedTextItem.setPlainText(self.ROOT_NOTES[self._rootNoteIndex])
        self._rootNoteLeftTextItem.setPlainText(self.ROOT_NOTES[(self._rootNoteIndex-1)%len(self.ROOT_NOTES)])
        self._rootNoteRightTextItem.setPlainText(self.ROOT_NOTES[(self._rootNoteIndex+1)%len(self.ROOT_NOTES)])
        self._scaleItem.setScale(self.SCALES[self._scaleTypeIndex][self._rootNoteIndex])
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
        if len(lines) == 1:
            self._soloTextItem3.setPlainText(lines[0])
        elif len(lines) == 2:
            self._soloTextItem3.setPlainText(lines[0])
            self._soloTextItem4.setPlainText(lines[1])
        elif len(lines) == 3:
            self._soloTextItem3.setPlainText(lines[0])
            self._soloTextItem4.setPlainText(lines[1])
            self._soloTextItem5.setPlainText(lines[2])
        elif len(lines) == 4:
            self._soloTextItem2.setPlainText(lines[0])
            self._soloTextItem3.setPlainText(lines[1])
            self._soloTextItem4.setPlainText(lines[2])
            self._soloTextItem5.setPlainText(lines[3])
        elif len(lines) == 5:
            self._soloTextItem2.setPlainText(lines[0])
            self._soloTextItem3.setPlainText(lines[1])
            self._soloTextItem4.setPlainText(lines[2])
            self._soloTextItem5.setPlainText(lines[3])
            self._soloTextItem6.setPlainText(lines[4])
        elif len(lines) == 6:
            self._soloTextItem2.setPlainText(lines[0])
            self._soloTextItem3.setPlainText(lines[1])
            self._soloTextItem4.setPlainText(lines[2])
            self._soloTextItem5.setPlainText(lines[3])
            self._soloTextItem6.setPlainText(lines[4])
            self._soloTextItem7.setPlainText(lines[5])
        elif len(lines) == 7:
            self._soloTextItem1.setPlainText(lines[0])
            self._soloTextItem2.setPlainText(lines[1])
            self._soloTextItem3.setPlainText(lines[2])
            self._soloTextItem4.setPlainText(lines[3])
            self._soloTextItem5.setPlainText(lines[4])
            self._soloTextItem6.setPlainText(lines[5])
            self._soloTextItem7.setPlainText(lines[6])
        elif len(lines) == 8:
            self._soloTextItem1.setPlainText(lines[0])
            self._soloTextItem2.setPlainText(lines[1])
            self._soloTextItem3.setPlainText(lines[2])
            self._soloTextItem4.setPlainText(lines[3])
            self._soloTextItem5.setPlainText(lines[4])
            self._soloTextItem6.setPlainText(lines[5])
            self._soloTextItem7.setPlainText(lines[6])
            self._soloTextItem8.setPlainText(lines[7])
        else:
            pass

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



################################################################################

class TriangleButton(QGraphicsObject):
    LEFT = -1
    RIGHT = 1
    SIDE = 30
    H = SIDE * sin(60 * pi / 180)
    PEN_WIDTH_NORMAL = 3
    PEN_WIDTH_HOVER = 6
    clicked = Signal()

################################################################################

    def __init__(self, variation, parent=None):
        super().__init__(parent)
        self._variation = variation
        self.setAcceptHoverEvents(True)
        self._hover = False
        if self._variation == self.LEFT:
            self._a =  QPointF(self.H/2, -self.SIDE/2)
            self._b = QPointF(self.H/2, self.SIDE/2)
            self._c = QPointF(-self.H/2, 0)
        elif self._variation == self.RIGHT:
            self._a = QPointF(-self.H/2, -self.SIDE/2)
            self._b = QPointF(-self.H/2, self.SIDE/2)
            self._c = QPointF(self.H/2, 0)

################################################################################

    def paint(self, painter, option, widget):
        """

        """

        pen = QPen(Qt.green)
        pen.setJoinStyle(Qt.MiterJoin)
        if self._hover:
            pen.setWidth(self.PEN_WIDTH_HOVER)
            painter.setPen(pen)
        else:
            pen.setWidth(self.PEN_WIDTH_NORMAL)
            painter.setPen(pen)
        painter.drawPath(self.shape())

################################################################################

    def boundingRect(self):
        """

        """

        if self._hover:
            penMargin = self.PEN_WIDTH_HOVER/2
        else:
            penMargin = self.PEN_WIDTH_NORMAL/2
        return QRectF(QPointF(min(self._a.x(), self._b.x(), self._c.x())-penMargin,
                              min(self._a.y(), self._b.y(), self._c.y())-penMargin),
                      QPointF(max(self._a.x(), self._b.x(), self._c.x())+penMargin,
                              max(self._a.y(), self._b.y(), self._c.y())+penMargin))

################################################################################

    def shape(self):
        """

        """

        shape = QPainterPath()
        shape.moveTo(self._a)
        shape.lineTo(self._b)
        shape.lineTo(self._c)
        shape.lineTo(self._a)
        return shape

################################################################################

    def hoverEnterEvent(self, event):
        """

        """

        self.prepareGeometryChange()
        self._hover = True
        if self._variation == self.LEFT:
            self._a =  QPointF(self.H/2+randint(0, int(self.H/3)),
                               -self.SIDE/2-randint(0, int(self.SIDE/3)))
            self._b = QPointF(self.H/2+randint(0, int(self.H/3)),
                              self.SIDE/2+randint(0, int(self.SIDE/3)))
            self._c = QPointF(-self.H/2-randint(0, int(self.H/3)),
                              randint(-int(self.SIDE/6), int(self.SIDE/6)))
        elif self._variation == self.RIGHT:
            self._a = QPointF(-self.H/2-randint(0, int(self.H/3)),
                              -self.SIDE/2-randint(0, int(self.SIDE/3)))
            self._b = QPointF(-self.H/2-randint(0, int(self.H/3)),
                              self.SIDE/2+randint(0, int(self.SIDE/3)))
            self._c = QPointF(self.H/2+randint(0, int(self.H/3)),
                              randint(-int(self.SIDE/6), int(self.SIDE/6)))
        else:
            pass
        super().hoverEnterEvent(event)

################################################################################

    def hoverLeaveEvent(self, event):
        """

        """

        self.prepareGeometryChange()
        self._hover = False
        if self._variation == self.LEFT:
            self._a =  QPointF(self.H/2, -self.SIDE/2)
            self._b = QPointF(self.H/2, self.SIDE/2)
            self._c = QPointF(-self.H/2, 0)
        elif self._variation == self.RIGHT:
            self._a = QPointF(-self.H/2, -self.SIDE/2)
            self._b = QPointF(-self.H/2, self.SIDE/2)
            self._c = QPointF(self.H/2, 0)
        else:
            pass
        super().hoverLeaveEvent(event)

################################################################################

    def mousePressEvent(self, event):
        """

        """

        self.clicked.emit()
        super().mousePressEvent(event)

################################################################################



################################################################################

class RectButton(QGraphicsObject):
    WIDTH = 150
    HEIGHT = 40
    PEN_WIDTH_NORMAL = 3
    PEN_WIDTH_HOVER = 6
    clicked = Signal()

################################################################################

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptHoverEvents(True)
        self._hover = False
        self._a = QPointF(-self.WIDTH/2, -self.HEIGHT/2)
        self._b = QPointF(self.WIDTH/2, -self.HEIGHT/2)
        self._c = QPointF(self.WIDTH/2, self.HEIGHT/2)
        self._d = QPointF(-self.WIDTH/2, self.HEIGHT/2)

################################################################################

    def paint(self, painter, option, widget):
        """

        """

        pen = QPen(Qt.green)
        pen.setJoinStyle(Qt.MiterJoin)
        if self._hover:
            pen.setWidth(self.PEN_WIDTH_HOVER)
            painter.setPen(pen)
        else:
            pen.setWidth(self.PEN_WIDTH_NORMAL)
            painter.setPen(pen)
        painter.drawPath(self.shape())
        painter.setFont(QFont('Helvetica', 20))
        painter.drawText(self.boundingRect(), Qt.AlignCenter, 'Generate')

################################################################################

    def boundingRect(self):
        """

        """

        if self._hover:
            penMargin = self.PEN_WIDTH_HOVER/2
        else:
            penMargin = self.PEN_WIDTH_NORMAL/2
        return QRectF(QPointF(min(self._a.x(), self._d.x())-penMargin,
                              min(self._a.y(), self._b.y())-penMargin),
                      QPointF(max(self._b.x(), self._c.x())+penMargin,
                              max(self._c.y(), self._d.y())+penMargin))

################################################################################

    def shape(self):
        """

        """

        shape = QPainterPath()
        shape.moveTo(self._a)
        shape.lineTo(self._b)
        shape.lineTo(self._c)
        shape.lineTo(self._d)
        shape.lineTo(self._a)
        return shape

################################################################################

    def hoverEnterEvent(self, event):
        """

        """

        self.prepareGeometryChange()
        self._hover = True
        self._a =  QPointF(-self.WIDTH/2-randint(0, int(self.HEIGHT/3)),
                           -self.HEIGHT/2-randint(0, int(self.HEIGHT/3)))
        self._b = QPointF(self.WIDTH/2+randint(0, int(self.HEIGHT/3)),
                          -self.HEIGHT/2-randint(0, int(self.HEIGHT/3)))
        self._c = QPointF(self.WIDTH/2+randint(0, int(self.HEIGHT/3)),
                          self.HEIGHT/2+randint(0, int(self.HEIGHT/3)))
        self._d = QPointF(-self.WIDTH/2-randint(0, int(self.HEIGHT/3)),
                          self.HEIGHT/2+randint(0, int(self.HEIGHT/3)))
        super().hoverEnterEvent(event)

################################################################################

    def hoverLeaveEvent(self, event):
        """

        """

        self.prepareGeometryChange()
        self._hover = False
        self._a = QPointF(-self.WIDTH/2, -self.HEIGHT/2)
        self._b = QPointF(self.WIDTH/2, -self.HEIGHT/2)
        self._c = QPointF(self.WIDTH/2, self.HEIGHT/2)
        self._d = QPointF(-self.WIDTH/2, self.HEIGHT/2)
        super().hoverLeaveEvent(event)

################################################################################

    def mousePressEvent(self, event):
        """

        """

        self.clicked.emit()
        super().mousePressEvent(event)

################################################################################



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



################################################################################

class ScaleTextItem(QGraphicsItem):
    NOTES_SHARP = 'A A# B C C# D D# E F F# G G#'
    NOTES_FLAT = 'A Bb B C Db D Eb E F Gb G Ab'
    HEIGHT = 40
    WIDTH = 13*HEIGHT
    FONT_SIZE = 20
    FONT_FAMILY = 'Helvetica'

################################################################################

    def __init__(self, scale, parent=None):
        self._scale = scale
        super().__init__(parent)

################################################################################

    def setScale(self, scale):
        """

        """

        self._scale = scale
        self.update()

################################################################################

    def paint(self, painter, option, widget):
        """

        """

        rects = [QRectF(QPointF(-self.WIDTH/2+(i*self.HEIGHT), -self.HEIGHT/2),
                        QPointF(-self.WIDTH/2+(i+1)*self.HEIGHT, self.HEIGHT/2))
                 for i in range(13)]

        scale = self._scale.split()
        if any(['#' in note for note in scale]) and all(['b' not in note for note in scale]):
            used = self.NOTES_SHARP.split()
        elif any(['b' in note for note in scale]) and all(['#' not in note for note in scale]):
            used = self.NOTES_FLAT.split()
        else:
            used = self.NOTES_SHARP.split()
        used = used[used.index(scale[0]):]+used[:used.index(scale[0])+1]

        painter.setFont(QFont(self.FONT_FAMILY, self.FONT_SIZE))
        for i in range(len(used)):
            if used[i] in scale:
                painter.setPen(Qt.green)
            else:
                painter.setPen(Qt.darkRed)
            painter.drawText(rects[i], Qt.AlignCenter, used[i])

################################################################################

    def boundingRect(self):
        """

        """

        return QRectF(QPointF(-self.WIDTH/2, -self.HEIGHT/2), QPointF(self.WIDTH/2, self.HEIGHT/2))

################################################################################