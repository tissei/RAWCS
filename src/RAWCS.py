# coding=utf-8
"""
RAWCS - github.com/alleen94/RAWCS
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
    def __init__(self, registers, graph):
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

    def allocate(self):
        """
        Tries to allocate the interference graph variables into the available registers

        :return: List with allocations or None is case there's no possible allocation
        :rtype: [{str: int}] or None
        """
        solution = self.prepare().getSolutions()
        while solution == []:
            print solution
            print self.graph
            self.spill()
            solution = self.prepare().getSolutions()
        return solution

    def prepare(self):
        """
        Creates an python-constraint problem adding variables, domain and constraints

        :return: Instance of Problem
        :rtype: Problem
        """
        if any(self.graph.adjList):
            allocation = Problem()
            registers_list = [str(n) for n in range(0, self.registers)]
            print 'registers_list: ', registers_list
            vars_list = [var for var in self.graph.adjList]
            print 'vars_list: ', vars_list
            allocation.addVariables(registers_list, vars_list)
            allocation.addConstraint(AllDifferentConstraint())
            allocation.addConstraint(self.liveRangeConstraint, registers_list)
            return allocation
        return None

    def liveRangeConstraint(self, *domain):
        """
        Constraint of the live range problem

        :param domain: Set of domain values to verify
        :type domain: ()
        :return: Boolean representing that the given domain satisfies the live range constraint
        :rtype: bool
        """
        print 'domain', domain
        for vertex in domain:
            adjacent_list = [adjacent for adjacent in self.graph.adjList[vertex]]
            verify_allocation = [adjacent in domain for adjacent in adjacent_list]
            not_allocated = [allocated for allocated in verify_allocation if not allocated]
            if not_allocated:
                return False
        return True

    def spill(self):
        """
        Spill the variable out to be stored on memory
        """
        most_dependent = self.graph.maxOutputDegree()
        self.spilledOut.append(most_dependent)
        self.graph.removeVertex(most_dependent)
