"""
    This is a basic source file for a python function testing based on Unittest framework.
    The file run various test on a file called calculator where the tested functions are stored.
"""

# Import Libraries:
#import sys
# Add 
#sys.path.append('.')
#sys.path.append('core_package/')
#sys.path.insert(0, '/home/amninder/Desktop/Folder_2')

import unittest
# Import file source file for test:

import Calculator as calculator



# TestCase Class for unittest testing
class TestCalc(unittest.TestCase):

    # Test addition
    def test_add(self):
        self.assertEqual(calculator.add(1, 1), 2)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(1.1, 3.3), 4.4)

    # Test subtraction (last test case fails)
    def test_sub(self):
        self.assertEqual(calculator.sub(1, 1), 0)
        self.assertEqual(calculator.sub(-1, 1), -2)
        self.assertEqual(calculator.sub(1.1, -3.3), 4.4)

    # Test multiplication (first case fails)
    def test_mult(self):
        self.assertEqual(calculator.mult(1, 1), 1)
        self.assertEqual(calculator.mult(0, 1), 0)
        self.assertEqual(calculator.mult(1.5, 2), 3)

    # Test division (third case fails)
    def test_div(self):
        self.assertEqual(calculator.div(1, 1), 1)
        self.assertEqual(calculator.div(0, 1), 0)
        # self.assertEqual(calculator.div(1, 0), 0)
        # self.assertEqual(calculator.div(1.0, 0.0), float("nan"))


if __name__ == "__main__":
    unittest.main()
