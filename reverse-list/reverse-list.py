"""Reverse List

Given a list, reverse it in place.

Example:

    >>>lst = [1, 2, 3, 4, 5]
    >>>reverse_list(lst)
    [5, 4, 3, 2, 1]

"""


def reverse_list(lst):
    """Reverse a list in place

    Returns list to allow for chaining"""
    for i in range(len(lst) / 2):
        temp = lst[i]
        lst[i] = lst[-(i + 1)]
        lst[-(i + 1)] = temp
    return lst
