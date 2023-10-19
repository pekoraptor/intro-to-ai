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

    def get_parameters(self):
        return (self.learningRate)

    def solve(self, problem, problemGradient, x0, final_step=1e-5):
        steps = 0
        previousX = x0
        previous = problem(previousX)

        x = np.array([0 for _ in range(previousX.size)], dtype=np.float64)
        resultArray = [previous]

        while True:
            for i in range(previousX.size):
                x[i] = previousX[i] - self.learningRate * \
                    problemGradient(previousX)[i]

            result = problem(x)
            resultArray.append(result)

            if abs(previous - result) < final_step:
                break

            previousX = x
            previous = result
            steps += 1

        return (x, resultArray, steps)


if __name__ == "__main__":
    s = MySolver(0.01)
    # output = s.solve(f, fGradient, np.array([5], dtype=np.float64))
    x = np.array([0, 1], dtype=np.float64)
    output = s.solve(g, gGradient, x, final_step=1e-17)  # check for g

    print(output[1])
    print(output[0])
