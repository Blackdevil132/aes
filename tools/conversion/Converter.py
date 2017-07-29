from typing import List, Sequence

from tools.datatypes.State import State
from tools.datatypes.Byte import Byte

hexcToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, }

hexcToBin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
             '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}


def hexToBin(hex: str) -> str:
    """
    convert hexadecimal values into binary. result will have at least 4 digits
    :param hex: hexadecimal value
    :return: corresponding binary value
    """
    binary = ""
    for i in range(len(hex)):
        binary += hexcToBin[hex[i]]
    return binary


def hexToInt(hex: str) -> int:
    """
    mostly for converting 2 digit hexadecimal values into integers
    :param hex: (2 digit) hexadecimal value
    :return: corresponding integer value(base 10)
    """
    integer = 0
    for i in range(len(hex)):
        integer += hexcToInt[hex[-(i+1)]] * 16 ** i
    return integer


def intToHex(integer: int) -> str:
    """
    convert integer(base 10) to hexadecimal. Hexadecimal value will have at least 2 digits
    :param integer: value with base 10
    :return: corresponding hexadecimal value
    """
    h = hex(integer)
    h = h[2:]
    if len(h) == 1:
        h = '0' + h
    return h


def intToBin(integer: int) -> str:
    """
    convert integer with base 10 to binary
    :param integer: value with base 10
    :return: corresponding binary value
    """
    s = ""
    if not integer:
        return "0"
    while integer:
        s = str(integer % 2) + s
        integer = int(integer / 2)
    return s


def binToInt(binary: str) -> int:
    """
    convert binary value to int with base 10
    :param binary: value with base 2
    :return: corresponding value with base 10
    """
    integer = 0
    for i in range(len(binary)):
        integer += int(binary[-(i+1)]) * 2 ** i
    return integer


def binToHex(binary: str) -> str:
    """
    convert from base 2 to base 16
    :param binary: value with base 2
    :return: value with base 16
    """
    return intToHex(binToInt(binary))


def bytearrayToState(a: Sequence[Byte]) -> State:
    """
    Convert 16 Bytes into a State
    :param a: iterable object with 16 Bytes
    :return: State
    """
    state = State()
    for c in range(4):
        for r in range(4):
            state[r][c] = a[r + 4 * c]

    return state


def stateToBytearray(state: State) -> List[Byte]:
    """
    convert State into its corresponding List of Bytes
    :param state: State
    :return: List of 16 Bytes
    """
    array = [Byte() for i in range(16)]
    for c in range(4):
        for r in range(4):
            array[r + 4 * c] = state[r][c]

    return array


def binToBytearray(bits: str) -> List[Byte]:
    """
    convert binary sequence into a List of Bytes
    :param bits: binary sequence with length divisible by 8
    :return: List of Bytes
    """
    length = len(bits)
    nb = int(length / 8)
    array = [Byte() for i in range(nb)]
    for n in range(nb):
        array[n] = Byte(
            [bits[8 * n], bits[8 * n + 1], bits[8 * n + 2], bits[8 * n + 3], bits[8 * n + 4], bits[8 * n + 5],
             bits[8 * n + 6], bits[8 * n + 7]])

    return array


def hexToBytearray(hex: str) -> List[Byte]:
    """
    convert sequence of hexadecimal symbols to List of Bytes. length of hexadecimal sequence needs to be divisible by 2
    :param hex: hex. sequence with length divisible by 2
    :return: corresponding List of Bytes
    """
    length = len(hex)
    nb = int(length / 2)
    array = [Byte() for i in range(nb)]
    for n in range(nb):
        array[n] = Byte(hex[2*n] + hex[2*n + 1])
    return array


def bytearrayToHex(ba: Sequence[Byte]) -> str:
    """
    convert List of Bytes into hexadecimal str
    :param ba: List of Bytes
    :return: hex in str
    """
    hex = ""
    for b in ba:
        hex += str(b)[1:3]
    return hex


def textToHex(text: str) -> str:
    """
    convert a ASCII encoded text into hexadecimal sequence
    :param text: text
    :return: hexadecimal str
    """
    hseq = ""
    for c in text:
        i = ord(c)
        hseq += intToHex(i)
    return hseq


def hexToText(hex: str) -> str:
    pass


def bytearrayToText(ba: Sequence[Byte]) -> str:
    h = bytearrayToHex(ba)
    return hexToText(h)


def textToBytearray(text:str) -> List[Byte]:
    h = textToHex(text)
    return hexToBytearray(h)
