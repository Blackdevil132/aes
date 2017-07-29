

def getRounds(k, b):
    """
    Gives back the number of rounds for the AES algorithm

    :type k: int
    :type b: int
    :rtype: int
    :param k:   (4, 6, 8)
    :param b:   (4)
    :return:    (10, 12, 14)
    """
    if k == 4 and b == 4:
        return 10
    elif k == 6 and b == 4:
        return 12
    elif k == 8 and b == 4:
        return 14
    else:
        raise ArithmeticError("Wrong Parameters!")


def shift(r, Nb):
    return r
