from common import *
from Lenglth_list import lenthOfLL

Headodd=createLLFromList([1, 2, 3, 4, 5])
Headeven=createLLFromList([2, 4, 6, 8, 10,12])

def middleNode(head):
    if head is None or head.next is None:
        return head
    len=lenthOfLL(head)
    middle=len//2
    temp=head
    count=0
    while count < middle:
        temp = temp.next
        count += 1
    return temp
