
# 🧩 HashMap - Complete README Guide

A **HashMap (Dictionary in Python)** is a data structure that maps keys to values for efficient lookup.

---

## 📌 Key Operations

| Operation     | Time Complexity |
|---------------|------------------|
| Insert        | O(1) avg         |
| Delete        | O(1) avg         |
| Search        | O(1) avg         |

---

## 🧠 HashMap in Python

```python
# Creating a hashmap
map = {}

# Inserting
map["apple"] = 10

# Accessing
print(map["apple"])

# Updating
map["apple"] += 1

# Deleting
del map["apple"]

# Checking existence
if "banana" in map:
    print("Exists")
```

---

## 🎯 Use Cases

- Counting elements (frequency maps)
- Caching (memoization)
- Hashing for fast lookup
- Mapping relationships

---

## 🧪 Sample Problem: First Unique Character

```python
def firstUniqChar(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1
```

---
