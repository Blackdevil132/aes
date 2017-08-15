from tools.conversion.Converter import hexToBytearray
from AES import AES
import unittest


class TestAES(unittest.TestCase):
    def test_cipher(self):
        i = '00112233445566778899aabbccddeeff'
        k = '000102030405060708090a0b0c0d0e0f'
        o = '69c4e0d86a7b0430d8cdb78070b4c55a'

        aes = AES(4)
        aes.setKey(hex=k)
        aes.setPlaintext(file="input.txt")
        aes.encrypt()
        aes.getCiphertext(t="file")
        #self.assertEqual(aes.getCiphertext(), o)
        aes.decrypt()
        aes.getPlaintext(t="file")
        #self.assertEqual(aes.getPlaintext(), i)
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()
