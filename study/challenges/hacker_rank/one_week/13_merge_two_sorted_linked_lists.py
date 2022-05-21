#!/bin/python3

import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


"""
1 -> 3 -> 7 -> null
1 -> 2 -> null

0    1    2    3
V
1 -> 2 -> 3 -> null

0    1    2
V
3 -> 4 -> null

Head : 1 <= 3 ? 1 : 3

H
1 -> 2 -> 3 -> 3 -> 4 -> null

"""


def mergeLists(head1, head2):
    new_head = None
    if head1 and head2:
        if head1.data <= head2.data:
            new_head = head1
            head1 = head1.next
        else:
            new_head = head2
            head2 = head2.next

    elif head1 and not head2:
        new_head = head1
    else:
        new_head = head2

    pointer = new_head
    while head1 or head2:
        if head1:
            print("head1", head1.data)
        if head2:
            print("head2", head2.data)
        if head1 and (not head2 or head1.data <= head2.data):
            pointer.next = head1
            head1 = head1.next
        elif head2 and (not head1 or head1.data > head2.data):
            pointer.next = head2
            head2 = head2.next

        pointer = pointer.next

    return new_head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
