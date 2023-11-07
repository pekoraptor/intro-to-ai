from abc import ABC, abstractmethod
from costFunction import simulateLanding
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


def initPopulation(individualSize, popSize):
    population = []
    for _ in range(popSize):
        i = ""
        for __ in range(individualSize):
            i += str(random.randrange(2))

        population.append(i)

    return population


@dataclass
class MySolver(Solver):
    individualSize: int
    popSize: int
    mutationProb: float
    crossProb: float
    population = []
    maxIterations: int

    def grade(self, problem):
        costs = []
        for individual in self.population:
            costs.append(problem(individual))

        max_cost = costs[0]
        best_individual = self.population[0]
        for individual, cost in zip(self.population, costs):
            if cost > max_cost:
                max_cost = cost
                best_individual = individual
        return (costs, best_individual, max_cost)

    def selection(self, costs):
        minCost = min(costs)
        # rescale each cost so that none are negative
        for i, cost in enumerate(costs):
            costs[i] = cost + abs(minCost)

        minCost = min(costs)
        maxCost = max(costs)
        sumCosts = sum(costs)

        probs = []  # list with probabilities for each individual
        for cost in costs:
            probs.append(cost/sumCosts)

        ranges = []
        rangeSum = 0
        for prob in probs:
            prob = 0 if prob == 0 else round(1/prob)
            rangeSum += prob
            ranges.append(rangeSum)

        newPopulation = []
        for _ in range(self.popSize):
            chosen = random.randrange(ranges[-1])
            for index, r in enumerate(ranges):
                if chosen < r:
                    newPopulation.append(self.population[index])
                    break
        self.population = newPopulation

    def get_parameters(self):
        pass

    def solve(self, problem):
        i = 0
        self.population = initPopulation(self.individualSize, self.popSize)
        costs, best_individual, max_cost = self.grade(problem)
        while i < self.maxIterations:
            self.selection(costs)
            i += 1

    def mutation(self):
        pass

    def crossover(self):
        pass


# s = MySolver(200, 5, 0.1, 0.1, 10)
# s.solve(simulateLanding)
