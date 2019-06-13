import unittest
import calc
class Testcalc(unittest.TestCase):
    def test_add(self):
	    result = calc.add(3,4)
	    self.assetEquals(result,7)