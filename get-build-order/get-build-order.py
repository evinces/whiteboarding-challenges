"""Get Build Order

Given a dependency structure for a series of modules, and a given module,
determine the correct build order for the modules. Challenge includes choosing
the data structure of the incoming dependencies.

For help visulazing, consider the following statements true:

* Module A depends on modules B and C.
* Module B depends on modules C and D.
* Module D depends on modules E and F.
* Modules C, E and F depend on nothing.


Example:

    >>>dependencies = {
    ...    "A": ["B", "C"],
    ...    "B": ["C", "D"],
    ...    "C": [],
    ...    "D": ["E", "F"],
    ...    "E": [],
    ...    "F": []
    ...}

    >>>get_build_order(dependencies, "A")
    ["F", "E", "D", "C", "B", "A"]

    >>>get_build_order(dependencies, "B")
    ["F", "E", "D", "C", "B"]

"""


def get_build_order(dependencies, module):
    """Get the build order of dependencies for a given module"""

    order = []
    queue = Queue()
    queue.enqueue(module)
    seen = set(queue)

    while queue:
        module = queue.dequeue()
        order.append(module)

        for dependency in dependencies[module]:
            if dependency not in seen:
                queue.enqueue(dependency)
                seen.add(dependency)

    return order[::-1]


# Below is not part of the challenge

class LinkNode(object):
    """Linked List Node class"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue(object):
    """Queue class"""

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Add an item to the queue"""

        node = LinkNode(data)

        if self.is_empty():
            self.head = node
        elif self.tail == self.head:
            self.head.next = node
        else:
            self.tail.next = node

        self.tail = node

    def dequeue(self):
        """Remove an item from the queue"""

        if self.is_empty():
            return

        data = self.head.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return data

    def peek(self):
        """Preview the next data in the queue"""

        return self.tail.data

    def is_empty(self):
        """Return True if queue is empty"""

        return self.head is None
