import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    mvsd = np.array(list).reshape([3, 3])
    calculations = {
        "mean": [mvsd.mean(0).tolist(), mvsd.mean(1).tolist(), mvsd.mean()],
        "variance": [mvsd.var(0).tolist(), mvsd.var(1).tolist(), mvsd.var()],
        "standard deviation": [mvsd.std(0).tolist(), mvsd.std(1).tolist(), mvsd.std()],
        "max": [mvsd.max(0).tolist(), mvsd.max(1).tolist(), mvsd.max()],
        "min": [mvsd.min(0).tolist(), mvsd.min(1).tolist(), mvsd.min()],
        "sum": [mvsd.sum(0).tolist(), mvsd.sum(1).tolist(), mvsd.sum()],
    }
    return calculations