class GraphMatrix:
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self.vertices=[None]*num_vertices
        self.adj_matrix=[[0]*num_vertices for row  in range(num_vertices)]

    def add_vertex(self,index,label):
        if index >=0 and index < self.num_vertices:
            if self.vertices[index] is None:
                self.vertices[index] = label
            else:
                print(f"Vertex {index} is already present.")

    def add_edge(self,source,destination,weight=1):
        if 0 <= source < self.num_vertices and 0<=destination <self.num_vertices:
            self.adj_matrix[source][destination] = weight
            self.adj_matrix[destination][source] = weight

    def display(self):
        print("Vertices:")
        for index, label in enumerate(self.vertices):
            if label is not None:
                print(f"  {index}: {label}")

        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print("  ", row)

graph= GraphMatrix(5)   
graph.add_vertex(0, "A")
graph.add_vertex(1, "B")
graph.add_vertex(2, "C")
graph.add_vertex(3, "D")
graph.add_vertex(4, "E")
graph.add_edge(0, 1, 5)
graph.add_edge(1, 2, 10)
graph.add_edge(2, 3, 15)
graph.add_edge(3, 4, 20)
graph.display() 
