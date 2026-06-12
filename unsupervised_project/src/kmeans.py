import numpy as np


def find_closest_centroids(X, centroids):
    K = centroids.shape[0]
    idx = np.zeros(X.shape[0], dtype=int)

    for i in range(len(X)):
        distances = []

        for k in range(K):
            dist = np.sum((X[i] - centroids[k]) ** 2)
            distances.append(dist)

        idx[i] = np.argmin(distances)

    return idx


def compute_centroids(X, idx, K):
    m, n = X.shape
    centroids = np.zeros((K, n))

    for k in range(K):
        points = X[idx == k]

        if len(points) > 0:
            centroids[k] = np.mean(points, axis=0)
        else:
            centroids[k] = np.zeros(n)

    return centroids


def run_kmeans(X, centroids, iterations):
    for _ in range(iterations):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_centroids(X, idx, centroids.shape[0])

    return centroids, idx