from common import *
def middleNode(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow