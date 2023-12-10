from abc import ABC, abstractmethod
import math
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
        self.root = None
        self.max_depth = max_depth

    def fit(self, X: list, y: list):
        self.root = self._build_tree(X, y)
    
    def _build_tree(self, X, y, current_depth=0):
        pair_count = len(y)
        feature_count = len(X[0])

        if current_depth <= self.max_depth:
            best_split = self._get_best_split(X, y, pair_count, feature_count)
            if best_split["inf_gain"] > 0:
                left_child = self.fit(best_split["left_X"], best_split["left_Y"], current_depth + 1)
                right_child = self.fit(best_split["right_X"], best_split["right_Y"], current_depth + 1)
                return Node(best_split["feature_index"], best_split["threshold"], left_child, right_child, best_split["inf_gain"])

        y_vals = list(set(y))
        chosen_y = y[0]
        chosen_y_count = y.count(chosen_y)
        for y_val in y_vals:
            count = y.count(y_val)
            if count > chosen_y_count:
                chosen_y = y_val
                chosen_y_count = count
        return Node(value=chosen_y)

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

    def _calculate_inf_gain(self, y, left_y, right_y):
        l_weight = len(left_y) / len(y)
        r_weight = len(right_y) / len(y)
        inf_gain = self._calculate_entropy(y) - l_weight * self._calculate_entropy(
            left_y) - r_weight * self._calculate_entropy(right_y)
        return inf_gain

    def _calculate_entropy(self, y):
        y_vals = list(set(y))
        entropy = 0
        for y_val in y_vals:
            p = y.count(y_val) / len(y)
            entropy += -p * math.log(p, 2)
        return entropy

    def _get_best_split(self, X, y, pair_count, feature_count):
        output = {}
        max_inf_gain = -float('inf')

        for feature_index in range(feature_count):
            # get unique values for this feature
            feature_vals = []
            for i in range(len(X)):
                if X[i][feature_index] not in feature_vals:
                    feature_vals.append(X[i][feature_index])

            # loop over all feature_vals to find the split with the most information gain
            for threshold in feature_vals:
                left_X, left_Y, right_X, right_Y = self._split(X, y, feature_index, threshold)
                if len(left_X) > 0 and len(right_X) > 0:
                    # calculate inf_gain
                    inf_gain = self._calculate_inf_gain(y, left_Y, right_Y)
                    if inf_gain > max_inf_gain:
                        # node = Node(feature_index, threshold, left_X, left_Y, right_X, right_Y, inf_gain)
                        output["feature_index"] = feature_index
                        output["threshold"] = threshold
                        output["left_X"] = left_X
                        output["left_Y"] = left_Y
                        output["right_X"] = right_X
                        output["right_Y"] = right_Y
                        output["inf_gain"] = inf_gain
                        max_inf_gain = inf_gain

        return output


if __name__ == "__main__":
    X, y = read_from_csv("lab04/cardio_train.csv", 0, 5)
    X = format_data(X, [0, 2, 3], [100, 5, 5])  # format age, height, weight
    pass
