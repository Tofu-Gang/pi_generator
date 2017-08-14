__author__ = 'Tofu Gang'

from unittest import TestCase, main
from src.pi import PiGenerator
from src.scales import SCALE_TYPES, ROOT_NOTES



################################################################################

class TestPiGenerator(TestCase):

################################################################################

    def setUp(self):
        """

        """

        self._generator = PiGenerator()

################################################################################

    def testInputData(self):
        """
        Testing bunch of facts stated at the source (pi.txt) website
        http://newton.ex.ac.uk/research/qsystems/collabs/pi/.
        """

        data = self._generator._data[0]
        self.assertTrue(len(data)==1000000)
        self.assertTrue(data[-1]=='1')
        self.assertTrue(data.count('123456')==0)
        self.assertTrue(data.count('12345')==8)
        self.assertTrue(data.count('123455')==3)
        self.assertTrue(data.count('012345')==2)
        self.assertTrue(data.count('0123455')==2)
        self.assertTrue(data.count('270161')==3)
        self.assertTrue(data.count('0')==99959)
        self.assertTrue(data.count('1')==99758)
        self.assertTrue(data.count('2')==100026)
        self.assertTrue(data.count('3')==100229)
        self.assertTrue(data.count('4')==100230)
        self.assertTrue(data.count('5')==100359)
        self.assertTrue(data.count('6')==99548)
        self.assertTrue(data.count('7')==99800)
        self.assertTrue(data.count('8')==99985)
        self.assertTrue(data.count('9')==100106)

################################################################################

    def testScale(self):
        """

        """

        self._generator._scaleTypeIndex = 0
        self.assertEqual(self._generator.previousScaleType, SCALE_TYPES[-1])
        self._generator.setPreviousScaleType()
        self.assertEqual(self._generator.nextScaleType, SCALE_TYPES[0])
        self._generator.setNextScaleType()
        self.assertEqual(self._generator.previousScaleType, SCALE_TYPES[-1])

################################################################################

    def testRootNote(self):
        """

        """

        self._generator._rootNoteIndex = len(ROOT_NOTES)-1
        self.assertEqual(self._generator.nextRootNote, ROOT_NOTES[0])
        self._generator.setNextRootNote()
        self.assertEqual(self._generator.previousRootNote, ROOT_NOTES[-1])
        self._generator.setPreviousRootNote()
        self.assertEqual(self._generator.nextRootNote, ROOT_NOTES[0])

################################################################################

    def testSoloLength(self):
        """

        """

        self._generator._soloLength = 1
        self._generator.decreaseSoloLength()
        self.assertEqual(self._generator.soloLength, self._generator.maxSoloLength)
        self._generator.increaseSoloLength()
        self.assertEqual(self._generator.soloLength, 1)

################################################################################

    def testMapping(self):
        """

        """

        for _ in range(100):
            used = self._generator.usedNumbers
            excluded = self._generator._excludedNumbers
            joined = ''.join([str(number) for number in used])+excluded
            self.assertEqual(len(joined), 10)
            [self.assertEqual(joined.count(str(i)), 1) for i in range(10)]
            self._generator._updateMappingExclusion()

################################################################################

    def testSegments(self):
        """

        """

        segments = self._generator._segments()
        self.assertTrue(all([len(segment)>0 for segment in segments]))
        for digit in self._generator._excludedNumbers:
            self.assertFalse(any([digit in segment for segment in segments]))
            self.assertFalse(digit in self._generator.soloSegment())
        self.assertEqual(len(self._generator.soloSegment()), self._generator.soloLength)

################################################################################

    def tearDown(self):
        """

        """

        del self._generator

################################################################################

if __name__ == '__main__':
    main()

################################################################################