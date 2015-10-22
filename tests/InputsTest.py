import copy
import unittest
from constraint import RecursiveBacktrackingSolver, MinConflictsSolver, BacktrackingSolver

from src.RAWCS import RAWCS
from src.helpers.InputReader import InputReader
from src.helpers.Timer import Timer


class InputsTest(unittest.TestCase):

    inputs_folder = "..\src\inputs\\"

    def testInputsWithSingleAllocation(self):
        inputs = [
            {'input': 'le450_15c.col', 'k': 3},
            {'input': 'le450_15d.col', 'k': 3},
            {'input': 'le450_25c.col', 'k': 3},
            {'input': 'le450_25d.col', 'k': 3}
        ]
        # inputs = ['flat1000_76_0.col', 'flat300_28_0.col']
        iterations = 10
        for input in inputs:
            print input['input']
            print input['k']
            graph = InputReader.read(self.inputs_folder + input['input'])
            total_time = 0
            average_time = 0
            spills_amount = 0
            final_allocation = None
            vertex_amount = graph.nodes
            for i in range(1, iterations):
                print 'new test: ', graph.nodes
                with Timer(iterations=iterations) as timer:
                    allocator = RAWCS(input['k'], copy.deepcopy(graph))
                    allocation = allocator.getAllocation()
                total_time += timer.msecs
                if i == iterations - 1:
                    average_time = total_time / iterations
                    spills_amount = len(allocator.spilledOut)
                    final_allocation = allocation
            print '---'
            print 'input file: ', input['input']
            print 'k: ', input['k']
            print 'iterations amount: ', iterations
            print 'total spent time: ', total_time * 0.001, ' seconds'
            print 'average spent time: ', average_time * 0.001, ' seconds'
            print 'amount of vertexes: ', vertex_amount
            print 'amount of spills needed: ', spills_amount
            print 'suggested allocation: ', final_allocation

    # def testAllocationPerformance(self):
    #     inputs = [
    #         {'input': 'le450_15c.col', 'k': 15}
    #     ]
    #
    #     solvers = [RecursiveBacktrackingSolver, MinConflictsSolver, BacktrackingSolver]
    #     # inputs = ['flat1000_76_0.col', 'flat300_28_0.col']
    #     iterations = 10
    #     for input in inputs:
    #         graph = InputReader.read(self.inputs_folder + input['input'])
    #         total_time = 0
    #         average_time = 0
    #         spills_amount = 0
    #         vertex_amount = graph.nodes
    #         edges_amount = graph.edges
    #         for j in range(15, 16):
    #             print "j: ", j
    #             for solver in solvers:
    #                 print solver.__name__
    #                 for i in range(1, iterations):
    #                     print "i: ", i
    #                     local_graph = InputReader.read(self.inputs_folder + input['input'])
    #                     with Timer(iterations=iterations) as timer:
    #                         allocator = RAWCS(j, local_graph, solver = solver)
    #                         allocator.getAllocation()
    #                     total_time += timer.msecs
    #                     if i == iterations - 1:
    #                         average_time = total_time / iterations
    #                         spills_amount = len(allocator.spilledOut)
    #                 print '---'
    #                 print 'input file: ', input['input']
    #                 print 'k: ', j
    #                 print 'solver:', solver.__name__
    #                 print 'iterations amount: ', iterations
    #                 print 'total spent time: ', total_time * 0.001, ' seconds'
    #                 print 'average spent time: ', average_time * 0.001, ' seconds'
    #                 print 'amount of vertexes: ', vertex_amount
    #                 print 'amount of edges:', edges_amount
    #                 print 'amount of spills needed: ', spills_amount