import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)

# TODO 1: Sigmoid —  formula: 1 / (1 + e^(-x))
def sigmoid(x):
    # 💡 HINT: return 1 / (1 + np.exp(-x))
    return 1/ (1+ np.exp(-x))

# TODO 2: ReLU — formula: max(0, x)
def relu(x):
    # 💡 HINT: return np.maximum(0, x)
    return np.maximum(0,x)

# TODO 3: Linear — formula: just return x
def linear(x):
    # 💡 HINT: return x
    return x

def check_sigmoid():
    print("--- Sigmoid checks ---")
    print(f"sigmoid(0)    = {sigmoid(0)}")    # should be 0.5
    print(f"sigmoid(100)  = {sigmoid(100)}")  # should be ~1.0
    print(f"sigmoid(-100) = {sigmoid(-100)}") # should be ~0.0

def plot_activations():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    fig.suptitle("Activation Functions — Week 2", fontsize=14)

    # TODO: replace None with your function calls
    axes[0].set_title("Sigmoid")
    axes[0].plot(x, sigmoid(x), color="blue")   # 💡 sigmoid(x)
    axes[0].grid(True)

    axes[1].set_title("ReLU")
    axes[1].plot(x, relu(x), color="orange") # 💡 relu(x)
    axes[1].grid(True)

    axes[2].set_title("Linear")
    axes[2].plot(x, linear(x), color="green")  # 💡 linear(x)
    axes[2].grid(True)

    plt.tight_layout()
    plt.savefig("activation_functions.png")
    plt.show()
    print("✅ Plot saved!")

if __name__ == "__main__":
    check_sigmoid()
    plot_activations()