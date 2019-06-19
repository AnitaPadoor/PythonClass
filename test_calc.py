"""Test_calc"""
import unittest
import calc
class Testcalc(unittest.TestCase):
    """ testing of addition of 2 numbers
    """
    def test_add(self):
        """Method docstring
        """
        result = calc.add(3, 4)
        self.assertEqual(result, 7)
		