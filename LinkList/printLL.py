class Node:
    def __init__(self,data):
        self.data= data
        self.next=None
    
    def print_LL(head):
        temp=head
        while temp is None:
            print(temp.data)
            temp = temp.next
            
