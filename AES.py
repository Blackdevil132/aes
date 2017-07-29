

class AES():
    # input: sequences of 128 bits (blocks)
    # output: sequences of 128 bits (blocks)
    def __init__(self, k, b=4):
        self.n_k = k
        self.n_b = b
        self.n_r = getRounds(k, b)
        self.k = ''
        self.plaintext = ''

    def setKey(self, key):
        self.key = key

    def setPlaintext(self, text):
        self.plaintext = text

    def run(self):
        pass