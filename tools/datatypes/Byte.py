hexToBin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

class Byte():
    """Class to represent a sequence of 8 bits as a Byte"""
    def __init__(self, inp='00'):
        self.bits = ['0' for i in range(8)]

        if type(inp) == list:
            s = inp
        else:
            s = hexToBin[inp[0]] + hexToBin[inp[1]]
        for i in range(8):
            self.bits[i] = int(s[i])

    def __index__(self):
        """

        :rtype: int
        :return: Integer representation of the Byte object
        """
        r = 0
        for i in range(8):
            r += int(self.bits[i]) * 2 ** (7 - i)

        return r

    def __setitem__(self, key, value):
        self.bits[7 - key] = value

    def __getitem__(self, item):
        return self.bits[7 - item]

    def __str__(self):
        """

        :return: hexadecimal Representation as a String object
        """
        h = hex(self)
        h = h[2:]
        if len(h) == 1:
            h = '0' + h
        return '{' + h + '}'

    def __add__(self, other):
        """
        Addition is the bitwise XOR of self and other

        :rtype: Byte
        :type other: Byte
        :param other: Byte object added to self
        :return: sum of two Bytes as the bitwise XOR operation
        """
        new = Byte()
        for i in range(8):
            new[i] = str(int(self[i]) ^ int(other[i]))

        return new

    def __mul__(self, other):
        """
        Multiplication of self and other in a finite field is multiplication modulo an irreducible polynomial
        In the case of Rijndael's finite field this polynomial is {01}{1b}

        :rtype: Byte
        :type other: Byte
        :param other: Byte to multiply self with
        :return: returns the calculated value as Byte object
        
        modification of the peasant's algorithm
        a and b are the multiplicands; p will be the product, initialized to 0
        at the start and the end, and the start and end of each iteration, this invariant is true: ab + p is the product
        when the algorithm terminates, a or b will be 0 so p will contain the product
        """
        a = self.__index__()
        b = other.__index__()
        p = 0
        for i in range(8):
            if b % 2:
                p ^= a
            b = b >> 1
            # keep track of the leftmost bit of a
            carry = 0
            if a >= 128:
                carry = 1
            a = (a << 1) % 256
            if carry:
                a ^= 0x1b

        # formatting the hex value to fit the param inp of __init__()
        h = hex(p)
        h = h[2:]
        if len(h) == 1:
            h = '0' + h

        return Byte(h)

    def __pow__(self, power, modulo=None):
        new = Byte('01')
        for i in range(power):
            new = new * self

        return new

    def __eq__(self, other):
        if type(other) == Byte:
            return self.__index__() == other.__index__()
        else:
            raise TypeError("can't compare Byte with " + type(other))

"""
a = Byte('f0')
b = Byte('ff')
c=a+b
print(c)

a = Byte('53')
b = Byte('ca')
print(a*b)

"""
