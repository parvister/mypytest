"""
Simple arithmetic functions
"""

class BasicMath:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        a * b


class BasicLinear:

    def __init__(self, m, b):
        self.m = m
        self.b = b

    @staticmethod
    def calc_y(self, x, m, b):
        return (m * x) + b

    def get_y(self, x):
        return (self.m * x) + self.b

