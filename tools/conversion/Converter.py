from tools.datatypes.State import State
from tools.datatypes.Byte import Byte

hexToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, }

hexToBin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}


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


def bitseqToBytearray(seq):
    """

    :param seq: sequence of (128) bits 
    :rtype: [Byte]
    """
    length = len(seq)
    nb = int(length/8)
    array = [0 for i in range(nb)]
    for n in range(nb):
        array[n] = Byte([seq[8*n], seq[8*n + 1], seq[8*n + 2], seq[8*n + 3], seq[8*n + 4], seq[8*n + 5], seq[8*n + 6], seq[8*n + 7]])

    return array


def hexseqToBitseq(hseq):
    bseq = ''
    for c in hseq:
        bseq += hexToBin[c]

    return bseq