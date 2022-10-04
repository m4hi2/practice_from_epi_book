def count_bits(x):
    num_bits = 0
    while x:
        num_bits += 1
        x = x >> 1

    return num_bits


for i in range(10):
    print(count_bits(i))
