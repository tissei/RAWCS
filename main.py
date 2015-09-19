import copy

from src.ExtendedDiGraph import ExtendedDiGraph
from src.RAWCS import RAWCS
from src.helpers.Timer import Timer


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

# [{0: '0', 1: '2', 2: '1', 3: '0', 4: '2', 5: '1'}

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

# graph = InputReader.read('src\inputs\queen10_10.col')

with Timer(iterations=10, verbose=True) as timer:
    for i in range(1, 10):
        RAWCS(2, copy.deepcopy(graph)).allocation()

allocator = RAWCS(2, graph)
print allocator.allocation()
print allocator.spilledOut
