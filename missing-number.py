"""Missing Number

Given a list of numbers that contains two of each integer from 1 through n,
find the number that is missing from the list.

Extra credit:

    Write the function without loops.

Example:

    >>> nums = [3, 2, 4, 2, 1, 1, 4]
    >>> missing_number(nums)
    3

"""


def missing_number(nums):
    """Return the missing int from nums"""

    n = (len(nums) + 1) / 2
    target_sum = (n + 1) * (n / 2)

    if n % 2 == 1:
        target_sum += (n + 1) / 2

    return target_sum - sum(nums)
