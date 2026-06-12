import numpy as np

def recommend_by_cluster(X, labels, user_index, top_n=3):
    """
    X = user feature matrix
    labels = cluster labels form Kmeans
    user_index = user we want recommendations for
    """
    user_cluster = labels[user_index]

    similar_users = np.where(labels == user_cluster)[0]

    similar_users = similar_users[similar_users != user_index]

    return similar_users[:top_n]