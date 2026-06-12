import numpy as np


def estimate_gaussian(X):
    mu = np.mean(X, axis=0)
    sigma2 = np.var(X, axis=0)
    return mu, sigma2


def multivariate_gaussian(X, mu, sigma2):
    return np.exp(-np.sum((X - mu) ** 2 / (2 * sigma2), axis=1))


def select_threshold(y_val, p_val):
    best_epsilon = 0
    best_f1 = 0

    stepsize = (max(p_val) - min(p_val)) / 1000
    epsilons = np.arange(min(p_val), max(p_val), stepsize)

    for epsilon in epsilons:
        predictions = (p_val < epsilon)

        tp = np.sum((predictions == 1) & (y_val == 1))
        fp = np.sum((predictions == 1) & (y_val == 0))
        fn = np.sum((predictions == 0) & (y_val == 1))

        precision = tp / (tp + fp + 1e-8)
        recall = tp / (tp + fn + 1e-8)

        f1 = 2 * precision * recall / (precision + recall + 1e-8)

        if f1 > best_f1:
            best_f1 = f1
            best_epsilon = epsilon

    return best_epsilon, best_f1