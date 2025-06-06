class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

    def list_to_bst(l):
        if len(l) == 0:
            return None
        
        mid = len(l) // 2

        root = Node(l[mid])
        root.left = Node.list_to_bst(l[:mid])
        root.right = Node.list_to_bst(l[mid + 1:])
        return root
    
