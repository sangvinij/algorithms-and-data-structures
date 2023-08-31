def get_nod(value1, value2):
    while value1 != value2:
        if value1 > value2:
            value1 -= value2
        else:
            value2 -= value1

    return value1


def get_nod_fast(value1, value2):
    if value1 < value2:
        value1, value2 = value2, value1

    while value2 != 0:
        value1, value2 = value2, value1 % value2

    return value1


print(get_nod(18, 24))
print(get_nod_fast(18, 24))


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
