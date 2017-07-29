from tools.Byte import Byte


# noinspection PyTypeChecker
class Word():
    def __init__(self, ba='00000000'):
        """

        :type ba: [Byte]
        """
        #TODO Typechecking of list elements
        if type(ba) == list and len(ba) == 4:
            self.bytes = ba
        elif type(ba) == str and len(ba) == 8:
            self.bytes = [Byte(ba[2*i: 2*i + 2]) for i in range(4)]

    def __setitem__(self, key, value):
        self.bytes[key] = value

    def __getitem__(self, item):
        return self.bytes[item]

    def __str__(self):
        s = ''
        for byte in self.bytes:
            s += str(byte)

        return s

    def __add__(self, other):
        """
        Addition is performed by adding the finite field coefficients of like powers
        This addition corresponds to an XOR operation between the corresponding bytes in each of the words

        :type other: Word
        :rtype: Word
        :param other: the Word to add to self
        :return: Sum of self and other
        """
        new = Word()
        for i in range(4):
            new[i] = self[i] + other[i]

        return new

    def __mul__(self, other):
        """
        modular product of words a and b, to get a polynomial of degree less than 4 the multiplication is reduced 
        modulo the polynomial {01}{01}
        using a = {00}{00}{00}{01} will rotate bytes of b (to the left) -- RotWord()

        :type other: Word
        :rtype: Word
        :param other: the Word to multiply self with
        :return: Product of self and other
        """
        new = Word()
        a = self
        b = other
        d_0 = (a[0] * b[0]) + (a[3] * b[1]) + (a[2] * b[2]) + (a[1] * b[3])
        d_1 = (a[1] * b[0]) + (a[0] * b[1]) + (a[3] * b[2]) + (a[2] * b[3])
        d_2 = (a[2] * b[0]) + (a[1] * b[1]) + (a[0] * b[2]) + (a[3] * b[3])
        d_3 = (a[3] * b[0]) + (a[2] * b[1]) + (a[1] * b[2]) + (a[0] * b[3])
        new[:] = [d_0, d_1, d_2, d_3]

        return new




"""
b1 = Byte('00')
b2 = Byte('00')
b3 = Byte('00')
b4 = Byte('01')
b5 = Byte('aa')
b6 = Byte('bb')
b7 = Byte('cc')
b8 = Byte('dd')

w1 = Word()
w2 = Word()
w1[:] = [b1, b2, b3, b4]
w2[:] = [b5, b6, b7, b8]
print(w1*w2)
"""