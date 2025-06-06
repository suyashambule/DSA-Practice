from collections import deque
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def print_level_wise(root):
    if root is None:
        return
    
    queue = deque([root])  
    
    while queue:
        current_node = queue.popleft() 
        print(f"{current_node.data}: ", end=" ")
        
        if current_node.left:
            print(f"L->{current_node.left.data}", end=", ")
            queue.append(current_node.left)  
        else:  
            print("L->None", end=", ")
        
        if current_node.right:
            print(f"R->{current_node.right.data}")
            queue.append(current_node.right) 
        else:
            print("R->None")


