
# 🌐 Graphs - Complete README Guide

Graphs are data structures that consist of a set of **nodes (vertices)** connected by **edges**.

---

## 📌 Types of Graphs

| Type             | Description                                 |
|------------------|---------------------------------------------|
| Directed         | Edges have a direction (A → B)              |
| Undirected       | Edges are bidirectional (A — B)             |
| Weighted         | Edges have weights/costs                    |
| Unweighted       | No weights on edges                         |
| Cyclic           | Contains cycles                             |
| Acyclic          | No cycles (e.g., DAG - Directed Acyclic)    |
| Connected        | Every node reachable from any other         |
| Disconnected     | Not all nodes are connected                 |

---

## 🧠 Representation

### 🔹 Adjacency List
```python
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
```

### 🔹 Adjacency Matrix
```python
# 0: no edge, 1: edge exists
matrix = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
```

---

## 🔍 Traversal Techniques

### BFS (Breadth-First Search)
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])
```

### DFS (Depth-First Search)
```python
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

---

## 🔧 Common Graph Problems

- Graph Traversals (DFS, BFS)
- Topological Sort
- Detect Cycles
- Shortest Path (Dijkstra, BFS)
- Minimum Spanning Tree (Prim’s, Kruskal’s)
- Number of Connected Components
- Bipartite Graph Check

---
