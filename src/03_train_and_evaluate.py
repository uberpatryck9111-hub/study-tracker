# ============================================================
# EXERCISE 3: Compile, Train & Evaluate the Network
# ============================================================
# 📖 CONCEPT — Training has 3 steps:
#
#   1. COMPILE  → tell Keras HOW to train
#                 - optimizer: algorithm that updates weights (Adam is standard)
#                 - loss:      what we're trying to minimize
#                 - metrics:   what we want to track (accuracy)
#
#   2. FIT      → actually run training
#                 - feed it X_train and y_train
#                 - pick number of epochs (passes through the data)
#                 - pick batch_size (how many samples per weight update)
#
#   3. EVALUATE → test on data the model has NEVER seen (X_test)
#
# 🎯 GOAL: Get >95% accuracy on the test set
# ============================================================

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# ── Reload data (same as Exercise 2) ─────────────────────────
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(-1, 784) / 255.0
X_test  = X_test.reshape(-1, 784)  / 255.0


# ── Rebuild model (copy your solution from Exercise 2) ───────
def build_model():
    # 💡 HINT: Paste your working model from 02_build_network.py here
    #          3 layers: Dense(25, relu) → Dense(15, relu) → Dense(10, softmax)
    model = None  # ← replace with your Sequential model
    return model


# ============================================================
# TODO 1: Compile the model
#
# Use these settings (standard for multi-class classification):
#   optimizer = 'adam'
#   loss      = 'sparse_categorical_crossentropy'
#   metrics   = ['accuracy']
#
# 📖 Why sparse_categorical_crossentropy?
#   "sparse" means labels are integers (0,1,2...) not one-hot vectors
#   "categorical" means multi-class (more than 2 classes)
# ============================================================
def compile_model(model):
    # 💡 HINT: model.compile(optimizer=..., loss=..., metrics=[...])
    pass  # ← replace with model.compile(...)
    return model


# ============================================================
# TODO 2: Train the model
#
# Call model.fit() with:
#   - X_train, y_train
#   - epochs=10        (10 passes through the training data)
#   - batch_size=32    (update weights every 32 samples)
#   - validation_split=0.1  (hold out 10% of training data to watch for overfitting)
# ============================================================
def train_model(model):
    # 💡 HINT: history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)
    #          The returned 'history' object stores loss & accuracy per epoch — keep it!
    history = None  # ← replace with model.fit(...)
    return history


# ============================================================
# TODO 3: Evaluate on the test set
#
# Call model.evaluate(X_test, y_test) and print the results
# ============================================================
def evaluate_model(model):
    # 💡 HINT: test_loss, test_acc = model.evaluate(X_test, y_test)
    #          Then print them with f-strings
    pass


# ============================================================
# BONUS: Plot training curves
# This shows accuracy over epochs — helps you spot overfitting!
# Overfitting = training accuracy >> validation accuracy
# ============================================================
def plot_history(history):
    if history is None:
        print("❌ history is None — complete TODO 2 first!")
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # Accuracy
    ax1.plot(history.history['accuracy'],     label='Train Accuracy')
    ax1.plot(history.history['val_accuracy'], label='Val Accuracy')
    ax1.set_title("Accuracy over Epochs")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Accuracy")
    ax1.legend()
    ax1.grid(True)

    # Loss
    ax2.plot(history.history['loss'],     label='Train Loss')
    ax2.plot(history.history['val_loss'], label='Val Loss')
    ax2.set_title("Loss over Epochs")
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Loss")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig("training_curves.png")
    plt.show()
    print("✅ Training curves saved as training_curves.png")


# ============================================================
# REFLECTION QUESTIONS (answer in comments):
#
# After training, look at your curves and think about:
# Q1: Does your validation accuracy track with training accuracy?
#     If val_accuracy << train_accuracy → OVERFITTING. How to fix?
#     💡 Hint: add more data, add Dropout layers, reduce model size
#
# Q2: What happens if you increase epochs to 30?
#     Try it and observe!
#
# Q3: Andrew Ng talks about the "bias/variance tradeoff."
#     High training error = HIGH BIAS (underfitting)
#     High val error, low train error = HIGH VARIANCE (overfitting)
#     Which does your model have?
# ============================================================


if __name__ == "__main__":
    model = build_model()
    if model:
        compile_model(model)
        history = train_model(model)
        evaluate_model(model)
        plot_history(history)
        model.save("digit_model_trained.keras")
        print("\n✅ Trained model saved! Open 04_multiclass_softmax.py next.")
