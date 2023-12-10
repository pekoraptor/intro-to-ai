import csv


def read_from_csv(file_path: str, start=0, end=float('inf')):
    x = []
    y = []
    with open(file_path, 'r') as fh:
        reader = csv.DictReader(fh, delimiter=";")
        # , fieldnames=[id, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio]
        for i, row in enumerate(reader):
            if i < start:
                continue
            elif i == end:
                break
            x.append((
                int(row.get("age")),
                int(row.get("gender")),
                int(row.get("height")),
                int(float(row.get("weight"))),
                int(row.get("ap_hi")),
                int(row.get("ap_lo")),
                int(row.get("cholesterol")),
                int(row.get("gluc")),
                int(row.get("smoke")),
                int(row.get("alco")),
                int(row.get("active"))
            ))
            y.append(int(row.get("cardio")))
    return x, y


def format_data(X: list, indexes: list, precisions: list):
    for i, sample in enumerate(X):
        new_sample = list(sample)
        for index, precision in zip(indexes, precisions):
            new_sample[index] = round(new_sample[index] / precision) * precision
        X[i] = tuple(new_sample)
    return X
