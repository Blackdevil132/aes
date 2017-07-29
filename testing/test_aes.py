from tools.conversion.Converter import hexseqToBitseq, bitseqToBytearray
from AES import AES
import unittest


class TestAES(unittest.TestCase):
    def test_cipher(self):
        i = '00112233445566778899aabbccddeeff'
        i = hexseqToBitseq(i)
        i = bitseqToBytearray(i)

        k = '000102030405060708090a0b0c0d0e0f'
        k = hexseqToBitseq(k)
        k = bitseqToBytearray(k)

        o = '69c4e0d86a7b0430d8cdb78070b4c55a'
        o = hexseqToBitseq(o)
        o = bitseqToBytearray(o)

        aes = AES(4)
        aes.setKey(k)
        aes.setPlaintext(i)
        aes.encrypt()
        self.assertEqual(aes.getCiphertext(), o)

if __name__ == '__main__':
    unittest.main()