import unittest

from src.RAWCS import RAWCS
from src.helpers.InputReader import InputReader
from src.helpers.Timer import Timer


class InputsTest(unittest.TestCase):
    inputs_folder = "..\src\inputs\\"

    def testQueenInputsWithSingleAllocation(self):
        inputs = ['queen10_10.col']
        iterations = 10
        registers = 3
        for input in inputs:
            graph = InputReader.read(self.inputs_folder + input)
            total_time = 0
            average_time = 0
            spills_amount = 0
            final_allocation = None
            for i in range(1, iterations):
                with Timer(iterations=iterations) as timer:
                    allocator = RAWCS(registers, graph)
                    allocation = allocator.allocation()
                total_time += timer.msecs
                if i == iterations - 1:
                    average_time = total_time / iterations
                    spills_amount = len(allocator.spilledOut)
                    final_allocation = allocation
            print '---'
            print 'input file: ', input
            print 'iterations amount: ', iterations
            print 'total spent time: ', total_time * 0.001, ' seconds'
            print 'average spent time: ', average_time * 0.001, ' seconds'
            print 'amount of spills needed: ', spills_amount
            print 'suggested allocation: ', final_allocation
