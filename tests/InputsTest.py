import unittest

from src.RAWCS import RAWCS
from src.helpers.InputReader import InputReader
from src.helpers.Timer import Timer


class InputsTest(unittest.TestCase):

    inputs_folder = "..\src\inputs\\"

    def testAllocationPerformance(self):

        inputs = [
            {'input': 'le450_15c.col'},
            {'input': 'le450_15d.col'},
            {'input': 'le450_25c.col'},
            {'input': 'le450_25d.col'},
            {'input': 'flat1000_76_0.col'},
            {'input': 'flat300_28_0.col'}
        ]
        iterations = 1
        registersAmount = 5

        for input in inputs:
            graph = InputReader.read(self.inputs_folder + input['input'])
            total_time = 0
            average_time = 0
            spills_amount = 0
            vertex_amount = graph.nodes
            edges_amount = graph.edges
            with Timer(iterations=iterations) as timer:
                allocator = RAWCS(registersAmount, graph)
                allocator.getAllocation()
            total_time += timer.secs
            average_time = total_time / iterations
            spills_amount = len(allocator.spilledOut)
            print '---'
            print 'input file: ', input['input']
            print 'k: ', registersAmount
            print 'iterations amount: ', iterations
            print 'total spent time: ', total_time, ' seconds'
            print 'average spent time: ', average_time, ' seconds'
            print 'amount of vertexes: ', vertex_amount
            print 'amount of edges:', edges_amount
            print 'amount of spills needed: ', spills_amount
