import numpy as np

def create_q_table():
    return np.array([
        [8, 3, 1],
        [4, 7, 2],
        [2, 4, 8]
    ])


def choose_action(state, q_table):
    return np.argmax(q_table[state])