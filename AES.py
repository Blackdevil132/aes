import argparse

from tools.Tools import getRounds
from functions.Cipher import Cipher
from functions.KeyExpansion import KeyExpansion
from tools.datatypes.Byte import Byte
from tools.conversion import Converter
import os


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

    def getKey(self, t: str="hex", filename="key.txt") -> str:
        if t == "hex":
            return Converter.bytearrayToHex(self.key)
        elif t == "text":
            return Converter.bytearrayToText(self.key)
        elif t == "file":
            text = Converter.bytearrayToHex(self.key)
            file = open(filename, 'w', encoding="utf8")
            file.write(text)
            file.close()
            return filename

    def getPlaintext(self, t: str="hex", filename="decrypted.txt") -> str:
        if t == "hex":
            return Converter.bytearrayToHex(self.plaintext)
        elif t == "text":
            return Converter.bytearrayToText(self.plaintext)
        elif t == "file":
            text = Converter.bytearrayToText(self.plaintext)
            file = open(filename, 'w', encoding="utf8")
            file.write(text)
            file.close()
            return filename

    def getCiphertext(self, t: str="hex", filename="encrypted.txt") -> str:
        if t == "hex":
            return Converter.bytearrayToHex(self.ciphertext)
        elif t == "text":
            return Converter.bytearrayToText(self.ciphertext)
        elif t == "file":
            text = Converter.bytearrayToHex(self.ciphertext)
            file = open(filename, 'w', encoding="utf8")
            file.write(text)
            file.close()
            return filename

    def setKey(self, **kwargs):
        for kw in kwargs:
            if kw == "text":
                key = Converter.textToBytearray(kwargs[kw])
                break
            elif kw == "file":
                file = open(kwargs[kw], encoding="utf8")
                text = file.read()
                file.close()
                key = Converter.hexToBytearray(text)
                break
            elif kw == "hex":
                key = Converter.hexToBytearray(kwargs[kw])
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
                self.plaintext = Converter.textToBytearray(kwargs[kw])
                break
            elif kw == "file":
                file = open(kwargs[kw], encoding="utf8")
                text = file.read()
                file.close()
                self.plaintext = Converter.textToBytearray(text)
                break
            elif kw == "bytes":
                self.plaintext = kwargs[kw]
                break
            elif kw == "hex":
                self.plaintext = Converter.hexToBytearray(kwargs[kw])
                break
            else:
                raise ValueError(kw + " is no accepted input type.")

    def setCiphertext(self, **kwargs):
        for kw in kwargs:
            if kw == "text":
                self.ciphertext = Converter.textToBytearray(kwargs[kw])
                break
            elif kw == "file":
                file = open(kwargs[kw], encoding="utf8")
                text = file.read()
                file.close()
                self.ciphertext = Converter.hexToBytearray(text)
                break
            elif kw == "bytes":
                self.ciphertext = kwargs[kw]
                break
            elif kw == "hex":
                self.ciphertext = Converter.hexToBytearray(kwargs[kw])
                break
            else:
                raise ValueError(kw + " is no accepted input type.")

    def encrypt(self):
        if self.plaintext is None or self.key is None:
            raise AttributeError("Missing key or plaintext.")

        self.ciphertext = []
        self.keyschedule = KeyExpansion(self.key, self.Nk, self.Nb).run()
        self.cipher = Cipher(self.keyschedule, self.Nr)
        if len(self.plaintext) % 16 != 0:
            for i in range(16 - len(self.plaintext) % 16):
                self.plaintext.append(Byte())

        for i in range(0, len(self.plaintext), 16):
            inp = self.plaintext[i:i+16]
            self.ciphertext += self.cipher.encrypt(inp)

    def decrypt(self):
        if self.ciphertext is None or self.key is None:
            raise AttributeError("Missing key or ciphertext.")

        self.plaintext = []
        self.keyschedule = KeyExpansion(self.key, self.Nk, self.Nb).run()
        cipher = Cipher(self.keyschedule, self.Nr)

        if len(self.ciphertext) % 16 != 0:
            for i in range(16 - len(self.ciphertext) % 16):
                self.ciphertext.append(Byte())

        for i in range(0, len(self.ciphertext), 16):
            inp = self.ciphertext[i:i+16]
            self.plaintext += cipher.decrypt(inp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Encrypt and decrypt files with AES.")

    parser.add_argument('-k', '--key', required=True, help="Key in textform of length 16, 24 or 32 Symbols")
    parser.add_argument("-i", "--input", required=True, help="Path to file which should be encrypted or decrypted")
    parser.add_argument("-d", action='store_true', help="set this flag if you want to decrypt the file")
    args = parser.parse_args()

    keylength = int(len(args.key)/4)
    aes = AES(keylength)
    aes.setKey(text=args.key)
    if not args.d:
        file = args.input.split(".")
        name = file[0] + "." + file[1] + ".enc"
        aes.setPlaintext(file=args.input)
        aes.encrypt()
        aes.getCiphertext("file", name)
        os.remove(args.input)
        print("File encrypted and stored in: " + name)
    else:
        file = args.input.split(".")
        name = file[0] + "." + file[1]

        if os.path.isfile(args.input):
            f = args.input
        elif os.path.isfile(args.input + ".enc"):
            f = args.input + ".enc"
        else:
            raise FileNotFoundError("File" + args.input + "does not exist!")

        aes.setCiphertext(file=f)
        aes.decrypt()
        os.remove(f)
        aes.getPlaintext("file", name)
        print("File decrypted and stored in: " + name)
