import unittest
from tools.conversion.Converter import *
from tools.datatypes.State import State


class TestConverter_advanced(unittest.TestCase):

    def setUp(self):
        self.hex = '00112233445566778899aabbccddeeff'
        self.ba = [Byte("00"), Byte("11"), Byte("22"), Byte("33"), Byte("44"), Byte("55"), Byte("66"), Byte("77"),
                   Byte("88"), Byte("99"), Byte("aa"), Byte("bb"), Byte("cc"), Byte("dd"), Byte("ee"), Byte("ff")]
        self.state = State()
        self.state.matrix = [[Byte("00"), Byte("44"), Byte("88"), Byte("cc")], [Byte("11"), Byte("55"), Byte("99"), Byte("dd")],
                             [Byte("22"), Byte("66"), Byte("aa"), Byte("ee")], [Byte("33"), Byte("77"), Byte("bb"), Byte("ff")]]

    def test_bytea_and_state_conv(self):
        self.assertEqual(bytearrayToState(self.ba), self.state)
        self.assertEqual(stateToBytearray(self.state), self.ba)
        self.assertEqual(stateToBytearray(bytearrayToState(self.ba)), self.ba)

    def test_hex_and_bytea_conv(self):
        self.assertEqual(hexToBytearray(self.hex), self.ba)
        self.assertSequenceEqual(bytearrayToHex(self.ba), self.hex)
        self.assertEqual(bytearrayToHex(hexToBytearray(self.hex)), self.hex)

    def test_hex_and_text_conv(self):
        self.assertEqual(hexToText("68616c6c6f"), "hallo")
        self.assertEqual(hexToText("2122a72425262f2829"), '!"§$%&/()')
        self.assertEqual(textToHex("hallo"), "68616c6c6f")
        self.assertEqual(textToHex('!"§$%&/()'), "2122a72425262f2829")


if __name__ == '__main__':
    unittest.main()