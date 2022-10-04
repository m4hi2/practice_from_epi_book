def parity_brute_force(x):
    """This implementation of the function checks every bit
    of the word to calculate parity.
    """
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parity(x):
    """This implementation only counts set bits.
    As in the bits that are only 1.
    """
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # drops the lowest set bit
    return result


for i in range(10):
    print(f"{bin(i)} : {parity(i)}")
