
# 🌳 Binary Tree - Complete README Guide

A **Binary Tree** is a tree where each node has at most 2 children: `left` and `right`.

---

## 📌 Types of Binary Trees

| Type                    | Description                               |
|-------------------------|-------------------------------------------|
| Full Binary Tree        | Every node has 0 or 2 children            |
| Complete Binary Tree    | All levels filled except possibly last    |
| Perfect Binary Tree     | All internal nodes have 2 children        |
| Balanced Binary Tree    | Height difference ≤ 1 at every node       |
| Binary Search Tree (BST)| Left < Root < Right                       |

---

## 🧠 Basic Implementation

```python
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
```

---

## 🔍 Traversals

- In-order: Left, Root, Right
- Pre-order: Root, Left, Right
- Post-order: Left, Right, Root
- Level-order: BFS

---

## 🧪 Sample Problem: Validate BST

```python
def isValidBST(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return isValidBST(root.left, low, root.val) and isValidBST(root.right, root.val, high)
```

---
