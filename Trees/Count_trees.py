# Nodes in Trees
def count_trees(root):
    if(root==None):
        return
    numberOfNodes=1

    for eachChild in root.children:
        numberOfNodes+=count_trees(eachChild)

