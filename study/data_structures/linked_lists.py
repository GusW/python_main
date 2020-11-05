from collections import deque


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        res = deque()
        trav_node = self._head_node
        while trav_node:
            res.append(trav_node.data_val)
            trav_node = trav_node.next

        items_str = ', '.join(list(map(str, [val for val in res if val])))
        return f'[{items_str}]'

    # empty linked list O(n):
    def clear(self):
        trav_node = self._head_node
        self._head_node = None
        while trav_node:
            next_node = trav_node.next
            trav_node.next = None
            del trav_node
            self._size -= 1
            trav_node = next_node

    def _is_empty_list(self):
        return self._size == 0

    def _handle_add_to_empty_linked_list(self, new_node):
        if self._is_empty_list():
            self._head_node = self._tail_node = new_node
            return True

    def add(self, new_data):
        return self.add_tail(new_data)

    def add_head(self, new_data):
        new_node = Node(new_data)
        was_empty_list = self._handle_add_to_empty_linked_list(new_node)
        if not was_empty_list:
            new_node.next = self._head_node
            self._head_node = new_node

        self._size += 1

    def _catch_method_on_empty_list(self):
        if self._is_empty_list():
            raise Exception('Cannot perform this method on an empty list!')

    def _catch_method_on_index_out_of_bounds(self, index):
        if not (0 <= index <= len(self) - 1):
            raise Exception('Index out of bounds!')

    def peek_head(self):
        self._catch_method_on_empty_list()
        return self._head_node.data_val

    def peek_tail(self):
        self._catch_method_on_empty_list()
        return self._tail_node.data_val

    def remove_head(self):
        self._catch_method_on_empty_list()

        current_head_node = self._head_node
        target_head_node = current_head_node.next
        if len(self) == 1:
            del self._tail_node

        del current_head_node
        self._head_node = target_head_node

        self._size -= 1

    def remove_tail(self):
        self._catch_method_on_empty_list()

        current_tail_node = self._tail_node

        if len(self) == 1:
            del self._head_node
            self._head_node = None

        trav_node = self._head_node
        while trav_node:
            if trav_node.next == current_tail_node:
                trav_node.next = None
                self._tail_node = trav_node

            trav_node = trav_node.next

        del current_tail_node

        self._size -= 1


class SinglyLinkedList(LinkedList):

    def add_at(self, index, new_data):
        self._catch_method_on_index_out_of_bounds(index)

        if index == 0:
            return self.add_head(new_data)

        if index == len(self) - 1:
            return self.add_tail(new_data)

        new_node = Node(new_data)

        counter = 0
        current_node = self._head_node
        while current_node:
            if index == counter + 1:
                new_node.next = current_node.next
                current_node.next = new_node
                self._size += 1
                return

            current_node = current_node.next
            counter += 1

    def add_tail(self, new_data):
        new_node = Node(new_data)
        was_empty_list = self._handle_add_to_empty_linked_list(new_node)
        if not was_empty_list:
            self._tail_node.next = new_node
            self._tail_node = new_node

        self._size += 1

    # O(n)
    def remove(self, data):
        if self._head_node.data_val == data:
            return self.remove_head()

        if self._tail_node.data_val == data:
            return self.remove_tail()

        trav_node = self._head_node
        while trav_node.next:
            next_node = trav_node.next
            if next_node.data_val == data:
                trav_node.next = next_node.next
                del next_node
                self._size -= 1
                return

            trav_node = trav_node.next

    def remove_at(self, index):
        self._catch_method_on_index_out_of_bounds(index)

        if index == 0:
            return self.remove_head()

        if index == len(self) - 1:
            return self.remove_tail()

        counter = 0
        current_node = self._head_node
        while current_node:
            if index == counter + 1:
                next_node = current_node.next
                current_node.next = next_node.next
                del next_node
                self._size -= 1
                return

            current_node = current_node.next
            counter += 1


