from EasyPyGraph.EasyPyGraph import DiGraph
from constraint import *


class RAWCS:

    def __init__(self):
        #	 	 ( 0 )
        #		 /   \
        #		/	  \
        #  ( 1 ) ----- ( 2 )
        #		\	  /
        #		 \   /
        # 		 ( 3 )
        #		/
        #	   /
        #  ( 4 ) ----- ( 5 )
        self.graph = DiGraph()
        self.graph.addEdge(0, 1)
        self.graph.addEdge(0, 2)
        self.graph.addEdge(1, 2)
        self.graph.addEdge(1, 3)
        self.graph.addEdge(1, 0)
        self.graph.addEdge(2, 1)
        self.graph.addEdge(2, 3)
        self.graph.addEdge(2, 0)
        self.graph.addEdge(3, 1)
        self.graph.addEdge(3, 2)
        self.graph.addEdge(3, 4)
        self.graph.addEdge(4, 3)
        self.graph.addEdge(4, 5)
        self.graph.addEdge(5, 4)

    def allocate(self, n):
        allocation = Problem()


