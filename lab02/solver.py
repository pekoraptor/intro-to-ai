from abc import ABC, abstractmethod
from dataclasses import dataclass
import random


class Solver(ABC):
    """A solver. It may be initialized with some hyperparameters."""

    @abstractmethod
    def get_parameters(self):
        """Returns a dictionary of hyperparameters"""
        ...

    @abstractmethod
    def solve(self, problem, pop0, *args, **kwargs):
        """
        A method that solves the given problem for given initial solutions.
        It may accept or require additional parameters.
        Returns the solution and may return additional info.
        """
        ...


@dataclass
class MySolver(Solver):
    popSize: int
    mutationProb: float
    crossProb: float
    population = []

    def initPopulation(self):
        for _ in range(self.popSize):
            i = ""
            for __ in range(200):
                i += str(random.randrange(2))

            self.population.append(i)

    def get_parameters(self):
        pass

    def solve(self, problem, pop0, *args, **kwargs):
        pass

    def mutation(self):
        pass

    def crossover(self):
        pass

    def cost(individual: str):
        gravityAcc = 0.09
        fuel = individual.count('1')
        weight = 200 + fuel
        altitude = 200
        velocity = 0
        acceleration = 0
        for event in individual:
            if event == '1':
                weight -= 1
                acceleration = 40/weight - gravityAcc
            else:
                acceleration = -gravityAcc

            velocity += acceleration
            altitude += velocity

            if altitude < 2:
                if abs(velocity) < 2:
                    return 2000 - fuel
                else:
                    return -1000 - fuel
