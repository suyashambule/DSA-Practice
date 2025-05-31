# Height of tree
def heightOftree(root):
    if root is None:
        return 0
    max_height = 0
    for child in root.children:
        child_height = heightOftree(child)
        max_height = 1+max(max_height, child_height)
    return max_height