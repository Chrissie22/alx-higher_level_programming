#!/usr/bin/python3
"""Defines a node of a singly linked list"""


class Node:
    """Defines a node."""

    def __init__(self, data, next_node=None):
        """Initializes a Node instance"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets/sets data"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets/sets a next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes an instance of SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct soreted position in the list
        (increasing order)
        """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            ptr = self.__head
            while (ptr.next_node is not None and
                    ptr.next_node.data < value):
                ptr = ptr.next_node
            new.next_node = ptr.next_node
            ptr.next_node = new

    def __str__(self):
        """Prints the entire list, one node number by line."""
        val = []
        ptr = self.__head
        while ptr is not None:
            val.append(str(ptr.data))
            ptr = ptr.next_node
        return ('\n'.join(val))
