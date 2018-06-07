"""Is Binary Tree

Given a subset of node relationships in a graph, determine if the
relationships can be represented as a binary tree.

Relationships will be represented as a list of tuple pairs where the
parent is the first element and the child is the second.

eg. [(parent_1, child_1), (parent_2, child_2), ... (parent_n, child_n)]

"""


def is_biniary_tree(node_pairs):
    """Determine if node_pairs can be represented as a binary tree"""

    root_count = 0
    tree = {}

    for parent, child in node_pairs:
        if parent not in tree:
            tree[parent] = {
                "left": child,
                "right": None,
                "parent": None
            }
            root_count += 1
        elif tree[parent]["left"] is None:
            tree[parent]["left"] = child
        elif tree[parent]["right"] is None:
            tree[parent]["right"] = child
        else:
            return False

        if child not in tree:
            tree[child] = {
                "left": None,
                "right": None,
                "parent": parent
            }
        elif tree[child]["parent"] is None:
            tree[child]["parent"] = parent
            root_count -= 1
        else:
            return False

    return root_count == 1
