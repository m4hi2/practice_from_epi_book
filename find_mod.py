# Compute x mod a power of two, e.g., returns 13 for 77 mod 64

def get_mod(numerator, denominator):
    return numerator & (denominator - 1)


print(get_mod(21, 16))
print(get_mod(21, 4))
print(get_mod(77, 64))
