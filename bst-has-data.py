"""BST Has Data

Given the root of a binary search root node and some data, determine if that
data is in the tree.

Example:

    >>> root = Node(4, Node(3, Node(1)), Node(7, Node(6), Node(9)))

            (4)
           /  \
         (3)  (7)
        /    /  \
      (1)  (6)  (9)

    >>> bst_has_data(root, 3)
    True

    >>> bst_has_data(root, 5)
    Flase

"""


class Node(object):
    """Binary Search Tree Node class"""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bst_has_data(root, data):
    """Determine if BST has given data"""

    curr = root

    while curr:
        if curr.data == data:
            return True
        if curr.data < data:
            curr = curr.right
        else:
            curr = curr.left

    return False
