class Router:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        
    def link_state_routing(self, src):
        # Dijkstra's Algorithm
        dist = [float('inf')] * self.V
        dist[src] = 0
        done = [False] * self.V
        
        for _ in range(self.V):
            min_dist = float('inf')
            u = 0
            
            # Find closest unvisited node
            for v in range(self.V):
                if not done[v] and dist[v] < min_dist:
                    min_dist = dist[v]
                    u = v
            
            done[u] = True
            
            # Update distances
            for v in range(self.V):
                if not done[v] and self.graph[u][v] and \
                   dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]
        
        return dist

    def distance_vector_routing(self, src):
        # Bellman-Ford Algorithm
        dist = [float('inf')] * self.V
        dist[src] = 0
        
        # Relax edges |V|-1 times
        for _ in range(self.V - 1):
            for u in range(self.V):
                for v in range(self.V):
                    if self.graph[u][v] and \
                       dist[u] + self.graph[u][v] < dist[v]:
                        dist[v] = dist[u] + self.graph[u][v]
        
        return dist

def main():
    # Example network with 4 nodes
    router = Router(4)
    
    # Add links (0=A, 1=B, 2=C, 3=D)
    router.graph = [
        [0, 1, 4, 0],  # A's links
        [1, 0, 2, 5],  # B's links
        [4, 2, 0, 1],  # C's links
        [0, 5, 1, 0]   # D's links
    ]
    
    source = 0  # Start from node A
    
    # Find shortest paths using Link State
    ls_paths = router.link_state_routing(source)
    print("\nLink State Routing (Dijkstra):")
    for node, dist in enumerate(ls_paths):
        print(f"Node {chr(65+source)} → {chr(65+node)}: {dist}")
    
    # Find shortest paths using Distance Vector
    dv_paths = router.distance_vector_routing(source)
    print("\nDistance Vector Routing (Bellman-Ford):")
    for node, dist in enumerate(dv_paths):
        print(f"Node {chr(65+source)} → {chr(65+node)}: {dist}")

if __name__ == "__main__":
    main()