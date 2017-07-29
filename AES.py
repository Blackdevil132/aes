from tools.Tools import getRounds
from functions.Cipher import Cipher
from functions.KeyExpansions import KeyExpansion


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
        self.ciphertext = None

        self.cipher = None
        self.keyschedule = None

    def getKey(self):
        return self.key

    def getPlaintext(self):
        return self.plaintext

    def getCiphertext(self):
        return self.ciphertext

    def setKey(self, key):
        self.key = key

    def setPlaintext(self, text):
        self.plaintext = text

    def setCiphertext(self, text):
        self.ciphertext = text

    def encrypt(self):
        if self.plaintext is None or self.key is None:
            raise AttributeError("Missing key or plaintext.")

        self.keyschedule = KeyExpansion(self.key, self.Nk, self.Nb).run()
        self.cipher = Cipher(self.plaintext, self.keyschedule, self.Nr)

        self.ciphertext = self.cipher.run()

    def decrypt(self):
        pass
