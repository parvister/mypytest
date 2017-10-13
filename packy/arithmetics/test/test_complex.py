"""
Unit tests for the complex arithmetic equations
"""

import unittest

from packy.arithmetics.complex import LinearEquation, QuadraticEquation


class ComplexTest(unittest.TestCase):

    def test_linear_equation(self):
        eq = LinearEquation(2, 1)
        self.assertEqual(eq.get_y(2), 5, "linear equation get_y() not working")
        self.assertEqual(eq.next_y(), 3, "linear equation next_y() not working")
        self.assertEqual(eq.next_y(), 5, "linear equation next_y() not working")

    def test_quadratic_equation(self):
        eq = QuadraticEquation(1, 2, 1)
        self.assertEqual(eq.get_y(2), 9, "quadratic equation get_y() not working")
        self.assertEqual(eq.next_y(), 4, "quadratic equation next_y() not working")
        self.assertEqual(eq.next_y(), 9, "quadratic equation next_y() not working")


if __name__ == '__main__':
    unittest.main()

