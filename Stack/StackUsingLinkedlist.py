class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.head = None 
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def pop(self):
        if self.head is None:
            return None
        popped_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped_data

    def is_empty(self):
        return self.head is None

    def get_size(self):
        return self.size
