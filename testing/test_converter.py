import unittest
from tools.conversion.Converter import *


class TestConverter_basics(unittest.TestCase):
    def test_hextoint(self):
        self.assertEqual(hexToInt('00000'), 0)
        self.assertEqual(hexToInt('11'), 17)
        self.assertEqual(hexToInt('11f'), 287)

    def test_hextobin(self):
        self.assertEqual(hexToBin("3f"), "00111111")
        self.assertEqual(hexToBin("0"), "0000")
        self.assertEqual(hexToBin("1ac4"), "0001101011000100")

    def test_inttohex(self):
        self.assertEqual(intToHex(287), "11f")
        self.assertEqual(intToHex(17), "11")
        self.assertEqual(intToHex(0), "00")

    def test_inttobin(self):
        self.assertEqual(intToBin(13), "1101")
        self.assertEqual(intToBin(0), "0")
        self.assertEqual(intToBin(176), "10110000")

    def test_bintoint(self):
        self.assertEqual(binToInt("1101"), 13)
        self.assertEqual(binToInt("0"), 0)
        self.assertEqual(binToInt("10110000"), 176)

    def test_bintohex(self):
        self.assertEqual(binToHex("00111111"), "3f")
        self.assertEqual(binToHex("0000"), "00")
        self.assertEqual(binToHex("0001101011000100"), "1ac4")

if __name__ == '__main__':
    unittest.main()