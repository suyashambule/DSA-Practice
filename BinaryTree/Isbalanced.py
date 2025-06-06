class BinaryTree:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

    def is_balanced(self, node):
        if node is None:
            return True, 0
        
        left_balanced, left_height = self.is_balanced(node.left)
        right_balanced, right_height = self.is_balanced(node.right)

        balanced = (
            left_balanced and  
            right_balanced and 
            abs(left_height - right_height) <= 1
        )
        height = max(left_height, right_height) + 1

        return balanced, height
