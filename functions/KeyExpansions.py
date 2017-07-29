from tools.conversion.Converter import hexToInt
from tools.SBox import SBox
from tools.Tools import getRounds
from tools.datatypes.Byte import Byte
from tools.datatypes.Word import Word


class KeyExpansion:
    def __init__(self, key, Nk, Nb=4):
        """

        :type key: [Byte]
        :type Nk: int
        :type Nb: int
        :param key: the cipherkey in form of a Bytearray of length 4*Nk
        :param Nk: keylength in words; possible values 4, 6 and 8
        :param Nb: blocklength in words; fixes to 4 for AES
        """
        self.key = key
        self.Nk = Nk
        self.Nb = Nb
        self.Nr = getRounds(Nk, Nb)

        self.Rcon = []
        for i in range(int((self.Nb * (self.Nr + 1))/self.Nk)):
            h = hex(Byte('02') ** i)[2:] + '000000'
            if len(h) == 7:
                h = '0' + h

            self.Rcon.append(Word(h))

        self.sbox = SBox()

    def run(self):
        """
        calculate the key schedule for the specified parameters

        :rtype: [Word]
        :return: Keyschedule for keylength Nk and blocklength Nb
        """
        w = [Word() for i in range(self.Nb * (self.Nr + 1))]

        for i in range(self.Nk):
            w[i] = Word(self.key[(4 * i):(4 * i + 4)])

        for i in range(self.Nk, self.Nb * (self.Nr + 1)):
            temp = w[i - 1]
            if i % self.Nk == 0:
                temp = self.SubWord(self.RotWord(temp)) + self.Rcon[int((i-1) / self.Nk)]
            elif self.Nk > 6 and i % self.Nk == 4:
                temp = self.SubWord(temp)
            w[i] = w[i - self.Nk] + temp

        return w

    def SubWord(self, word):
        new_word = Word()

        for i in range(4):
            x = hexToInt(str(word[i])[1])
            y = hexToInt(str(word[i])[2])
            new_word[i] = Byte(self.sbox[x][2 * y: 2 * y + 2])
        return new_word

    def RotWord(self, word):
        a = Word('00000001')
        ret = word * a
        return ret


"""
k = '2b7e151628aed2a6abf7158809cf4f3c'
print('Hexkey:', k)
k = hexSeqToBitSeq(k)
print('Bitkey:', k)
k = bitSeqToByteArray(k)
print('Bytearraykey:', end='')
for b in k:
    print(b, end='')
print('\n')
w = Word('09cf4f3c')
ke = KeyExpansion(k, 4)
keyschedule = ke.run()
for i in range(len(keyschedule)):
    print(i, ':', keyschedule[i])
"""