"""
All abstract classes
"""

from abc import ABCMeta, abstractmethod


class Equation:

    __metaclass__ = ABCMeta

    def __init__(self, x=0):
        self.x = x

    def next_y(self):
        self.x += 1
        return self.get_y(self.x)

    @abstractmethod
    def get_y(self, x):
        raise NotImplementedError("Abstract method of %s" % type(self).__name__)
