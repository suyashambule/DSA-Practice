class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def print_tree(node, level=0):
    print("  " * level + str(node.data))
    for child in node.children:
        print_tree(child, level + 1)


root = Node(1)
child1 = Node(2)
child2 = Node(3)

root.children.append(child1)
root.children.append(child2)

child1.children.append(Node(4))
child1.children.append(Node(5))


print_tree(root)
