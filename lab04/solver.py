from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

from node import Node
from utils import read_from_csv, format_data

class Solver(ABC):
    """A solver. Parameters may be passed during initialization."""

    @abstractmethod
    def get_parameters(self):
        """Returns a dictionary of hyperparameters"""
        ...

    @abstractmethod
    def fit(self, X, y):
        """
        A method that fits the solver to the given data.
        X is the dataset without the class attribute.
        y contains the class attribute for each sample from X.
        It may return anything.
        """
        ...

    def predict(self, X):
        """
        A method that returns predicted class for each row of X
        """


class MySolver(Solver):
    def __init__(self, max_depth=2) -> None:
        self.max_depth = max_depth

    def fit(self, X: list, y: list, current_depth=0):
        # X = [(data1, data2, data3, ...), (data1, data2, data3, ...), (data1, data2, data3, ...)]
        # y = [0, 1, 1]
        pair_count = len(y)
        feature_count = len(X[0])

        if current_depth <= self.max_depth:
            pass

    def _split(self, X: list, Y: list, feature_index: int, threshold: int):
        left_X = []
        left_Y = []
        right_X = []
        right_Y = []
        for x, y in zip(X, Y):
            if x[feature_index] < threshold:
                left_X.append(x)
                left_Y.append(y)
            else:
                right_X.append(x)
                right_Y.append(y)
        return left_X, left_Y, right_X, right_Y


if __name__ == "__main__":
    X, y = read_from_csv("lab04/cardio_train.csv", 0, 5)
    X = format_data(X, [0, 2, 3], [100, 5, 5])  # format age, height, weight

    pass
