from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


level_order(root)

