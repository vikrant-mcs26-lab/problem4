import pathlib as pth

class Data:
    def __init__(
        self, graph_path: pth.Path, 
        approx_path: pth.Path, 
        vertex_cover_path: pth.Path, 
    ):
        with open(graph_path) as file:
            init_data = file.readline().split(" ")
            
            num_nodes = int(init_data[0])

            self.nodes: set[int] = set(range(num_nodes))
            self.edges: set[tuple[int,int]] = set()

            for line in file.readlines():
                edge = line.split(",")
                u, v = int(edge[0]), int(edge[1])
    
                if (u,v) in self.edges or (v,u) in self.edges:
                    continue
                self.edges.add((u,v))
        
        with open(approx_path) as file:
            init_data = file.readline().split(" ")
            
            self.runtime_matching = int(init_data[2])

            self.matching_edges: set[tuple[int,int]] = set()
            self.matching_vertices: set[int] = set()

            for line in file.readlines():
                edge = line.split(" ")
                u, v = int(edge[0]), int(edge[1])
    
                if (u,v) in self.matching_edges or (v,u) in self.matching_edges:
                    continue
                self.matching_edges.add((u,v))
                self.matching_vertices.update([u, v])
        
        with open(vertex_cover_path) as file:
            init_data = file.readline().split(" ")
            self.runtime_brute_force = int(init_data[0])
            self.vertex_cover: set[int] = {int(x) for x in file.readline().strip().split(" ")}

        self.num_nodes = len(self.nodes)
        self.num_edges = len(self.edges)
        self.size_vertex_cover = len(self.vertex_cover)
        self.size_maximal_matching = len(self.matching_edges)
        self.size_approx_vertex_cover = len(self.matching_vertices)
