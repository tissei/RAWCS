from src.RAWCS import RAWCS
from src.helpers.ExtendedDiGraph import ExtendedDiGraph
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

with Timer(iterations=50000, verbose=True) as timer:
    for i in range(1, 50000):
        RAWCS(3, graph).allocate()

print RAWCS(3, graph).allocate()
