class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search_bst(root, key):
        if root is None:
            return False
        
        if root.data == key:
            return True

        elif key < root.data:
            return BinaryNode.search_bst(root.left, key)
        
        else:
            return BinaryNode.search_bst(root.right, key)