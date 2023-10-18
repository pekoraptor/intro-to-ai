from abc import ABC, abstractmethod
import math
import numpy as np


class Solver(ABC):
    """A solver. It may be initialized with some hyperparameters."""

    @abstractmethod
    def get_parameters(self):
        """Returns a dictionary of hyperparameters"""
        ...

    @abstractmethod
    def solve(self, problem, x0, *args, **kwargs):
        """
        A method that solves the given problem for given initial solution.
        It may accept or require additional parameters.
        Returns the solution and may return additional info.
        """
        ...


def f(x: int):
    return (x ^ 4)/4


def g(x: np.array):
    a = -math.exp(-x[0] ^ 2 - x[1] ^ 2)
    b = -0.5*math.exp(-(x[0] - 1) ^ 2-(x[1] + 2) ^ 2)
    return 1.5 + a + b


class MySolver(Solver):
    def __init__(self, varCount, learningRate):
        self.varCount = varCount
        self.learningRate = learningRate

    def get_parameters(self):
        return (self.varCount, self.learningRate)
