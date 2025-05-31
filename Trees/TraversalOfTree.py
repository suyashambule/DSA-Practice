# Traversal of Tree 

def preorder(root):
    if root is None:
        return 
    print(root.data, end=' ')
    for child in root.children:
        preorder(child)
def postorder(root):
    if root is None:
        return 
    for child in root.children:
        postorder(child)
    print(root.data, end=' ')
