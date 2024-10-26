class Router:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0]*vertices for _ in range(vertices)]
    
    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src], visited = 0, [False] * self.V
        for _ in range(self.V):
            u = min((d, v) for v, d in enumerate(dist) if not visited[v])[1]
            visited[u] = True
            for v in range(self.V):
                if self.graph[u][v] and not visited[v] and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]
        return dist
    
    def bellman_ford(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u in range(self.V):
                for v in range(self.V):
                    if self.graph[u][v] and dist[u] + self.graph[u][v] < dist[v]:
                        dist[v] = dist[u] + self.graph[u][v]
        return dist

def main():
    router = Router(4)
    router.graph = [[0, 1, 4, 0], [1, 0, 2, 5], [4, 2, 0, 1], [0, 5, 1, 0]]
    src = 0  # Node A

    print("Dijkstra:", router.dijkstra(src))
    print("Bellman-Ford:", router.bellman_ford(src))

if __name__ == "__main__":
    main()
