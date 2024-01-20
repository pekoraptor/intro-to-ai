import numpy as np
from solver import Solver

class NaiveBayesClassificator(Solver):
    def __init__(self):
        # self.discrete_data_table = []
        self.positive_prob_table = []
        self.negative_prob_table = []
        self.positive_prob = 0
        self.negative_prob = 0

    def fit(self, X, y):
        self.positive_prob = y.count(1) / len(y)
        self.negative_prob = 1 - self.positive_prob

        for feature in X:
            pos, neg = self.calculate_feature_distribution(feature, y)
            self.positive_prob_table.append(pos)
            self.negative_prob_table.append(neg)

    def predict(self, X):
        pos_prob = 1
        neg_prob = 1
        for i, feature in enumerate(X):
            pos_prob *= self.calculate_feature_prob(i, feature, self.positive_prob_table)
            neg_prob *= self.calculate_feature_prob(i, feature, self.negative_prob_table)

        return 1 if pos_prob > neg_prob else 0

    def calculate_feature_distribution(self, feature, y):
        pos = []
        neg = []
        pos_vals = [value for value, flag in zip(feature, y) if flag == 1]
        pos.append(np.mean(pos_vals))
        pos.append(np.std(pos_vals))

        neg_vals = [value for value, flag in zip(feature, y) if flag == 0]
        neg.append(np.mean(neg_vals))
        neg.append(np.std(neg_vals))

        return pos, neg

    def calculate_feature_prob(self, i, feature, prob_table):
        avg = prob_table[i][0]
        std_dev = prob_table[i][1]
        return 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(- np.power((feature - avg), 2) / (2 * np.power(std_dev, 2)))
