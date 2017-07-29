from tools.Tools import getRounds
from functions.Cipher import Cipher
from functions.KeyExpansions import KeyExpansion
from tools.datatypes.Byte import Byte
from tools.conversion import Converter
import sys


# noinspection PyTypeChecker
class AES:
    def __init__(self, Nk):
        """

        :type Nk: int
        :param Nk: key length in number of words. allowed values are 4, 6 and 8
        """
        if Nk not in (4, 6, 8):
            raise ValueError(str(Nk) + " is no supported key length.")
        self.Nk = Nk
        self.Nb = 4
        self.Nr = getRounds(self.Nk, self.Nb)
        self.key = None
        self.plaintext = None
        self.ciphertext = []

        self.cipher = None
        self.keyschedule = None

    def getKey(self):
        return self.key

    def getPlaintext(self):
        return self.plaintext

    def getCiphertext(self):
        return self.ciphertext

    def setKey(self, **kwargs):
        for kw in kwargs:
            if kw == "hex":
                bits = Converter.hexToBin(kwargs[kw])
                key = Converter.binToBytearray(bits)
                break
            elif kw == "bytes":
                key = kwargs[kw]
                break
            else:
                raise ValueError(kw + " is no supported key type.")

        if len(key) not in (16, 24, 32):
            raise ValueError(str(len(key)) + " is no supported key length")
        self.key = key
        self.Nk = int(len(key)/4)

    def setPlaintext(self, **kwargs):
        for kw in kwargs:
            if kw == "text":
                pass
            elif kw == "file":
                pass
            elif kw == "bytes":
                self.plaintext = kwargs[kw]
                break
            elif kw == "hex":
                bits = Converter.hexToBin(kwargs[kw])
                self.plaintext = Converter.binToBytearray(bits)
                break
            else:
                raise ValueError(kw + " is no accepted input type.")

    def setCiphertext(self, text):
        self.ciphertext = text

    def encrypt(self):
        if self.plaintext is None or self.key is None:
            raise AttributeError("Missing key or plaintext.")

        self.keyschedule = KeyExpansion(self.key, self.Nk, self.Nb).run()
        self.cipher = Cipher(self.keyschedule, self.Nr)

        if len(self.plaintext) % 16 != 0:
            for i in range(len(self.plaintext) % 16):
                self.plaintext.append(Byte())

        for i in range(0, len(self.plaintext), 16):
            inp = self.plaintext[i:i+16]
            self.ciphertext += self.cipher.encrypt(inp)

    def decrypt(self):
        pass


if __name__ == '__main__':
    args = sys.argv
    inp = args[1]
    key = args[2]
    c = AES(int(len(key)/8))
    c.setKey(hex=key)
    c.setPlaintext(hex=inp)
    c.encrypt()
    out = c.getCiphertext()
    for b in out:
        print(b, end='')
    print("\n")
