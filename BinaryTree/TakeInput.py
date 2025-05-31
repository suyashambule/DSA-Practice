class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def take_input_binary_tree():
    data = int(input("Enter node data (-1 for no node): "))
    if data == -1:
        return None
    node = BinaryTreeNode(data)
    node.left = take_input_binary_tree()
    node.right = take_input_binary_tree()
    return node 


root = take_input_binary_tree()
