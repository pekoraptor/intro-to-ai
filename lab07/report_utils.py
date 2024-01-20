from naive_bayes import NaiveBayesClassificator
from utils import read_from_csv
import numpy as np
from sklearn.model_selection import train_test_split


def k_cross_validation(X, y, k=5):
    split_indices = np.arange(0, len(X), len(X) // k)
    X_sets = np.split(X, split_indices[1:-1])
    y_sets = np.split(y, split_indices[1:-1])

    accuracies = []

    for i in range(k):
        X_test = X_sets[i]
        y_test = y_sets[i]

        X_train = X_sets[0] if i != 0 else X_sets[1]
        y_train = y_sets[0] if i != 0 else y_sets[1]
        for j in range(0, k):
            if j != i:
                X_train = np.concatenate((X_train, X_sets[j])).tolist()
                y_train = np.concatenate((y_train, y_sets[j])).tolist()

        model = NaiveBayesClassificator()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracies.append(sum(real_y == pred_y for real_y, pred_y in zip(y_test, y_pred)) / len(y_test))

    return np.mean(accuracies)


if __name__ == '__main__':
    X, y = read_from_csv('cardio_train.csv')
    print(k_cross_validation(X, y, 5))