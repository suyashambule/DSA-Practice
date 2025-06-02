class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def take_input():
    head = None
    tail = None
    while True:
        value = int(input("Enter the value of Node (1 to stop): "))
        if value == 1:
            break
        newNode = Node(value)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def print_ll(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head = take_input()
print_ll(head)
