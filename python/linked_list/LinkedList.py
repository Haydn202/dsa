from Node import Node

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # O(1)
    def append(self, value):
        new_node = Node(value)
        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # O(n)
    def pop(self):
        if self.length == 0:
            return None
        current = self.head
        prev = self.head
        while current.next is not None:
            prev = current
            current = current.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current
    
    def pop_first(self):
        if self.length == 0:
            return None
        first = self.head
        self.head = self.head.next
        first.next = None
        return first

    # O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # def insert(self, index, value):

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


