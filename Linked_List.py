class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def insert_back(self, value):
        new_node = Node(value, None)

        self.size += 1
        if self.size == 0:
            self.head = Node(value, None)

        self.tail = Node(value, None)

    def get(self. idx):
        pass

    def insert_at(self, idx, value):
        pass

    def remove(self, idx):
        pass

    def print(self):
        pass