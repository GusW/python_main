
class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def add_left_node(self, left_node):
        self.left_node = left_node

    def create_and_add_left_node(self, left_node_value):
        self.add_left_node(Node(left_node_value))

    def add_right_node(self, right_node):
        self.right_node = right_node

    def create_and_add_right_node(self, right_node_value):
        self.add_right_node(Node(right_node_value))


def solution1(root_node):
    # Depth-first tree search T(N) = O(N)
    # S(N) = O(logN)
    def _are_symmetric(root_left=root_node.left_node, root_right=root_node.right_node):
        if root_left is None and root_right is None:
            return True

        if root_left is None or root_right is None or root_left.value != root_right.value:
            return False

        return (_are_symmetric(root_left.left_node, root_right.right_node)
                and _are_symmetric(root_left.right_node, root_right.left_node))

    if root_node is None:
        return True

    return _are_symmetric()


if __name__ == "__main__":
    ex1 = Node(4)
    ex1.create_and_add_left_node(5)
    ex1.create_and_add_right_node(5)

    ex1.left_node.create_and_add_left_node(2)
    ex1.left_node.create_and_add_right_node(8)
    ex1.right_node.create_and_add_right_node(2)
    ex1.right_node.create_and_add_left_node(8)

    ex1.left_node.left_node.create_and_add_left_node(9)
    ex1.left_node.left_node.create_and_add_right_node(7)
    ex1.right_node.right_node.create_and_add_right_node(9)
    ex1.right_node.right_node.create_and_add_left_node(7)

    ex1.left_node.left_node.left_node.create_and_add_left_node(3)
    ex1.left_node.left_node.left_node.create_and_add_right_node(0)
    ex1.right_node.right_node.right_node.create_and_add_right_node(3)
    ex1.right_node.right_node.right_node.create_and_add_left_node(0)

    ex1.left_node.left_node.right_node.create_and_add_right_node(6)
    ex1.right_node.right_node.left_node.create_and_add_left_node(6)

    ex1.left_node.right_node.create_and_add_left_node(1)
    ex1.right_node.left_node.create_and_add_right_node(1)

    print(solution1(ex1))

    ex2 = Node(4)
    ex2.create_and_add_left_node(5)
    ex2.create_and_add_right_node(5)

    ex2.left_node.create_and_add_left_node(2)
    ex2.left_node.create_and_add_right_node(8)
    ex2.right_node.create_and_add_right_node(2)
    ex2.right_node.create_and_add_left_node(7)
    print(solution1(ex2))

    ex3 = Node(4)
    ex3.create_and_add_left_node(5)
    ex3.create_and_add_right_node(5)

    ex3.left_node.create_and_add_left_node(2)
    ex3.left_node.create_and_add_right_node(8)
    ex3.right_node.create_and_add_right_node(2)
    print(solution1(ex3))
