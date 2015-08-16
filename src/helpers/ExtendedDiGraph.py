from libs.EasyPyGraph.EasyPyGraph import DiGraph


class ExtendedDiGraph(DiGraph):

    def maxOutputDegree(self):
        """
        Finds the vertex with the highest output degree

        :return: Vertex with the highest output degree
        :rtype: int
        """
        return max({vertex: self.outputDegree(vertex) for vertex in self.adjList})
