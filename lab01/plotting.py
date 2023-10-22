from solver import MySolver
from functions import f, fGradient, g, gGradient
import numpy as np
import matplotlib.pyplot as plt


def initPlot(title='', yLabel='', xLabel=''):
    plt.title(title)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)


def plot(learningRate, problem, problemGradient, x0, steps=10, FinalStep=1e-5):
    s = MySolver(learningRate)
    s.solve(problem, problemGradient, x0, stepLimit=steps, finalStep=FinalStep)
    plt.plot(s.valueArray, label=str(learningRate))
