import unittest

from tests.InputsTest import InputsTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(InputsTest("testAllocationPerformance"))
    return suite


unittest.TextTestRunner().run(suite())
