from tools.datatypes.Byte import Byte


class State:
    def __init__(self):
        """
        State s represents 4 rows of bytes, each containing Nb bytes
        Byte b = s[r, c] where r is the row of the Byte and c the column 
        """
        self.Nb = 4
        self.matrix = [[Byte() for j in range(self.Nb)] for i in range(4)]

    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __eq__(self, other):
        if type(other) != State:
            raise TypeError(type(other) + " can not be compared with State.")
        ret = True
        for r in range(4):
            for c in range(self.Nb):
                ret &= (self.matrix[r][c] == other.matrix[r][c])
        return ret


    def __str__(self):
        s = ''
        for r in range(4):
            for c in range(self.Nb):
                s += str(self.matrix[r][c])
            s += '\n'

        return s

"""
s = State()
s[0][0] = Byte('01')
s[0][1] = Byte('ff')
print(s)
"""