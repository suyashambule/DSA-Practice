# 📘 Graph - Complete README Guide

Graphs are a non-linear data structure consisting of nodes (vertices) and edges connecting these nodes. They are used to model relationships between objects.

# 📌 What is a Graph?

A graph is a collection of vertices (nodes) connected by edges (links). Graphs can be directed (edges have direction) or undirected (edges have no direction).
Common representations:

Adjacency Matrix: A 2D array where matrix[i][j] indicates an edge between node i and j.
Adjacency List: A list where each node points to its neighbors.
🧠 General Graph Traversal

# Depth-First Search (DFS):

python
def dfs(node, visited):
if node not in visited:
visited.add(node)
for neighbor in graph[node]:
dfs(neighbor, visited)
Breadth-First Search (BFS):

python
from collections import deque

def bfs(start):
visited = set()
queue = deque([start])
visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 🧮 Example: Detect Cycle in a Directed Graph

python

    def has_cycle(graph):
    visited = set()
    recursion_stack = set()

    def dfs(node):
        visited.add(node)
        recursion_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in recursion_stack:
                return True
        recursion_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

# 🔍 Example Input:

python
graph = {
0: [1],
1: [2],
2: [0]
}
✅ Output:

python
True # Cycle exists (0 -> 1 -> 2 -> 0)
🧰 Common Graph Problems

Problem Description
Shortest Path (Dijkstra's/BFS) Find the shortest path between nodes
Topological Sorting Linear ordering of vertices in a DAG
Minimum Spanning Tree (Prim's/Kruskal) Connect all nodes with minimal weight
Strongly Connected Components (Kosaraju) Find groups of strongly connected nodes
Bipartite Graph Check Check if graph can be divided into two disjoint sets
🧠 Tips to Master Graphs

# Understand the representation (Adjacency List vs. Matrix)

Practice both DFS and BFS traversals
Learn standard algorithms like Dijkstra's, Prim's, and Kosaraju's
Visualize graphs using tools like Graphviz or draw them on paper

# 🎓 Good Practice Problems

Number of Islands - Leetcode 200
Course Schedule - Leetcode 207
Clone Graph - Leetcode 133
Network Delay Time - Leetcode 743
Word Ladder - Leetcode 127
