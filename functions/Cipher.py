from functions.KeyExpansion import KeyExpansion
from tools.Tools import shift
from tools.SBox import SBox
from tools.conversion.Converter import binToBytearray, hexToBin, hexToInt, bytearrayToState, stateToBytearray
from tools.datatypes.Byte import Byte
from tools.datatypes.State import State
from tools.datatypes.Word import Word


# noinspection PyPep8Naming
class Cipher:
    def __init__(self, w, Nr, Nb=4):
        """
        
        Nb is fixed to 4 for the AES algorithm
        Nr depends on the key length (Nk: 4 -> Nr: 10; Nk: 6 -> Nr: 12; Nk: 8 -> Nr: 14)
        State s is transformed in Nr rounds, with the final round differing from the first Nr-1 rounds
        Final state is then copied to the output

        :type w: [Word]
        :param w: Key schedule
        """
        self.output = None
        self.w = w
        self.Nb = Nb
        self.Nr = Nr
        self.state = None
        self.sbox = SBox()
        self.invsbox = SBox(inverse=True)

    def encrypt(self, inp):
        """
        :rtype: [Byte]

        """

        self.state = bytearrayToState(inp)

        self.AddRoundKey(0)

        for i in range(1, self.Nr):
            self.SubBytes()
            self.ShiftRows()
            self.MixColumns()
            self.AddRoundKey(i)

        self.SubBytes()
        self.ShiftRows()
        self.AddRoundKey(self.Nr)

        self.output = stateToBytearray(self.state)
        return self.output

    def AddRoundKey(self, round):
        keywords = self.w[(round * self.Nb):((round + 1) * self.Nb)]
        new_state = State()

        for c in range(self.Nb):
            col = [self.state[0][c], self.state[1][c], self.state[2][c], self.state[3][c]]
            col_w = Word(col)
            new_col = col_w + keywords[c]

            for i in range(4):
                new_state[i][c] = new_col[i]

        self.state = new_state

    def SubBytes(self):
        new_state = State()
        for c in range(self.Nb):
            for r in range(4):
                x = hexToInt(str(self.state[r][c])[1])
                y = hexToInt(str(self.state[r][c])[2])

                new_state[r][c] = Byte(self.sbox[x][2 * y: 2 * y + 2])

        self.state = new_state

    def ShiftRows(self):
        new_state = State()

        for r in range(4):
            for c in range(self.Nb):
                new_state[r][c] = self.state[r][(c + shift(r, self.Nb)) % self.Nb]

        self.state = new_state

    def MixColumns(self):
        new_state = State()

        for c in range(self.Nb):
            new_state[0][c] = (Byte('02') * self.state[0][c])   + (Byte('03') * self.state[1][c])   + self.state[2][c]                  + self.state[3][c]
            new_state[1][c] = self.state[0][c]                  + (Byte('02') * self.state[1][c])   + (Byte('03') * self.state[2][c])   + self.state[3][c]
            new_state[2][c] = self.state[0][c]                  + self.state[1][c]                  + (Byte('02') * self.state[2][c])   + (Byte('03') * self.state[3][c])
            new_state[3][c] = (Byte('03') * self.state[0][c])   + self.state[1][c]                  + self.state[2][c]                  + (Byte('02') * self.state[3][c])

        self.state = new_state

    def InvShiftRows(self):
        new_state = State()

        for r in range(4):
            for c in range(self.Nb):
                new_state[r][(c + shift(r, self.Nb)) % self.Nb] = self.state[r][c]

        self.state = new_state

    def InvSubBytes(self):
        new_state = State()
        for c in range(self.Nb):
            for r in range(4):
                x = hexToInt(str(self.state[r][c])[1])
                y = hexToInt(str(self.state[r][c])[2])

                new_state[r][c] = Byte(self.invsbox[x][2 * y: 2 * y + 2])

        self.state = new_state

    def InvMixColumns(self):
        new_state = State()

        for c in range(self.Nb):
            new_state[0][c] = (Byte('0e') * self.state[0][c])   + (Byte('0b') * self.state[1][c])   + (Byte('0d') * self.state[2][c])   + (Byte('09') * self.state[3][c])
            new_state[1][c] = (Byte('09') * self.state[0][c])   + (Byte('0e') * self.state[1][c])   + (Byte('0b') * self.state[2][c])   + (Byte('0d') * self.state[3][c])
            new_state[2][c] = (Byte('0d') * self.state[0][c])   + (Byte('09') * self.state[1][c])   + (Byte('0e') * self.state[2][c])   + (Byte('0b') * self.state[3][c])
            new_state[3][c] = (Byte('0b') * self.state[0][c])   + (Byte('0d') * self.state[1][c])   + (Byte('09') * self.state[2][c])   + (Byte('0e') * self.state[3][c])

        self.state = new_state

    def decrypt(self, inp):
        """
        :rtype: [Byte]

        """

        self.state = bytearrayToState(inp)

        self.AddRoundKey(self.Nr)

        for i in range(self.Nr-1, 0, -1):
            self.InvShiftRows()
            self.InvSubBytes()
            self.AddRoundKey(i)
            self.InvMixColumns()

        self.InvShiftRows()
        self.InvSubBytes()
        self.AddRoundKey(0)

        self.output = stateToBytearray(self.state)
        return self.output