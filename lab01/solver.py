from abc import ABC, abstractmethod
from functions import f, fGradient, g, gGradient
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


class MySolver(Solver):
    def __init__(self, learningRate):
        self.learningRate = learningRate
        self.previousResult = None
        self.valueArray = None

    def get_parameters(self):
        params = {
            "learningRate": self.learningRate,
            "previousResult": self.previousResult,
            "valueArray": self.valueArray
        }

        return params

    def solve(self, problem, problemGradient, x0, finalStep=1e-5, stepLimit=1e5):
        steps = 0
        previousX = x0
        previous = problem(previousX)

        x = np.array([0 for _ in range(previousX.size)], dtype=np.float64)
        self.valueArray = [previous]

        while True:
            steps += 1
            if steps > stepLimit:
                break

            for i in range(previousX.size):
                x[i] = previousX[i] - self.learningRate * \
                    problemGradient(previousX)[i]

            result = problem(x)
            self.valueArray.append(result)

            if abs(previous - result) < finalStep:
                break

            previousX = x
            previous = result

        self.previousResult = x
        return (x, steps)
