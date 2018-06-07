"""Find Equilibrum

Given a list of unordered integers, find the eqilibrium point where the
sum of all ints to the left equals the sum of all ints to the right.

Notes:

    - Return the index of the equilibrium
    - If there is no exact equilibrium point, return the closest

Example:

    >>> nums = [2, 4, 3, 1, 2, 1, 5]
    >>> find_equilibrium(nums)
    2

    >>> nums = [2, 1, 3]
    >>> find_equilibrium(nums)
    1

Explaination:

    given [2, 4, 3, 1, 2, 1, 5]
    sum([2, 4, 3]) = 9
    sum([1, 2, 1, 5]) = 9
    return 2 (the index of the last element in the first half of the list)

"""


def find_equilibrium(nums):
    """Find the equilibrium point of a list of ints"""

    left, right = 0, len(nums) - 1
    sum_left, sum_right = nums[left], nums[right]

    while left < right - 1:
        if sum_left < sum_right:
            left += 1
            sum_left += nums[left]
        else:
            right -= 1
            sum_right += nums[right]

    return left
