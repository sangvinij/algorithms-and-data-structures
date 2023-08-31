import array

arr = array.array("f", (1.0, 1.5, 2.0, 2.5))

print(arr)


def move_zeros_to_end(lst):
    zero_index = 0
    for index, value in enumerate(lst):
        if value != 0:
            lst[zero_index] = value
            if zero_index != index:
                lst[index] = 0
            zero_index += 1

    return lst


print(move_zeros_to_end([8, 0, 3, 0, 12]))
