class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    

    def insert_at_head(head,value):
        if head is not None:
            newNode=Node(value)
            newNode.next=head
            head = newNode
        return head
    
    def insert_at_tail(head,data):
        newNode = Node(data)
        if(head is None):
            return newNode 
    
        temp = head
        while(temp.next != None):
            temp = temp.next

        temp.next = newNode

        return head
    
    def insert_at_position(head,data,position):
        if head is None:
            return Node(data)
        
        NewNode = Node(data)
        temp=head
        count = 0

        while (head is None and count < position-1):
            temp = temp.next
            count += 1
        NewNode.next = temp.next
        temp.next = NewNode

        return head
