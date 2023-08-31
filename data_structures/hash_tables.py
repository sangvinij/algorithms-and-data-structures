from collections import Counter


def count(a_string):
    a_dict = {}
    for char in a_string:
        if char in a_dict:
            a_dict[char] += 1
        else:
            a_dict[char] = 1

    return a_dict


def alt_count(a_string):
    return Counter(a_string)


def two_sum(a_list, target):
    a_dict = {}
    for index, value in enumerate(a_list):
        rem = target - value
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[value] = index
