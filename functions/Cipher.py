from tools.State import State
from tools.Byte import Byte
from tools.Word import Word
from functions.KeyExpansions import KeyExpansion
from tools.Tools import *


class Cipher:
    def __init__(self, input, w):
        """
        
        Nb is fixed to 4 for the AES algorithm
        Nr depends on the key length (Nk: 4 -> Nr: 10; Nk: 6 -> Nr: 12; Nk: 8 -> Nr: 14)
        State s is transformed in Nr rounds, with the final round differing from the first Nr-1 rounds
        Final state is then copied to the output

        :type input: [Byte]
        :type w: [Word]
        :param input: 128 bit block (16 Byte)
        :param w: Key schedule
        """
        self.input = input
        self.output = 0
        self.w = w
        self.Nr = 10
        self.Nb = 4
        self.state = bytearrayToState(input)
        self.sbox = initiateSbox()

    def main(self):
        """
        :rtype: [Byte]

        """

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
        keywords = self.w[(round*self.Nb):((round + 1)*self.Nb)]
        print('from', (round*self.Nb), 'to', ((round + 1)*self.Nb), keywords)
        new_state = State()

        for c in range(self.Nb):
            col = [self.state[0][c], self.state[1][c], self.state[2][c], self.state[3][c]]
            col_w = Word(col)
            print('column:', c)
            new_col = col_w + keywords[c]

            for i in range(4):
                new_state[i][c] = new_col[i]

        self.state = new_state


    def SubBytes(self):
        hexToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, }

        new_state = State()
        for c in range(self.Nb):
            for r in range(4):
                x = hexToInt[str(self.state[r][c])[1]]
                y = hexToInt[str(self.state[r][c])[2]]
                # print(r, c, '->', x, y, '->', (2 * y), self.sbox[x][2*y: 2*y + 2])

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


def bytearrayToState(a):
    state = State()
    for c in range(4):
        for r in range(4):
            state[r][c] = a[r + 4 * c]

    return state


def stateToBytearray(state):
    array = [Byte() for i in range(16)]
    for c in range(4):
        for r in range(4):
            array[r + 4 * c] = state[r][c]

    return array


def initiateSbox():
    PATH_SBOX = "Sbox.txt"

    file = open(PATH_SBOX)
    s = file.read()
    file.close()

    sbox = ['' for i in range(16)]
    for i in range(16):
        sbox[i] = s[(32 * i):(32 * i + 32)]

    return sbox


def shift(r, Nb):
    return r


a = '00112233445566778899aabbccddeeff'
k = '000102030405060708090a0b0c0d0e0f'

print('Hexinput:', a)
a = hexSeqToBitSeq(a)
print('Bitinput:', a)
a = bitSeqToByteArray(a)
print('Bytearrayinput:', end='')
for b in a:
    print(b, end='')
print('\n')

print('Hexkey:', k)
k = hexSeqToBitSeq(k)
print('Bitkey:', k)
k = bitSeqToByteArray(k)
print('Bytearraykey:', end='')
for b in k:
    print(b, end='')
print('\n')

ke = KeyExpansion(k, 4)
w = ke.run()
c = Cipher(a, w)
o = c.main()
print('Bytearrayouput:', end='')
for b in o:
    print(b, end='')
print('\n')