class DoublyLinkedList(LinkedList):

    def add_at(self, index, new_data):
        self._catch_method_on_index_out_of_bounds(index)

        if index == 0:
            return self.add_head(new_data)

        if index == len(self) - 1:
            return self.add_tail(new_data)

        new_node = Node(new_data)

        counter = 0
        current_node = self._head_node
        while current_node:
            if index == counter + 1:
                next_node = current_node.next
                new_node.next = next_node
                new_node.prev = current_node
                next_node.prev = new_node
                current_node.next = new_node
                self._size += 1
                return

            current_node = current_node.next
            counter += 1

    def add_tail(self, new_data):
        new_node = Node(new_data)
        was_empty_list = self._handle_add_to_empty_linked_list(new_node)
        if not was_empty_list:
            new_node.prev = self._tail_node
            self._tail_node.next = new_node
            self._tail_node = new_node

        self._size += 1

    # O(n)
    def remove(self, data):
        if self._head_node.data_val == data:
            return self.remove_head()

        if self._tail_node.data_val == data:
            return self.remove_tail()

        trav_node = self._head_node
        while trav_node.next:
            next_node = trav_node.next
            if next_node.data_val == data:
                trav_node.next = next_node.next
                next_node.next.prev = trav_node
                del next_node
                self._size -= 1
                return

            trav_node = trav_node.next

    def remove_at(self, index):
        self._catch_method_on_index_out_of_bounds(index)

        if index == 0:
            return self.remove_head()

        if index == len(self) - 1:
            return self.remove_tail()

        counter = 0
        current_node = self._head_node
        while current_node:
            if index == counter + 1:
                next_node = current_node.next
                current_node.next = next_node.next
                next_node.next.prev = current_node
                del next_node
                self._size -= 1
                return

            current_node = current_node.next
            counter += 1


def main_singly():
    print(' >>> SINGLY LINKED LIST')
    s = SinglyLinkedList()
    print(' >>> add 1')
    s.add(1)
    print(len(s))
    print(s)
    print(' >>> remove head')
    s.remove_head()
    print(len(s))
    print(s)
    print(' >>> add 3')
    s.add(3)
    print(len(s))
    print(s)
    print(' >>> add 5')
    s.add(5)
    print(len(s))
    print(s)
    print(' >>> remove 3')
    s.remove(3)
    print(len(s))
    print(s)
    print(' >>> remove 5')
    s.remove(5)
    print(len(s))
    print(s)
    print(' >>> add 7')
    s.add(7)
    print(len(s))
    print(s)
    print(' >>> add 2')
    s.add(2)
    print(len(s))
    print(s)
    print(' >>> add 9')
    s.add(9)
    print(len(s))
    print(s)
    print(' >>> add 9')
    s.add(9)
    print(len(s))
    print(s)
    print(' >>> add 19')
    s.add(19)
    print(len(s))
    print(s)
    print(' >>> add 29')
    s.add(29)
    print(len(s))
    print(s)
    print(' >>> add 25 at index 3')
    s.add_at(3, 25)
    print(len(s))
    print(s)
    print(' >>> remove 9')
    s.remove(9)
    print(len(s))
    print(s)
    print(' >>> remove at 4')
    s.remove_at(4)
    print(len(s))
    print(s)
    print(' >>> remove head')
    s.remove_head()
    print(len(s))
    print(s)
    print(' >>> remove tail')
    s.remove_tail()
    print(len(s))
    print(s)
    print(' >>> clear')
    s.clear()
    print(len(s))
    print(s)


def main_doubly():
    print(' >>> DOUBLY LINKED LIST')
    s = DoublyLinkedList()
    print(' >>> add 1')
    s.add(1)
    print(len(s))
    print(s)
    print(' >>> remove head')
    s.remove_head()
    print(len(s))
    print(s)
    print(' >>> add 3')
    s.add(3)
    print(len(s))
    print(s)
    print(' >>> add 5')
    s.add(5)
    print(len(s))
    print(s)
    print(' >>> remove 3')
    s.remove(3)
    print(len(s))
    print(s)
    print(' >>> remove 5')
    s.remove(5)
    print(len(s))
    print(s)
    print(' >>> add 7')
    s.add(7)
    print(len(s))
    print(s)
    print(' >>> add 2')
    s.add(2)
    print(len(s))
    print(s)
    print(' >>> add 9')
    s.add(9)
    print(len(s))
    print(s)
    print(' >>> add 9')
    s.add(9)
    print(len(s))
    print(s)
    print(' >>> add 19')
    s.add(19)
    print(len(s))
    print(s)
    print(' >>> add 29')
    s.add(29)
    print(len(s))
    print(s)
    print(' >>> add 25 at index 3')
    s.add_at(3, 25)
    print(len(s))
    print(s)
    print(' >>> remove 9')
    s.remove(9)
    print(len(s))
    print(s)
    print(' >>> remove at 4')
    s.remove_at(4)
    print(len(s))
    print(s)
    print(' >>> remove head')
    s.remove_head()
    print(len(s))
    print(s)
    print(' >>> remove tail')
    s.remove_tail()
    print(len(s))
    print(s)
    print(' >>> clear')
    s.clear()
    print(len(s))
    print(s)


if __name__ == '__main__':
    main_singly()
    main_doubly()
