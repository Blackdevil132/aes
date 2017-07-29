from tools.Byte import Byte


def seqToByteArray(seq):
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


s = '00110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011'
a = seqToByteArray(s)
for i in a:
    print(str(i), end='')