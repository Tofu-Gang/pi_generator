__author__ = 'Tofu Gang'

from PyQt5.QtCore import QFile, QTextStream
from src.scales import SCALE_TYPES, ROOT_NOTES, SCALES
from itertools import chain
from random import randint
import res.resources_rc



################################################################################

class PiGenerator(object):
    SCALE_TYPE_DEFAULT_INDEX = 0
    ROOT_NOTE_DEFAULT_INDEX = 3

################################################################################

    def __init__(self):
        self._data = None
        self._loadData()
        self._scaleTypeIndex = self.SCALE_TYPE_DEFAULT_INDEX
        self._rootNoteIndex = self.ROOT_NOTE_DEFAULT_INDEX
        self._soloLength = 1
        self._excludedNumbers = None
        self._updateMappingExclusion()
        self._soloLength = self.maxSoloLength

################################################################################

    def _loadData(self):
        """

        """

        file = QFile(':/pi.txt')
        if file.open(QFile.ReadOnly):
            bytes = file.readAll()
            stream = QTextStream(bytes)
            self._data = [stream.readAll()]
            file.close()

################################################################################

    @property
    def scale(self):
        """

        """

        return SCALES[self._scaleTypeIndex][self._rootNoteIndex]

################################################################################

    @property
    def scaleType(self):
        """

        """

        return SCALE_TYPES[self._scaleTypeIndex]

################################################################################

    @property
    def nextScaleType(self):
        """

        """

        return SCALE_TYPES[(self._scaleTypeIndex+1)%len(SCALE_TYPES)]

################################################################################

    @property
    def previousScaleType(self):
        """

        """

        return SCALE_TYPES[(self._scaleTypeIndex-1)%len(SCALE_TYPES)]

################################################################################

    def setNextScaleType(self):
        """

        """

        if self._scaleTypeIndex < len(SCALE_TYPES)-1:
            self._scaleTypeIndex += 1
        else:
            self._scaleTypeIndex = 0
        if len(self._excludedNumbers) != 10-len(self.scale):
            self._updateMappingExclusion()

################################################################################

    def setPreviousScaleType(self):
        """

        """

        if self._scaleTypeIndex > 0:
            self._scaleTypeIndex -= 1
        else:
            self._scaleTypeIndex = len(SCALE_TYPES)-1
        if len(self._excludedNumbers) != 10-len(self.scale):
            self._updateMappingExclusion()

################################################################################

    @property
    def rootNote(self):
        """

        """

        return ROOT_NOTES[self._rootNoteIndex]

################################################################################

    @property
    def nextRootNote(self):
        """

        """

        return ROOT_NOTES[(self._rootNoteIndex+1)%len(ROOT_NOTES)]

################################################################################

    @property
    def previousRootNote(self):
        """

        """

        return ROOT_NOTES[(self._rootNoteIndex-1)%len(ROOT_NOTES)]

################################################################################

    def setNextRootNote(self):
        """

        """

        if self._rootNoteIndex < len(ROOT_NOTES)-1:
            self._rootNoteIndex += 1
        else:
            self._rootNoteIndex = 0

################################################################################

    def setPreviousRootNote(self):
        """

        """

        if self._rootNoteIndex > 0:
            self._rootNoteIndex -= 1
        else:
            self._rootNoteIndex = len(ROOT_NOTES)-1

################################################################################

    @property
    def soloLength(self):
        """

        """

        return self._soloLength

################################################################################

    @property
    def maxSoloLength(self):
        """

        """

        return max([len(segment) for segment in self._segments()])

################################################################################

    def increaseSoloLength(self):
        """

        """

        if self._soloLength < self.maxSoloLength:
            self._soloLength += 1
        else:
            self._soloLength = 1

################################################################################

    def decreaseSoloLength(self):
        """

        """

        if self._soloLength > 1:
            self._soloLength -= 1
        else:
            self._soloLength = self.maxSoloLength

################################################################################

    @property
    def usedNumbers(self):
        """

        """

        return [i for i in range(10) if str(i) not in self._excludedNumbers]

################################################################################

    def _updateMappingExclusion(self):
        """

        """

        self._excludedNumbers = ''
        for _ in range(10-len(self.scale.split()[:-1])):
            number = randint(0, 9)
            while str(number) in self._excludedNumbers:
                number = randint(0, 9)
            self._excludedNumbers += str(number)
        if self._soloLength > self.maxSoloLength:
            self._soloLength = self.maxSoloLength

################################################################################

    def _segments(self):
        """

        """

        segments = self._data
        for denominator in self._excludedNumbers:
            segments = list(chain(*[segment.split(denominator) for segment in segments if len(segment) > 0]))
        return [segment for segment in segments if len(segment) > 0]

################################################################################

    def soloSegment(self):
        """

        """

        segments = [segment for segment in self._segments() if len(segment) >= self._soloLength]
        segmentIndex = randint(0, len(segments)-1)
        segment = segments[segmentIndex]
        startIndex = randint(0, len(segment)-self._soloLength)
        return segment[startIndex:startIndex+self._soloLength]

################################################################################