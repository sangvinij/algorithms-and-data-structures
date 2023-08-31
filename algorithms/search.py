from bisect import bisect_left
from typing import Iterable, Any


# linear search for O(n)
def linear_search(sequence: Iterable, value: Any) -> bool:
    for i in sequence:
        if i == value:
            return True
    return False


lst = [1, 8, 32, 91, 5, 15, 9, 100, 3]
print(linear_search(lst, 91))


# Binary search for O(log n)
def binary_search(sequence, value):
    first = 0
    last = len(sequence) - 1
    while last >= first:
        mid = (first + last) // 2
        if sequence[mid] == value:
            return True
        elif value < sequence[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return False


lst2 = sorted(lst)
print(lst2)
print(binary_search(lst2, 91))


def alternative_binary_search(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False


print(alternative_binary_search(lst2, 2))
