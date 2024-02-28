from naive_bayes import NaiveBayesClassificator
from utils import read_from_csv
import numpy as np
import matplotlib.pyplot as plt
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


def plot_k_cross_val(X, y, k_table=[2, 3, 4, 5]):
    x = [str(k) for k in k_table]
    accuracies = []
    for k in k_table:
        accuracies.append(k_cross_validation(X, y, k))
    
    plt.bar(x, accuracies, capsize=5, color='slategray')
    plt.title("Different k cross validation runs")
    plt.ylabel("Accuracy")
    plt.xlabel("k")

    for i, acc in enumerate(accuracies):
        plt.text(i, 0.1, f'{100*acc:.2f}%', ha="center", va='bottom', color='black')

    plt.show()


def plot_train_test(X, y, iterations=10, train_sizes=[0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]):
    x = [str(k) for k in train_sizes]
    accuracies = []
    for ts in train_sizes:
        acc = []
        for i in range(iterations):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(1-ts))
            classificator = NaiveBayesClassificator()
            classificator.fit(X_train, y_train)
            y_pred = classificator.predict(X_test)
            acc.append(sum(real_y == pred_y for real_y, pred_y in zip(y_test, y_pred)) / len(y_test))

        accuracies.append(acc)

    plot_y = [np.mean(acc) for acc in accuracies]
    y_err = [np.std(acc) for acc in accuracies]
    
    plt.bar(x, plot_y, yerr=y_err, capsize=5, color='slategray')
    plt.title("Different train size runs")
    plt.ylabel("Mean Accuracy")
    plt.xlabel("train size")

    for i, acc in enumerate(plot_y):
        plt.text(i, 0.1, f'{100*acc:.2f}%', ha="center", va='bottom', color='black')

    plt.show()


# if __name__ == '__main__':
#     X, y = read_from_csv('cardio_train.csv')
#     print(k_cross_validation(X, y, 5))

