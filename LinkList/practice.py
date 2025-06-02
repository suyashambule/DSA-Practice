class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def create_ll(l1):
        head=None
        tail=None
        for value in l1:
            newNode= Node(value)
            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        return head
    
