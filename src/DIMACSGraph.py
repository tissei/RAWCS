from src.ExtendedDiGraph import ExtendedDiGraph

class DIMACSGraph(ExtendedDiGraph):

    def __init__(self, nodes, edges, edgesList):
        """
        This class is an adapter that lets you use
        the EasyPyGraph class to instantiate an DIMACS
        Graph by using the InputReader helper.

        :param nodes: amount of nodes in the graph
        :param edges: amount of edges in the graph
        :param edgesList: list of edges in the graph
        :return: new DIMACSGraph instance
        """
        super(DIMACSGraph, self).__init__()
        self.nodes = nodes
        self.edges = edges
        [self.addEdge(edge.vertex, edge.adjacent) for edge in edgesList]
