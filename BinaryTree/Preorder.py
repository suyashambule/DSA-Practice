def pre_order_traversal(root):
    if root is None:
        return []
    
    result = []
    result.append(root.data)  
    result.extend(pre_order_traversal(root.left))  
    result.extend(pre_order_traversal(root.right))  
    
    return result