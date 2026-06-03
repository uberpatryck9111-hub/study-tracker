# ============================================================
# EXERCISE 4: Multi-class Classification & Softmax Deep Dive
# ============================================================
# 📖 CONCEPT — Softmax turns raw scores into probabilities:
#
#   Raw output (logits): [2.1,  0.3, -1.5,  4.8, ...]
#   After softmax:       [0.04, 0.01, 0.0,  0.88, ...]
#                                              ↑
#                                     Model is 88% sure this is a "3"
#
#   Key property: all probabilities SUM to 1.0
#
#   Softmax formula for class j:
#       P(j) = e^(z_j) / sum(e^(z_k) for all k)
#
# 📖 Andrew Ng's important note:
#   In TensorFlow, for NUMERICAL STABILITY it is better to:
#     - Use linear activation in the output layer (outputs = logits)
#     - Set from_logits=True in the loss function
#   This avoids floating point errors from computing softmax twice.
#
# 🎯 GOAL: Understand softmax, make predictions, read probabilities
# ============================================================

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# ── Load data ─────────────────────────────────────────────────
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(-1, 784) / 255.0
X_test  = X_test.reshape(-1, 784)  / 255.0


# ============================================================
# TODO 1: Implement softmax yourself
#
# Formula:  softmax(z)_j = e^(z_j) / sum(e^(z_k))
# ============================================================
def my_softmax(z):
    """
    z: a 1D numpy array of raw scores (logits)
    returns: array of probabilities that sum to 1
    """
    # 💡 HINT: Step 1 — compute e^z for each element: np.exp(z)
    # 💡 HINT: Step 2 — divide each element by the sum: / np.sum(...)
    pass  # ← write your formula


def test_softmax():
    z = np.array([2.0, 1.0, 0.1])
    probs = my_softmax(z)
    print("--- Softmax Test ---")
    print(f"Input:        {z}")
    print(f"Output:       {probs}")
    print(f"Sum of probs: {np.sum(probs):.6f}  ← should be 1.0")
    # ✅ Expected: roughly [0.659, 0.242, 0.099] and sum = 1.0


# ============================================================
# TODO 2: Build the "numerically stable" version of the model
#
# Change the output layer to use activation='linear'  (no softmax here!)
# Then in compile(), use:
#   loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
#
# 📖 This is the version Andrew Ng recommends in lectures.
#    TF will apply softmax internally during loss computation — more stable.
# ============================================================
def build_stable_model():
    # 💡 HINT: Same as before BUT last layer uses activation='linear'
    model = None  # ← replace with your model
    return model


# ============================================================
# TODO 3: Train this stable model (same compile/fit as Exercise 3)
# ============================================================
def train_stable_model(model):
    # 💡 HINT: compile with from_logits=True loss, then fit for 10 epochs
    pass


# ============================================================
# TODO 4: Make a prediction and read the probability output
#
# After training, pick one test image and:
#   1. Get the raw output (logits) from model.predict()
#   2. Apply softmax to get probabilities
#   3. Take np.argmax() to get the predicted class
#   4. Compare to the true label
# ============================================================
def predict_one(model, index=0):
    """Predict the digit for X_test[index] and show a breakdown."""

    # 💡 HINT: image = X_test[index:index+1]   ← keep the batch dimension!
    #          logits = model.predict(image)
    #          probs  = tf.nn.softmax(logits).numpy()[0]
    #          pred   = np.argmax(probs)

    image  = None  # ← your code
    logits = None  # ← your code
    probs  = None  # ← your code
    pred   = None  # ← your code

    true_label = y_test[index]

    print(f"\n--- Prediction for test image #{index} ---")
    print(f"True label : {true_label}")
    print(f"Predicted  : {pred}")
    print(f"\nProbability breakdown:")
    if probs is not None:
        for digit, p in enumerate(probs):
            bar = "█" * int(p * 40)
            marker = " ← predicted" if digit == pred else ""
            print(f"  Digit {digit}: {p:.4f}  {bar}{marker}")

    # Show the image
    plt.imshow(X_test[index].reshape(28, 28), cmap="gray")
    plt.title(f"True: {true_label}  |  Predicted: {pred}")
    plt.axis("off")
    plt.savefig("prediction_sample.png")
    plt.show()


# ============================================================
# REFLECTION — The key ideas from this exercise:
#
# 1. Softmax output = probability distribution over classes
# 2. Always pick the class with the HIGHEST probability (argmax)
# 3. from_logits=True is more numerically stable — use it!
# 4. The model can be WRONG even when one probability is high
#    → this is called a "confident wrong prediction"
#    → Andrew Ng calls these cases worth inspecting carefully
#
# CHALLENGE: Find an image where the model is confidently wrong.
#   Try: loop through test images until pred != true_label
#        and the max probability is > 0.9
# ============================================================


if __name__ == "__main__":
    test_softmax()   # Test your manual softmax first

    model = build_stable_model()
    if model:
        train_stable_model(model)
        predict_one(model, index=7)   # try different index values!

        print("\n🎉 Congratulations! You've completed all 4 exercises.")
        print("   You built, trained, and evaluated a neural network.")
        print("   That's the core of Week 2!")
