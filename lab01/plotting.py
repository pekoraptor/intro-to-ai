from solver import MySolver
from functions import f, fGradient, g, gGradient
import numpy as np
import matplotlib.pyplot as plt


def initPlot(title='', yLabel='', xLabel=''):
    plt.title(title)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)


def plot(learningRate, problem, problemGradient, x0, steps=10):
    s = MySolver(learningRate)
    s.solve(problem, problemGradient, x0, stepLimit=steps)
    plt.plot(s.valueArray, label=str(learningRate))


initPlot('Different learning rates', 'function values', 'iterations')
for rate in [0.01, 0.001, 0.0001]:
    plot(rate, f, fGradient, np.array([5]))

plt.legend(loc='right')
plt.show()
