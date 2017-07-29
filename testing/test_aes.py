from tools.conversion.Converter import hexToBytearray
from AES import AES
import unittest


class TestAES(unittest.TestCase):
    def test_cipher(self):
        i = '00112233445566778899aabbccddeeff'
        k = '000102030405060708090a0b0c0d0e0f'
        o = hexToBytearray('69c4e0d86a7b0430d8cdb78070b4c55a')

        aes = AES(4)
        aes.setKey(hex=k)
        aes.setPlaintext(hex=i)
        aes.encrypt()
        self.assertEqual(aes.getCiphertext(), o)

if __name__ == '__main__':
    unittest.main()
