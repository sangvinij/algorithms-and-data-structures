# bubble sort for O(n**2)
def bubble_sort(sequence):
    list_length = len(sequence) - 1
    for i in range(list_length):
        no_swaps = True
        for j in range(list_length - i):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
                no_swaps = False
        if no_swaps:
            return sequence
    return sequence


lst = [412, 12, 2, 33, 1241, 21, 451]

print(bubble_sort(lst))


# insertion sort for O(n**2)
def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        value = sequence[i]

        while i > 0 and sequence[i - 1] > value:
            sequence[i] = sequence[i - 1]
            i = i - 1
        sequence[i] = value

    return sequence


print(insertion_sort(lst))


# merge sort for O(n * log n)
def merge_sort(sequence):
    if len(sequence) <= 1:
        return sequence

    mid = len(sequence) // 2
    left_half = sequence[:mid]
    right_half = sequence[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(merge_sort(lst))
