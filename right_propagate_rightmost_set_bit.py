# Right propagate the rightmost set bit in x, e.9., tums (01010000)2 to (01011111)2

def right_prop(number):
    right_most_set_bit = number & ~(number-1)

    while right_most_set_bit:
        right_most_set_bit >>= 1
        number |= right_most_set_bit
    return number


for i in range(80, 100):
    print(f"{bin(i)}  :: {bin(right_prop(i))}")
