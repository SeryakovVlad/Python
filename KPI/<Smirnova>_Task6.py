#'Introduction to programming':Task 6
#Smirnova Natalia, FB-24, V-1

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def _dfs(self, start, visited):
        visited[start] = True
        for i in self.graph[start]:
            if not visited[i]:
                self._dfs(i, visited)

    def is_linked(self):
        visited = [False] * self.V
        self._dfs(0, visited)
        return all(visited)

g1 = Graph(5)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 4)
print(g1.is_linked()) # True

g2 = Graph(5)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(3, 4)
print(g2.is_linked()) # False