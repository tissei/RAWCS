import unittest

from tests.InputsTest import InputsTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(InputsTest("testQueenInputsWithSingleAllocation"))
    return suite


unittest.TextTestRunner().run(suite())
