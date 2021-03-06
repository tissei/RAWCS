# coding=utf-8
"""
RAWCS - github.com/tissei/RAWCS
~~~~~~~~~~~~~
WARNING! This is a prototype.
Copyright 2015 José Carlos S.A. Tissei and Lucas de Oliveira Teixeira
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

from constraint import *

class RAWCS:
    def __init__(self, registers, graph, solver=RecursiveBacktrackingSolver):
        """
        RAWCS class constructor

        :param registers: Amount of registers available for allocation
        :type registers: int
        :param graph: Interference graph of variables
        :type graph: Instance of ExtendedDiGraph
        """
        self.graph = graph
        self.registers = registers
        self.spilledOut = []
        self.solver = solver

    def _allocate(self, singleSolution=True):
        """
        Tries to allocate the interference graph variables into the available registers

        :return: List of the found allocation or the first valid allocation found,
                 returns None in case there's no possible allocation.
        :rtype: [{str: int}], {str: int} or None
        """
        solution = self._prepare().getSolution() if singleSolution else self._prepare().getSolutions()
        while solution == [] or solution == None:
            self._spill()
            solution = self._prepare().getSolution() if singleSolution else self._prepare().getSolutions()
        return solution

    def getAllocation(self):
        """
        Return the first valid allocation found

        :return: The first valid allocation found or None if there's no possible allocation
        :rtype : {str: int} or None
        """
        return self._allocate()

    def getAllocations(self):
        """
        Return the list with all the valid allocations found

        :return: List with allocations or None is case there's no possible allocation
        :rtype : [{str: int}] or None
        """
        return self._allocate(singleSolution=False)

    def _prepare(self):
        """
        Creates an python-constraint problem adding variables, domain and constraints

        :return: Instance of Problem
        :rtype: Problem
        """
        if any(self.graph.adjList):
            allocation = Problem(self.solver())
            registers_list = ['R' + str(n) for n in range(0, self.registers)]
            vars_list = [var for var in self.graph.adjList]
            allocation.addVariables(vars_list, registers_list)
            for var in vars_list:
                for adjacent in self.graph.adjList[var]:
                    allocation.addConstraint(AllDifferentConstraint(), [var, adjacent])
            return allocation
        return None

    def _spill(self, vertex = None):
        """
        Finds the vertex with the highest output degree
        and spill it out to the memory

        :param vertex: Vertex to be removed from the graph
        """
        if not vertex:
            vertex = self.graph.maxOutputDegree()
        self.spilledOut.append(vertex)
        self.graph.removeVertex(vertex)

    def _preSpill(self):
        """
        Executes an pre spill process searching for vertex which
        the output degree is to high to have an possible allocation
        then executes the spill process on then
        """
        outputDegrees = self.graph.allGraphOutputDegrees()
        for vertex in outputDegrees:
            if outputDegrees[vertex] > self.registers:
                self._spill(vertex)
