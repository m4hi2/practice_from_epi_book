# Test if x is a power of 2, i.e., evaluates to true for x = 1, 2, 4, 8,..., false for
# all other values

def is_power_of_2(x):
    if (x & x - 1):
        return False

    return True


for i in range(100):
    print(f"{i} :: {is_power_of_2(i)}")
