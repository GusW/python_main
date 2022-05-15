class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        if not self.is_balanced():
            return str(self.data)+'*'

        return str(self.data)

    def traverse_preorder(self):
        print(self.data)

        if self.left:
            self.left.traverse_preorder()

        if self.right:
            self.right.traverse_preorder()

    def traverse_inorder(self):
        if self.left:
            self.left.traverse_inorder()

        print(self.data)

        if self.right:
            self.right.traverse_inorder()

    def traverse_postorder(self):
        if self.left:
            self.left.traverse_postorder()

        if self.right:
            self.right.traverse_postorder()

        print(self.data)

    def search(self, target):
        """binary search
           values to the left: lesser than parent
           values to the right: greater than parent
        """
        if self.data == target:
            print("Found it!")
            return self

        if self.data > target and self.left:
            return self.left.search(target)

        if self.data < target and self.right:
            return self.right.search(target)

        print("Value is not in tree")

    def find_min_node(self):
        return self.left.find_min_node() if self.left else self

    def find_max_node(self):
        return self.left.find_max_node() if self.right else self

    def add(self, data):
        if data == self.data:
            # Binary search trees do not contain duplicates
            return
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                return
            else:
                self.left.add(data)
                self.left = self.left.handle_imbalance()

        if data > self.data:
            if self.right is None:
                self.right = Node(data)
                return
            else:
                self.right.add(data)
                self.right = self.right.handle_imbalance()

    def delete(self, target):
        if self.data == target:
            if self.right and self.left:
                min_node = self.right.find_min_node()
                self.data = min_node.data
                self.right = self.right.delete(self.data)
                return self
            else:
                return self.right or self.left

        if target < self.data and self.left:
            self.left = self.left.delete(target)

        if target > self.data and self.right:
            self.right = self.right.delete(target)

        return self.handle_imbalance()

    def _left_height(self, height=0):
        return self.left.height(height+1) if self.left else height

    def _rigth_height(self, height=0):
        return self.right.height(height+1) if self.right else height

    def height(self, h=0):
        return max(self._left_height(h), self._rigth_height(h))

    def get_nodes_at_depth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self)
            return nodes

        if self.left:
            self.left.get_nodes_at_depth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        if self.right:
            self.right.get_nodes_at_depth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        return nodes

    def _get_height_left_right_diff(self):
        return self._left_height() - self._rigth_height()

    def is_balanced(self):
        return abs(self._get_height_left_right_diff()) < 2

    def handle_imbalance(self):
        if self._get_height_left_right_diff() > 1:
            # left imbalance
            if self.left._get_height_left_right_diff() > 0:
                # left imbalance
                return rotate_right(self)
            else:
                # right imbalance
                self.left = rotate_left(self.left)
                return rotate_right(self)

        if self._get_height_left_right_diff() < -1:
            # right imbalance
            if self.right._get_height_left_right_diff() < 0:
                # right imbalance
                return rotate_left(self)
            else:
                # left imbalance
                self.right = rotate_right(self.right)
                return rotate_left(self)

        return self

    def rebalance(self):
        if self.left:
            self.left.rebalance()
            self.left = self.left.handle_imbalance()
        if self.right:
            self.right.rebalance()
            self.right = self.right.handle_imbalance()


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def traverse_inorder(self):
        self.root.traverse_inorder()

    def traverse_preorder(self):
        self.root.traverse_preorder()

    def traverse_postorder(self):
        self.root.traverse_postorder()

    def search(self, target):
        return self.root.search(target)

    def add(self, data):
        self.root.add(data)
        self.root = self.root.handle_imbalance()
        return self.root

    def delete(self, target):
        self.root = self.root.delete(target)

    def height(self):
        return self.root.height()

    def get_nodes_at_depth(self, depth):
        return self.root.get_nodes_at_depth(depth)

    def rebalance(self):
        self.root.rebalance()
        self.root = self.root.handle_imbalance()

    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1) + (' '*(spacing+2)
                                        ).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.get_nodes_at_depth(depth, [])
            print((' '*offset) +
                  ''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')


def rotate_right(root):
    pivot = root.left
    root.left, pivot.right = pivot.right, root
    return pivot


def rotate_left(root):
    pivot = root.right
    root.right, pivot.left = pivot.left, root
    return pivot


def _build_binary_tree_1():
    node = Node(10)
    node.left = Node(5)
    node.right = Node(15)

    node.left.left = Node(2)
    node.left.right = Node(6)

    node.right.left = Node(13)
    node.right.right = Node(10000)

    return Tree(node, 'Foobar Tree')


def _build_binary_tree_2():
    tree = Tree(Node(50))
    tree.root.left = Node(25)
    tree.root.right = Node(75)
    tree.root.left.left = Node(10)
    tree.root.left.right = Node(35)
    tree.root.left.left.left = Node(5)
    tree.root.left.left.right = Node(13)
    tree.root.left.right.left = Node(30)
    tree.root.left.right.right = Node(42)

    return tree


def _build_binary_tree_3():

    tall_tree = Tree(Node(50), 'A Very Tall Tree')
    tall_tree.root.left = Node(25)
    tall_tree.root.right = Node(75)
    tall_tree.root.left.left = Node(10)
    tall_tree.root.left.right = Node(35)
    tall_tree.root.left.right.left = Node(30)
    tall_tree.root.left.right.right = Node(42)
    tall_tree.root.left.left.left = Node(5)
    tall_tree.root.left.left.right = Node(13)
    tall_tree.root.left.left.left.left = Node(2)

    short_tree = Tree(Node(50), 'A Very Short Tree')
    return tall_tree, short_tree


def _build_binary_tree_4():
    tree = Tree(Node(50))
    tree.root.left = Node(25)
    tree.root.right = Node(75)
    tree.root.left.left = Node(13)
    tree.root.left.right = Node(35)
    tree.root.left.right.right = Node(37)
    tree.root.right.left = Node(55)
    tree.root.right.right = Node(103)
    tree.root.left.left.left = Node(2)
    tree.root.left.left.right = Node(20)
    tree.root.right.left = Node(55)
    tree.root.right.right.right = Node(256)
    return tree


def _build_binary_tree_5():
    tree = Tree(Node(50))
    tree.root.left = Node(25)
    tree.root.right = Node(75)
    tree.root.right.left = Node(67)
    tree.root.right.right = Node(100)
    tree.root.right.right.right = Node(120)
    tree.root.right.right.left = Node(80)
    tree.root.right.right.left.right = Node(92)
    return tree


def _build_unbalanced_left_left():
    unbalanced_left_left = Tree(Node(30), 'UNBALANCED LEFT LEFT')
    unbalanced_left_left.root.left = Node(20)
    unbalanced_left_left.root.left.right = Node(21)
    unbalanced_left_left.root.left.left = Node(10)
    unbalanced_left_left.root.left.left.left = Node(9)
    unbalanced_left_left.root.left.left.right = Node(11)
    return unbalanced_left_left


def _build_unbalanced_right_right():
    unbalanced_right_right = Tree(Node(10), 'UNBALANCED RIGHT RIGHT')
    unbalanced_right_right.root.right = Node(20)
    unbalanced_right_right.root.right.left = Node(19)
    unbalanced_right_right.root.right.right = Node(30)
    unbalanced_right_right.root.right.right.left = Node(29)
    unbalanced_right_right.root.right.right.right = Node(31)
    return unbalanced_right_right


def _build_unbalanced_left_right():
    unbalanced_left_right = Tree(Node(30), 'UNBALANCED LEFT RIGHT')
    unbalanced_left_right.root.right = Node(31)
    unbalanced_left_right.root.left = Node(10)
    unbalanced_left_right.root.left.right = Node(20)
    unbalanced_left_right.root.left.left = Node(9)
    unbalanced_left_right.root.left.right.left = Node(19)
    unbalanced_left_right.root.left.right.right = Node(21)
    return unbalanced_left_right


def _build_unbalanced_right_left():
    unbalanced_right_left = Tree(Node(30), 'UNBALANCED RIGHT LEFT')
    unbalanced_right_left.root.left = Node(20)
    unbalanced_right_left.root.right = Node(40)
    unbalanced_right_left.root.right.left = Node(35)
    unbalanced_right_left.root.right.right = Node(45)
    unbalanced_right_left.root.right.left.right = Node(37)
    unbalanced_right_left.root.right.left.left = Node(33)
    return unbalanced_right_left


def _build_unbalanced_tree():
    tree = Tree(Node(50))
    tree.root.left = Node(25)
    tree.root.right = Node(75)
    tree.root.left.left = Node(10)
    tree.root.left.right = Node(35)
    tree.root.left.right.left = Node(30)
    tree.root.left.left.left = Node(5)
    tree.root.left.left.right = Node(13)
    tree.root.left.left.left.left = Node(2)
    tree.root.left.left.left.left.left = Node(1)
    return tree


if __name__ == "__main__":
    myTree = _build_binary_tree_1()
    found = myTree.search(10000)
    print(found.data)

    myOtherTree = _build_binary_tree_2()
    print("\n", "Preorder --> |", "\n")
    myOtherTree.traverse_preorder()
    print("\n", "| <-- Preorder")

    print("\n", "Inorder --> |", "\n")
    myOtherTree.traverse_inorder()
    print("\n", "| <-- Inorder")

    print("\n", "Postorder --> |", "\n")
    myOtherTree.traverse_postorder()
    print("\n", "| <-- Postorder")

    tall_tree, short_tree = _build_binary_tree_3()
    print("\n", "tall_tree: ", tall_tree.height())
    print("\n", "short_tree: ", short_tree.height())

    tree_depth = _build_binary_tree_4()
    print("\n", "tree elements at depth: ", [
          (node.data if node else None) for node in tree_depth.get_nodes_at_depth(3)])

    print("\n", "my tree is:")
    tree_depth.print('My tree')

    print("\n", "Adding 100 to my tree:")
    tree_depth.add(100)
    tree_depth.print('My tree')

    print("\n", "Adding 1 to my tree:")
    tree_depth.add(1)
    tree_depth.print('My tree')

    print("\n", "Adding 75 to my tree:")
    tree_depth.add(75)
    tree_depth.print('My tree')

    tree_to_remove = _build_binary_tree_5()
    print("\n", "my tree to remove is:")
    tree_to_remove.print('Tree to remove')

    print("\n", "Removing 75:")
    tree_to_remove.delete(75)
    tree_to_remove.print('Tree to remove')

    print("\n", "Removing root 50:")
    tree_to_remove.delete(50)
    tree_to_remove.print('Tree to remove')

    print("\n", "Unbalanced left left tree:")
    unbalanced_left_left = _build_unbalanced_left_left()
    unbalanced_left_left.print()
    unbalanced_left_left.root = rotate_right(unbalanced_left_left.root)
    print("\n", "balanced tree:")
    unbalanced_left_left.print()

    print("\n", "Unbalanced right right tree:")
    unbalanced_right_right = _build_unbalanced_right_right()
    unbalanced_right_right.print()
    unbalanced_right_right.root = rotate_left(unbalanced_right_right.root)
    print("\n", "balanced tree:")
    unbalanced_right_right.print()

    print("\n", "Unbalanced left right tree:")
    unbalanced_left_right = _build_unbalanced_left_right()
    unbalanced_left_right.print()
    unbalanced_left_right.root.left = rotate_left(
        unbalanced_left_right.root.left)
    unbalanced_left_right.root = rotate_right(unbalanced_left_right.root)
    print("\n", "balanced tree:")
    unbalanced_left_right.print()

    print("\n", "Unbalanced right left tree:")
    unbalanced_right_left = _build_unbalanced_right_left()
    unbalanced_right_left.print()
    unbalanced_right_left.root.right = rotate_right(
        unbalanced_right_left.root.right)
    unbalanced_right_left.root = rotate_left(unbalanced_right_left.root)
    print("\n", "balanced tree:")
    unbalanced_right_left.print()

    print("\n", "Deep unbalanced tee:")
    deep_unbalanced_tree = _build_unbalanced_tree()
    deep_unbalanced_tree.print()
    deep_unbalanced_tree.rebalance()
    print("\n", "balanced tree:")
    deep_unbalanced_tree.print()
