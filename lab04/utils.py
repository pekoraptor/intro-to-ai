import csv


def read_from_csv(file_path: str, start: int, end: int):
    x = []
    y = []
    with open(file_path, 'r') as fh:
        reader = csv.DictReader(fh, delimiter=";")
        # , fieldnames=[id, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio]
        for i, row in enumerate(reader):
            if i < start:
                pass
            elif i > end:
                break
            x.append((
                row.get("age"),
                row.get("gender"),
                row.get("height"),
                row.get("weight"),
                row.get("ap_hi"),
                row.get("ap_lo"),
                row.get("cholesterol"),
                row.get("gluc"),
                row.get("smoke"),
                row.get("alco"),
                row.get("active")
            ))
            y.append(row.get("cardio"))
    return x, y


def format_data(X: list, indexes: list, precisions: list):
    for sample in X:
        for index, precision in zip(indexes, precisions):
            X[index] = round(X[index] / precision) * precision
    return X
