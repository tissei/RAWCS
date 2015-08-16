from src.RAWCS import RAWCS
from src.helpers.ExtendedDiGraph import ExtendedDiGraph

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

graph = ExtendedDiGraph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 0)
graph.addEdge(2, 1)
graph.addEdge(2, 3)
graph.addEdge(2, 0)
graph.addEdge(3, 1)
graph.addEdge(3, 2)
graph.addEdge(3, 4)
graph.addEdge(4, 3)
graph.addEdge(4, 5)
graph.addEdge(5, 4)
allocator = RAWCS(3, graph)
print allocator.allocate()