class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def search(head, value):
    temp = head
    index = 0
    while temp is not None:
        if temp.data == value:
            return index
        temp = temp.next
        index += 1
    return -1  

def create_ll(l1):
    head = None
    tail = None
    for value in l1:
        newNode = Node(value)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

# ✅ Store the head node
head = create_ll([1, 2, 3, 4, 5])

# ✅ Use the correct head reference
print(search(head, 3))  # Output: 2 (since index starts at 0)
