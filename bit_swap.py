# Implement code that takes an input a 64-bit integer and swaps the bit at
# indices i and j

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


print(bin(swap_bits(241, 2, 7)))
