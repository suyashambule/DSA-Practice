from Trees import print_tree, TreesNode
from collections import deque

def take_better_input():
    data = int(input("Enter root data: "))
    root = TreesNode.Node(data)
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        num_children = int(input(f"Enter the number of children for node {current_node.data}: "))
        
        for i in range(num_children):
            child_data = int(input(f"Enter data for child {i + 1}: "))
            child_node = TreesNode.Node(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)

    return root
