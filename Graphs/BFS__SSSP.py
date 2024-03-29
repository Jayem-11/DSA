class Graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


    def bfs(self, start, end):
        queue = []
        queue.append(start)
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjascent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjascent)
                queue.append(new_path)

customDict = {
    "a": ["b" , "c"],
    "b": ["d" , "g"],
    "c": ["d" , "f"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"],
}

graph = Graph(customDict)
print(graph.bfs("a", "g"))