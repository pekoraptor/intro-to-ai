from matplotlib import pyplot as plt

from solver import MySolver
from utils import read_from_csv, format_data
from sklearn.model_selection import train_test_split


def compare_depths(depths: list):
    output = []
    X, y = read_from_csv("cardio_train.csv")
    X = format_data(X, [0, 2, 3], [100, 5, 5])  # format age, height, weight
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    for d in depths:
        solver = MySolver(d)
        solver.fit(X_train, y_train)
        y_pred = solver.predict(X_test)
        correct = 0
        for predicted_y, actual_y in zip(y_pred, y_test):
            if predicted_y == actual_y:
                correct += 1
        output.append(correct/len(y_test))

    plt.plot(depths, output)
    plt.show()