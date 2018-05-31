"""Huffman Decoding

Given the root node of a Huffman tree and an encoded string, return the
decoded string.

Background:

    With Huffman encoding, strings can be converted to a non-fixed number of
    ones and zeroes by storing data at the leaf nodes of a binary tree
    and describing utilizing the left and right pointers as decoding points
    where zero would mean go left and a one would mean go right.

    https://en.wikipedia.org/wiki/Huffman_coding

Example:

    >>> tree = Node(left=Node('G'),
                    right=Node(left=Node('A'),
                               right=Node(left=Node('T'),
                                          right=Node('C'))))
    >>> encoded = '0101101101011110'
    >>> huffman_decoding(tree, encoded)
    GATTACA

"""


class Node(object):
    """Binary Tree Node class"""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def huffman_decoding(tree, encoded):
    """Decode a string using the provided tree"""

    curr = tree
    decoded = ''

    for char in encoded:
        if char == '0':
            curr = curr.left
        else:
            curr = curr.right

        if curr.left is None:
            decoded = decoded + curr.data
            curr = tree

    return decoded
