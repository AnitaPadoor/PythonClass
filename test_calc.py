import unittest
import calc
class Testcalc(unittest.TestCase):
"""" testing of addition of 2 numbers """"
    def test_add(self):
	    result = calc.add(3,4)
	    self.assetEquals(result,7)