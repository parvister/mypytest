"""
Complex Math
"""

from math import pow
from packy.models.abstracts import Equation


class LinearEquation(Equation):

    def __init__(self, m, b, x=0):
        super(LinearEquation, self).__init__(x)
        self.m = m
        self.b = b

    def get_y(self, x):
        return (self.m * x) + self.b


class QuadraticEquation(Equation):

    def __init__(self, a, b, c, x=0):
        super(QuadraticEquation, self).__init__(x)
        self.a = a
        self.b = b
        self.c = c

    def get_y(self, x):
        return (self.a * pow(x, 2)) + (self.b * x) + self.c
