#'Introduction to programming':Task 6
#Seryakov Vlad, FB-21, V-2(22)

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def topological_sorting(self, start, end, visited, path, paths):
        visited[start] = True
        path.append(start)

        if start == end:
            paths.append(list(path))
        else:
            for i in self.graph[start]:
                if not visited[i]:
                    self.topological_sorting(i, end, visited, path, paths)

        visited[start] = False
        path.pop()

    def count_path(self, start, end):
        visited = defaultdict(bool)
        paths = []
        self.topological_sorting(start, end, visited, [], paths)
        return len(paths)


g1 = Graph(5)
g1.add_edge(0, 1)
g1.add_edge(0, 3)
g1.add_edge(0, 2)
g1.add_edge(0, 4)
g1.add_edge(2, 3)
g1.add_edge(3, 4)

print(g1.count_path(0, 4))
print(g1.count_path(0, 1))