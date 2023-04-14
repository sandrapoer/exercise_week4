# QUESTION NR 1

# QUESTION NR 2

# QUESTION NR 3

# QUESTION NR 4

# QUESTION NR 5

# QUESTION NR 6

# QUESTION NR 7

"""
Exercise template for exercise 04 linked lists
"""


# singly linked list
# node class of the singly linked list
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

    def __str__(self):
        return str(self.data)


# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the SLLNode class
        node = SLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = node
        else:  # if it is not empty, we need to find the last node and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            # set the pointer of the last node to the new node
            current.next = node
        self.size += 1  # increase the size of the list

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    """
    Exercise part 1,2,3,4

    Implement the given methods below according to the requirements in the exercise sheet.
    Make sure to return the correct values.
    """

    def insert_node(self, prev_node_data, new_node_data):
        return

    def clear(self):
        return

    def get_data(self, data):
        return

    def delete_node(self, data):
        return


"""
Exercise part 5

Implement a doubly linked list according to the exercise sheet.
You can copy the code from the singly linked list and modify it.
"""


class DLLNode:
    """Implement the node of the doubly linked list here"""


class DoublyLinkedList:
    """Implement the doubly linked list and its methods here"""


"""
Exercise Part 5 and 7:
Complete the classes below to implement a stack and queue data structure. You are free to use built-in
methods but you have to complete all methods below. Always return the correct data type according
to the exercise sheet
"""


class MyStack:

    def push(self, element):
        return

    def pop(self):
        return

    def top(self):
        return

    def size(self):
        return


class MyQueue:

    def push(self, element):
        return

    def pop(self):
        return

    def show_left(self):
        return

    def show_right(self):
        return

    def size(self):
        return