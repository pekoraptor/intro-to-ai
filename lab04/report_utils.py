from matplotlib import pyplot as plt
from solver import MySolver
from utils import read_from_csv, format_data
from sklearn.model_selection import train_test_split


def compare_depths(depths: list, test_sizes):
    for i, test_size in enumerate(test_sizes):
        output = []
        X, y = read_from_csv("cardio_train.csv")
        # format age, height, weight
        X = format_data(X, [0, 2, 3], [100, 5, 5])
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42)
        for d in depths:
            solver = MySolver(d)
            solver.fit(X_train, y_train)
            y_pred = solver.predict(X_test)
            correct = 0
            for predicted_y, actual_y in zip(y_pred, y_test):
                if predicted_y == actual_y:
                    correct += 1
            output.append(correct * 100/len(y_test))

        plt.title("Comparison of different tree heights")
        plt.xlabel("Height of the tree")
        plt.ylabel("Success rate [%]")
        plt.xticks(depths)
        plt.plot(depths, output, label=f"Test size: {test_size}")

    plt.legend()
    plt.show()


def plot_train_test():
    X, y = read_from_csv("cardio_train.csv")
    X = format_data(X, [0, 2, 3], [100, 5, 5])
    train_output = []
    test_output = []
    for d in list(range(21)):
        solver = MySolver(max_depth=d)
        solver.fit(X[:50000], y[:50000])
        correct = 0
        pred_y = solver.predict(X[:1000])
        for predicted_y, actual_y in zip(pred_y, y[:1000]):
            if predicted_y == actual_y:
                correct += 1
        train_output.append(correct * 100/1000)

        correct = 0
        pred_y = solver.predict(X[50000:51000])
        for predicted_y, actual_y in zip(pred_y, y[50000:51000]):
            if predicted_y == actual_y:
                correct += 1
        test_output.append(correct * 100/1000)

    plt.title("Prediction on train data vs new data")
    plt.xlabel("Tree Height")
    plt.ylabel("Success rate [%]")
    plt.plot(list(range(21)), train_output, label="Train")
    plt.plot(list(range(21)), test_output, label="Test")
    plt.xticks(list(range(21)))
    plt.legend()
    plt.show()
