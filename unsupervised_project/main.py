import numpy as np

from src.kmeans import run_kmeans
from src.anomaly import estimate_gaussian, multivariate_gaussian, select_threshold
from src.recommender import recommend_by_cluster
from src.rl_recommender import create_q_table, choose_action


# -------------------------
# 1. DATA
# -------------------------
X = np.array([
    [1, 2],
    [2, 1],
    [1.5, 1.8],
    [8, 9],
    [9, 8],
    [8.5, 9.2],
    [50, 60]
])


# -------------------------
# 2. K-MEANS CLUSTERING
# -------------------------
initial_centroids = np.array([
    [1, 1],
    [9, 9]
])

centroids, idx = run_kmeans(X, initial_centroids, 10)

print("\n========================")
print("=== K-MEANS RESULTS ===")
print("========================")
print("Cluster assignments:", idx)
print("Centroids:\n", centroids)


# -------------------------
# 3. ANOMALY DETECTION
# -------------------------
mu, sigma2 = estimate_gaussian(X)
p_val = multivariate_gaussian(X, mu, sigma2)

y_val = np.array([0, 0, 0, 0, 0, 0, 1])  # only for evaluation

epsilon, f1 = select_threshold(y_val, p_val)
anomalies = p_val < epsilon

print("\n=================================")
print("=== ANOMALY DETECTION RESULTS ===")
print("=================================")
print("Epsilon:", epsilon)
print("F1 Score:", f1)
print("Anomalies:", anomalies)


# -------------------------
# 4. RECOMMENDER SYSTEM
# -------------------------
user_index = 0  # choose a user to test

recommendations = recommend_by_cluster(X, idx, user_index, top_n=3)

print("\n========================")
print("=== RECOMMENDER ===")
print("========================")
print(f"User {user_index} cluster:", idx[user_index])
print("Recommended similar users:", recommendations)


# -------------------------
# 5. REINFORCEMENT LEARNING
# -------------------------
q_table = create_q_table()

state = 0  # example: Beginner state
action = choose_action(state, q_table)

actions = ["Study Python", "Study SQL", "Study ML"]

print("\n=================================")
print("=== REINFORCEMENT LEARNING ===")
print("=================================")
print("State:", state)
print("Best action:", actions[action])