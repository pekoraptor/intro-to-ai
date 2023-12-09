from solver import MySolver, simulateLanding
from matplotlib import pyplot as plt


def plotMutationBest(indSize, popSize, maxIter, mutationsProbs, crossProb, colors):
    values = []
    for prob in mutationsProbs:
        s = MySolver(indSize, popSize, prob, crossProb, maxIter)
        values.append(s.solve(simulateLanding, None, -1200)[2])

    # whole plot
    plt.title('Whole plot')
    plt.xlabel('Generation')
    plt.ylabel('Best cost found')
    for v, c, m in zip(values, colors, mutationsProbs):
        plt.plot(v, c + 'o', markersize=2, label=f'MutationProb = {m}')
        plt.plot(v, c, linewidth=0.1)
    plt.legend()
    plt.show()

    # top part of the plot
    plt.title('Top part of the plot')
    plt.xlabel('Generation')
    plt.ylabel('Best cost found')
    plt.ylim(1870, 1920)
    for v, c, m in zip(values, colors, mutationsProbs):
        plt.plot(v, c + 'o', markersize=2, label=f'MutationProb = {m}')
        plt.plot(v, c, linewidth=0.1)
    plt.legend()
    plt.show()

    # bottom part of the plot
    plt.title('Bottom part of the plot')
    plt.xlabel('Generation')
    plt.ylabel('Best cost found')
    plt.ylim(-1125, -1075)
    for v, c, m in zip(values, colors, mutationsProbs):
        plt.plot(v, c + 'o', markersize=2, label=f'MutationProb = {m}')
        plt.plot(v, c, linewidth=0.1)
    plt.legend()
    plt.show()


def plotMutationMean(indSize, popSize, maxIter, mutationsProbs, crossProb, colors):
    values = []
    for prob in mutationsProbs:
        s = MySolver(indSize, popSize, prob, crossProb, maxIter)
        values.append(s.solve(simulateLanding, None, -1200)[3])

    plt.title('Mean cost per generation')
    plt.xlabel('Generation')
    plt.ylabel('Mean cost found')
    for v, c, m in zip(values, colors, mutationsProbs):
        plt.plot(v, c + 'o', markersize=2, label=f'MutationProb = {m}')
        plt.plot(v, c, linewidth=0.1)
    plt.legend()
    plt.show()
