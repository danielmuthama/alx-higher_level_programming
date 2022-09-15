#!/usr/bin/python3

"""a class Node that defines a node of a singly linked list
with private instance attributes and properties which
are accessed and changed by getters and setters respectively"""


class Node:
    """"
    Node (class): defines a node of a singly linked
    list raise error if type is not int or
    size is less than zero.
    Attributes:
        data (int): specifies the data
        next_node(): specifies the next node in the SLL
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is None) or (isinstance(value, Node) is True):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

    def __str__(self):
        return str(self.__data)


class SinglyLinkedList:
    """"
    SinglyLinkedList (class): defines a singly linked
    list with a private instance attribute: head
    Attributes:
        head (Node): specifies the head of the list
        sorted_insert (): method that inserts new nodes into
        the proper sorted position in the SLL (ascending order)
    """

    def __init__(self, data=None):
        self.__head = None
        self.__tail = None

        if data is not None:
            self.sorted_insert(data)

    def sorted_insert(self, value):
        if self.__head is None:
            self.__tail = self.__head = Node(value)
        else:
            self.__tail.next_node = Node(value)
            self.__tail = self.__tail.next_node
        return self.__tail

    def __len__(self):
        count = 0
        node = self.__head
        while node:
            count += 1
            node = node.next_node
        return count

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(tmp.data)
            tmp = tmp.next_node
        v = [str(val) for val in sorted(values)]
        return ('\n'.join(v))
