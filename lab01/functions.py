import math
import numpy as np


def f(x):
    return math.pow(x, 4) / 4


def fGradient(x):
    return np.array([math.pow(x, 3)], dtype=np.float64)


def g(x: np.array):
    x1 = x[0]
    x2 = x[1]

    a = -1 * math.exp(-1 * math.pow(x1, 2) - 1 * math.pow(x2, 2))
    b = -0.5 * \
        math.exp(-1 * math.pow((x1 - 1), 2) - 1 * math.pow((x2 + 2), 2))
    return 1.5 + a + b


def gGradient(x: np.array):
    x1 = x[0]
    x2 = x[1]
    a = 2 * x1 * math.exp(-1 * math.pow(x1, 2) - 1 * math.pow(x2, 2)) + (x1 - 1) * \
        math.exp(- 1 * math.pow((x1 - 1), 2) - 1 * math.pow((x2 + 2), 2))

    b = 2 * x2 * math.exp(-1 * math.pow(x1, 2) - 1 * math.pow(x2, 2)) + (x2 + 2) * \
        math.exp(- 1 * math.pow((x1 - 1), 2) - 1 * math.pow((x2 + 2), 2))

    return np.array([a, b], dtype=np.float64)
