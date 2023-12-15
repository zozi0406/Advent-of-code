import pandas as pd
import numpy as np


def compute_diff(series):
    diff = series.diff()[1:]
    diff = diff.to_list()
    print(f"Diff: {diff}")
    if diff == [0] * len(diff):
        return series.to_list()[0]
    else:
        print(series)
        return series.to_list()[0] - compute_diff(pd.Series(diff))


with open("./Day9/input.txt", encoding="utf-8") as f:
    results = list()
    for line in f.readlines():
        history = pd.Series([int(num) for num in line.strip().split(" ")])
        prediction = compute_diff(history)
        print(prediction)
        results.append(prediction)

    print(int(np.sum(results)))
