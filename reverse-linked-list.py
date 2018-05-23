"""Reverse Linked List

Given a singly-linked-list head node, reverse the list in place.

Example:

    >>> head = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(head)
    >>> head
    <Node data: 3, next: <Node data: 2, next: <Node data: 1, next: None>>>

"""


class Node(object):
    """A Linked List Node class"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<Node data: {}, next: {}>".format(self.data, self.next)


def reverse_linked_list(head):
    """Reverse a linked list in place"""

    tail = head
    while tail.next:
        curr = tail.next
        tail.next = curr.next
        curr.next = head
        head = curr
