class GraphUsingAdjancenyList:
    def __init__(self,vertices,edges):
        self.V=[]
        self.adj_list={}

    def add_vertex(self,vertex):
        if vertex not in self.V:
            self.V.append(vertex)
            self.adj_list[vertex] = []
        else:
            print(f"Vertex is already present: {vertex}")

    def add_edge(self,source,destination,weight=1):
        if source in self.V and destination in self.V:
            self.adj_list[source].append((destination, weight))
            self.adj_list[destination].append((source, weight))
        else:
            print("One or both vertices are not present in the graph")

    def display(self):
        for vertex in self.V:
            print(f"Vertex: {vertex}")
        for vertex,neighbors in self.adj_list.items():
            print(f"{vertex}:{neighbors}") 

graph = GraphUsingAdjancenyList([], [])
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3) 
graph.add_edge(1, 2, 5)     
graph.add_edge(2, 3, 10)    
graph.display() 

        
