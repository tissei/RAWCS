from constraint import *

from src.helpers.ExtendedDiGraph import ExtendedDiGraph


class RAWCS:
    def __init__(self, registers):
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
        self.graph = ExtendedDiGraph()
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
        self.registers = registers
        self.spilledOut = []

    def allocate(self):
        solution = self.prepare().getSolutions()
        while solution == []:
            print solution
            print self.graph
            self.spill()
            solution = self.prepare().getSolutions()
        return solution

    def prepare(self):
        allocation = Problem()
        registers_list = [str(n) for n in range(0, self.registers)]
        print 'registers_list: ', registers_list
        vars_list = [var for var in self.graph.adjList]
        print 'vars_list: ', vars_list
        allocation.addVariables(registers_list, vars_list)
        allocation.addConstraint(AllDifferentConstraint())
        allocation.addConstraint(self.liveRangeConstraint, registers_list)
        return allocation

    def liveRangeConstraint(self, *domain):
        print 'domain', domain
        for vertex in domain:
            adjacent_list = [adjacent for adjacent in self.graph.adjList[vertex]]
            verify_allocation = [adjacent in domain for adjacent in adjacent_list]
            not_allocated = [allocated for allocated in verify_allocation if not allocated]
            if not_allocated:
                return False
        return True

    def spill(self):
        most_dependent = self.graph.maxOutputDegree()
        self.spilledOut.append(most_dependent)
        self.graph.removeVertex(most_dependent)
