# coding=utf-8
"""
PyGraph - github.com/alleen94/EasyPyGraph
~~~~~~~~~~~~~
PyGraph is a python library that supports digraph and graph data structure.
WARNING! This is a prototype.
Copyright 2014 José Carlos S.A. Tissei and Lucas de Oliveira Teixeira
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
     http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
"""

#imports

import heapq


class DiGraph:
    def __init__(self):
        self.adjList = {}

    def __str__(self):
        return str( self.adjList )
    
    """
    Add an vertex to the adjList
    
    Verifies if the vertex does not exist adds it to the adjList
    
    @param vertex the vertex to be added
    @return void
    """
    
    def addVertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = {}

    """
    Add an edge between two vertexes
    
    If the edge does not exists adds it with given weight,
    If the edge already exists updates its weight
    
    @see addVertex method    
    @param vertex the starting vertex
    @param adjacent the ending vertex
    @param weight the edge weight
    @return void
    """
            
    def addEdge(self, vertex, adjacent, weight = 1):
        self.addVertex(vertex)
        self.addVertex(adjacent)
        self.adjList[vertex][adjacent] = weight
        
    """
    Remove a vertex and all his edges
    
    Removes the given vertex from the adjList and iterates trough all other
    vertexes in the adjList to remove any edges leading to it
    
    @param vertex the vertex to be removed
    @return void
    """

    def removeVertex(self, vertex):
        if vertex in self.adjList:
            del self.adjList[vertex]
            for adjacent in self.adjList:
                if vertex in self.adjList[adjacent]:
                    del self.adjList[adjacent][vertex]
    
    """
    Remove an edge between two vertexes
    
    Removes only the edge between the two vertexes
    
    @param vertex the starting vertex
    @param adjacent the ending vertex
    @return void
    """

    def removeEdge(self, vertex, adjacent):
        if vertex in self.adjList:
            if adjacent in self.adjList[vertex]:
                del self.adjList[vertex][adjacent]
                
    """            
    Verifies if a given vertex exists
    
    Verifies the presence of the vertex in the adjList
    
    @param vertex the vertex to be searched
    @return boolean
    """
                
    def hasVertex(self, vertex):
        return vertex in self.adjList

    """
    Verifies if an edge exists between two vertex
    
    Verifies if the vertex is in the adjList and if it's adjacent is in the 
    vertex adjList.
    
    @param vertex the starting vertex
    @param adjacent the adjacent vertex from the starting vertex
    @return boolean 
    """

    def hasEdge(self, vertex, adjacent):
        return vertex in self.adjList and adjacent in self.adjList[vertex]
    
    """
    Returns the output degree of a vertex
    
    Returns the length of the adjacent list of the given vertex
    
    @param vertex the vertex which the output degree will be calculated
    @return integer if the vertex exists 
    @return None if the vertex does not exists
    """

    def outputDegree(self, vertex):
        if vertex in self.adjList:
            return len(self.adjList[vertex])
        return None
    
    """
    Returns the input degree of a given vertex
    
    Iterate trough all vertexes in the adjList and verify if any of 
    them is adjacent to the given vertex.
    
    @param vertex the vertex which the input degree will be calculated
    @return integer if the vertex exists
    @return None if the vertex does not exists
    """
    
    def inputDegree(self, vertex):
        if vertex in self.adjList:
            degree = 0
            for adjacent in self.adjList:
                if vertex in self.adjList[adjacent]:
                    degree += 1
            return degree
        return None
    
    """
    Breadth-first search (BFS) is an algorithm for traversing or searching 
    graphs. Starts with a root node and explores all neighbors nodes before
    moving to another node. 
    
    The BFS begins at a root node and inspects all the neighbors nodes. 
    Then for each of those neighbor nodes in turn, it inspects their unvisited
    neighbors, and so on.
    
    @param start The starting vertex in the search
    @return List A List containing the search order of the vertexes
    """
    
    def breadthFirstSearch(self, start):
        visited = [start]
        queue = [start]
        while queue:
            t = queue.pop(0)
            if t == start and visited[0] != t: 
                return visited
            for adjacent in self.adjList[t]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    queue.append(adjacent)
        return visited
    
    """
    Depth-first search (DFS) is an algorithm for traversing or searching 
    graphs. Starts with a root node and explores as far as possible along 
    each branch before backtracking.
    The DFS begins at a root node and selects one the neighbors nodes and keep
    going through until there is a vertex with no neighbor that has not been visited,
    then backtracks to the closest parent node, and so on.
    
    @param start The starting vertex in the search
    @return List A List containing the search order of the vertexes
    """
    
    def depthFirstSearch(self, start):
        visited = []
        queue = [start]
        while queue:
            t = queue.pop()
            if t not in visited:
                visited.append(t)
                for adjacent in self.adjList[t]:
                    queue.append(adjacent)
        return visited

    """
    Verifies if a vertex can be reached from another vertex
    
    Uses DFS to verify if there's any way to reach the
    end vertex from the start vertex.
    
    @param vertex The starting vertex
    @param vertex The vertex to be reached
    @return boolean 
    """
    
    def areConected(self, start, end):
        return end in self.depthFirstSearch(start)
    
    """
    Verifies if a vertex can be reached back starting from its neighbors
    
    Uses DFS to verify if there is any way to reach back
    the vertex from any of its neighbors.
    
    @param vertex The starting vertex
    @return Boolean 
    """
    
    def hasCicle(self, vertex):
        for adjacent in self.adjList[vertex]:
            if vertex in self.depthFirstSearch(adjacent): return False
        return True
    
    """
    Verifies if there is no vertex that can be reached back starting from himself
    
    iterate trough adjList to test all vertexes and verifies if there is any way
    that they can be reached back starting from himselfs.
    
    @param vertex integer the starting vertex
    @return       boolean 
    """
    
    def isAcyclic(self):
        for vertex in self.adjList:
            for adjacent in self.adjList[vertex]:
                if vertex in self.adjList[adjacent]:
                    return False
        return True
    
    """
    Topological ordering of a graph is a linear ordering of its 
    vertices such that for every directed edge uv from vertex u to vertex v, 
    u comes before v in the ordering.
    
    search for all vertexes with input degree equal to 0 and put them in queue,
    iterate trough the queue breaking the conection between the vertexes and 
    its adjacents, if after this any adjacent has an input degree equal to 0
    the vertex is add to the queue, this method is repeated until the queue is
    empty.
    
    @return list list of ordered vertexes 
    """
    
    def topologicalSorting(self):
        adjListCopy = dict(self.adjList)
        outOnly = []
        count = 0
        for key in self.adjList:
            if self.inputDegree(key) == 0:
                outOnly.append(key)
        ordered = {}
        while len(outOnly) > 0:
            v = outOnly.pop(0)
            ordered[v] = count
            count += 1
            vList = adjListCopy[v].copy()
            for adjacent in vList:
                del adjListCopy[v][adjacent]
                if self.inputDegree(adjacent) == 0:
                       outOnly.append(adjacent)
        for key in adjListCopy:
            if len(adjListCopy[key]) > 0: return None
        else:
            return ordered
        
    """
    A bipartite graph is a graph whose vertices can be divided into two 
    disjoint sets U and V (that is, U and V are each independent sets) such 
    that every edge connects a vertex in U to one in V.
    
    The aproach choosen is the graph coloring were a graph is bipartite if it
    can be colored using only 2 colors.
    The algoritm iterates trough all vertexes and for each on of them test
    the attribution of two colors by checking if any of his adjacents is the
    same color, then iterates again trough all vertex checking if any of them
    are connected to the selected vertex has the same color, if none of those
    two conditions is true, then assing the color to the vertex and break the
    iteration.
    
    @return boolean
    """
        
    def isBipartite(self):
        colors = [0, 1]
        coloredGraph = {}
        for key in self.adjList: coloredGraph[key] = None
        for vertex in coloredGraph:
            if coloredGraph[vertex] == None:
                for color in colors:
                    checkAdj = True
                    for adjacent in self.adjList[vertex]:
                        if color == coloredGraph[adjacent]:
                            checkAdj = False
                            break
                    for isConected in self.adjList:
                        if vertex != isConected:
                            if vertex in self.adjList[isConected]:
                                if color == coloredGraph[isConected]:
                                    checkAdj = False
                                    break
                    if checkAdj:
                        coloredGraph[vertex] = color
                        break
        if None in coloredGraph: return False
        return True
        
    """
    Dijkstra's algorithm, is a graph search algorithm that solves the 
    single-source shortest path problem for a graph with non-negative edge 
    path costs, producing a shortest path tree.
    
    puts the initial vertex on ways, the weight 0 and the way transversed
    until now(only the initial vertex), initiate an iteration that continues
    to execute until ways is empty, when the iteration begins, remove the
    vertex with the lower value from ways and its weight,then assign to last
    the last visited vertex from the removed vertex from ways, then assign to
    dist the weight of the removed vertex from ways, then iterates trough the
    adjacents of last and if the distance of this adjacent has not yet been
    calculated add's him to the ways list and then repeats the process until
    the ways list in empty.
    @param  int  starting vertex
    @return list list with the shortest paths  and weights from the starting 
                 vertex to all vertexes.
    """
        
    def Dijkstra(self, v):
        dist = dict.fromkeys(self.adjList)
        ways = []
        heapq.heappush(ways, ( 0 , [v] ))
        while ways:
            ( weight , way ) = heapq.heappop(ways)
            last = way[ len(way) - 1 ]
            dist[last] = weight
            for neighbour in self.adjList[last]:
                if dist[neighbour] == None:
                    heapq.heappush(ways, ( weight + self.adjList[last][neighbour] , way + [neighbour] ) )
        return dist
    
        
    """
    The Bellman–Ford algorithm is an algorithm that computes shortest paths 
    from a single source vertex to all of the other vertices. It is slower 
    than Dijkstra's algorithm for the same problem, but more versatile, as 
    it is capable of handling graphs in which some of 
    the edge weights are negative numbers.
    
    puts the initial vertex on ways, the weight 0 and the way transversed
    until now(only the initil vertex), initiate an iteration that continues
    to execute until ways is empty, when the iteration begins, remove the
    vertex with the lower value from ways and its weight,then assign to last
    the last visited vertex from the removed vertex from ways, then assign to
    dist the weight of the removed vertex from ways, then iterates trough the
    adjacents of last and if the distance of this adjacent has not yet been
    calculated add's him to the ways list and then repeats the process until
    the ways list in empty.
    iterates trough all vertexes and it's adjcents and verify if there's any
    negative cicle.
    
    @param  int  starting vertex
    @return list list with the shortest paths  and weights from the starting 
                 vertex to all vertexes.
    """
            
    def BellmanFord(self, v):
        dist = dict.fromkeys(self.adjList)
        ways = []
        heapq.heappush(ways, ( 0 , [v] ))
        while ways:
            ( weight , way ) = heapq.heappop(ways)
            last = way[ len(way) - 1 ]
            dist[last] = weight
            for neighbour in self.adjList[last]:
                if dist[neighbour] == None:
                    heapq.heappush(ways, ( weight + self.adjList[last][neighbour] , way + [neighbour] ) )
        for vertex in self.adjList:
            for neighbour in self.adjList[vertex]:
                if dist[vertex] != None and dist[neighbour] != None:
                    if dist[vertex] > dist[neighbour] + self.adjList[vertex][neighbour]:
                        print 'negative cicle between ' + (str) (vertex) + ' and ' + (str) (neighbour) 
                        return None
        return dist

    """
    The Floyd–Warshall algorithm is a graph analysis algorithm for finding 
    shortest paths in a weighted graph with positive or negative edge weights 
    (but with no negative cycles). A single execution of the algorithm will 
    find the lengths (summed weights) of the shortest paths between all pairs 
    of vertices, though it does not return details of the paths themselves.
    
    Uses 3 iterations to make all possible comparisons between the vertexes
    and then compare 3 diferent combinations to get the weight, keep iterating
    until all the paths are found, the weights are put in a matrix and then
    the matrix is returned.
    
    @return [[]] matrix with the shortest paths from all vertexes to all vertexes.
    """
    
    def FloydWarshal(self):
        dist = self.adjList
        for k in dist:
            for i in dist:
                for j in dist:
                        if j not in dist[i]:
                            if k in dist[i] and j in dist[k]:
                                if i != j:
                                    dist[i][j] = dist[i][k] + dist[k][j]
                                else:
                                    dist[i][j] = 0
                        elif j in dist[i] and k in dist[i] and j in dist[k]:
                            if dist[i][j] > dist[i][k] + dist[k][j]:
                                dist[i][j] = dist[i][k] + dist[k][j] 
        return dist