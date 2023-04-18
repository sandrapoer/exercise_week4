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
        prev_node = self.head
        while prev_node is not None:
            if prev_node.data == prev_node_data:
                new_node = SLLNode(new_node_data)
                new_node.next = prev_node.next
                prev_node.next = new_node
                self.size += 1
                return
        return False

    def clear(self):
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None
        self.size = 0
        return

    def get_data(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node.data
            node = node.next
        return False

    def delete_node(self, data):
        # If Data is in Head Node
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1
            return

        prev_node = self.head
        node_to_delete = prev_node.next
        while node_to_delete is not None:
            if node_to_delete.data == data:
                temp = node_to_delete
                prev_node.next = node_to_delete.next
                temp = None
                self.size -= 1
                return
            prev_node = node_to_delete
            node_to_delete = node_to_delete.next
        return


"""
Exercise part 5
Implement a doubly linked list according to the exercise sheet.
You can copy the code from the singly linked list and modify it.
"""


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node
        self.previous = None  # pointer to the previous node

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Important to implement Tail everywhere!!!!!!!
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the SLLNode class
        node = DLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = node
        else:  # if it is not empty, we need to find the last node and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            # set the pointer of the last node to the new node
            current.next = node
            node.previous = current
            self.tail = node
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
        prev_node = self.head
        while prev_node is not None:
            if prev_node.data == prev_node_data:
                new_node = DLLNode(new_node_data)
                new_node.next = prev_node.next
                new_node.previous = prev_node
                prev_node.next = new_node
                next_node = new_node.next
                if next_node is not None:
                    next_node.previous = new_node
                    self.tail = new_node
                self.size += 1
                return
        return False

    def clear(self):
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None
        self.size = 0
        return

    def get_data(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node.data
            node = node.next
        return False

    def delete_node(self, data):
        # If Data is in Head Node
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1
            return

        if self.tail.data == data:  # Important to implement Tail everywhere!!!!!!!
            temp = self.tail
            self.tail = self.tail.previous
            temp
            None
            self.size -= 1
            return

        prev_node = self.head
        node_to_delete = prev_node.next
        while node_to_delete is not None:
            if node_to_delete.data == data:
                temp = node_to_delete
                prev_node.next = node_to_delete.next
                next_node = node_to_delete.next
                # if next_node is not None:
                #     next_node.previous = prev_node
                temp = None
                self.size -= 1
                return
            prev_node = node_to_delete
            node_to_delete = node_to_delete.next
        return


"""
Exercise Part 5 and 7:
Complete the classes below to implement a stack and queue data structure. You are free to use built-in
methods but you have to complete all methods below. Always return the correct data type according
to the exercise sheet
"""


class MyStack(DoublyLinkedList):

    def push(self, element):
        self.append(element)
        return

    def pop(self):
        pop_node = self.tail
        self.tail = self.tail.previous
        self.size -= 1
        return pop_node

    def top(self):
        return self.tail

    def bottom(self):
        return self.head

    def size(self):
        return self.size


class MyQueue(DoublyLinkedList):

    def push(self, element):
        self.append(element)
        return

    def pop(self):
        pop_node = self.head
        self.head = self.head.next
        self.size -= 1
        return pop_node

    def show_left(self):
        return self.head

    def show_right(self):
        return self.tail

    def size(self):
        return self.size
