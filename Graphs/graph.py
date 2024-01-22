class Graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjascentVertex in self.gdict[deVertex]:
                if adjascentVertex not in visited:
                    visited.append(adjascentVertex)
                    queue.append(adjascentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            deVertex = stack.pop()
            print(deVertex)
            for adjascentVertex in self.gdict[deVertex]:
                if adjascentVertex not in visited:
                    visited.append(adjascentVertex)
                    stack.append(adjascentVertex)

customDict = {
    "a": ["b" , "c"],
    "b": ["a" , "d", "e"],
    "c": ["a" , "e"],
    "d": ["b" , "e", "f"],
    "e": ["d" , "f"],
    "f": ["d" , "e"],
}

graph = Graph(customDict)
graph.dfs("a")