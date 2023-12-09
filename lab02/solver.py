from abc import ABC, abstractmethod
from costFunction import simulateLanding
from dataclasses import dataclass, field
import random
import numpy as np


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
    maxIterations: int
    population: list[int] = field(default_factory=list)

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

    def selection(self, costs, minCost):
        # rescale each cost so that none are negative
        for i, cost in enumerate(costs):
            costs[i] = cost + abs(minCost)

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
        for _ in range(self.popSize - 1):
            chosen = random.randrange(ranges[-1])
            for index, r in enumerate(ranges):
                if chosen < r:
                    newPopulation.append(self.population[index])
                    break
        return newPopulation

    def get_parameters(self):
        return {
            "individualSize": self.individualSize,
            "popSize": self.popSize,
            "mutationProb": self.mutationProb,
            "crossProb": self.crossProb,
            "maxIterations": self.maxIterations
        }

    def solve(self, problem, pop0=None, minCost=0):
        i = 0
        bestEachGen = []
        meanEachGen = []
        self.population = initPopulation(
            self.individualSize, self.popSize) if pop0 == None else pop0
        costs, bestIndividual, maxCost = self.grade(problem)
        currentBest = bestIndividual
        bestEachGen.append(maxCost)
        meanEachGen.append(np.mean(costs))
        while i < self.maxIterations:
            newPopulation = self.selection(costs, minCost)
            newPopulation.append(currentBest)
            self.population = newPopulation
            self.crossover()
            self.mutation()
            costs, currentBest, currentMax = self.grade(problem)
            bestEachGen.append(currentMax)
            meanEachGen.append(np.mean(costs))
            if currentMax > maxCost:
                bestIndividual = currentBest
                maxCost = currentMax

            i += 1

        return bestIndividual, maxCost, bestEachGen, meanEachGen

    def crossover(self):
        for i in range(self.popSize // 2):
            if random.randrange(round(1/self.crossProb)) == 0:
                crossPoint = random.randrange(self.individualSize - 1)
                newA = self.population[i][:crossPoint] + \
                    self.population[i + 1][crossPoint:]
                newB = self.population[i + 1][:crossPoint] + \
                    self.population[i][crossPoint:]
                self.population[i] = newA
                self.population[i + 1] = newB

    def mutation(self):
        for i in range(self.popSize):
            for j in range(self.individualSize):
                if random.randrange(round(1/self.mutationProb)) == 0:
                    newBit = '1' if self.population[i][j] == '0' else '0'
                    newIndividual = self.population[i][:j] + \
                        newBit + self.population[i][j+1:]
                    self.population[i] = newIndividual
