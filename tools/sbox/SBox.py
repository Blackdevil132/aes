import os


class SBox:
    def __init__(self, inverse=False):
        PATH = os.path.dirname(os.path.realpath(__file__))
        if inverse:
            self.PATH_SBOX = PATH + "/InvSBox.txt"
        else:
            self.PATH_SBOX = PATH + "/SBox.txt"

        self.box = self.initiate()

    def initiate(self):
        file = open(self.PATH_SBOX)
        s = file.read()
        file.close()

        sbox = ['' for i in range(16)]
        for i in range(16):
            sbox[i] = s[(32 * i):(32 * i + 32)]

        return sbox

    def __setitem__(self, key, value):
        raise PermissionError("Setting values not allowed.")

    def __getitem__(self, item):
        return self.box[item]
