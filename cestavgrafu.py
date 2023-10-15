class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

    def is_reachable(self, start, end, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        if start == end:
            return True

        if start not in self.graph:
            return False

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                if self.is_reachable(neighbor, end, visited):
                    return True

        return False

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 6)

start_node = 2
end_node = 6

if graph.is_reachable(start_node, end_node):
    print(f"Cesta mezi uzly {start_node} a {end_node} existuje.")
else:
    print(f"Cesta mezi uzly {start_node} a {end_node} neexistuje.")
