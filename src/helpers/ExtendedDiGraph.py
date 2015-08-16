from EasyPyGraph.EasyPyGraph import DiGraph


class ExtendedDiGraph(DiGraph):
    def maxOutputDegree(self):
        return max({vertex: self.outputDegree(vertex) for vertex in self.adjList})
