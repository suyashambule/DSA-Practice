class Node:
    def __init__(self, value):
        self.data=value
        self.next=None 
    
    def length_list(head):
        count=0
        temp=head
        while temp is not None:
            count+=1
            temp=temp.next
            return count