class GraphUsingEdgeList:
    def __init__(self):
        self.V = []
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.V:
            self.V.append(vertex)
        else:
            print(f"Vertex is already present: {vertex}")

    def add_edge(self, source, destination, weight=1):
        if source in self.V and destination in self.V:
            self.edges.append((source, destination, weight))
        else:
            print("One or both vertices are not present in the graph")

    def display(self):
        print("Vertices:", self.V)
        print("Edges:")
        for source, destination, weight in self.edges:
            print(f"{source} --({weight})--> {destination}")


graph = GraphUsingEdgeList()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)

graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 10)

graph.display()
