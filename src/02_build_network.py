import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

print("Loading MNIST dataset...")
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train / 255.0
X_test  = X_test  / 255.0
X_train = X_train.reshape(-1, 784)
X_test  = X_test.reshape(-1, 784)

print(f"Training samples : {X_train.shape[0]}")
print(f"Input features   : {X_train.shape[1]}")
print(f"Example label    : {y_train[0]}")

def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(units=25, activation='relu'),
        tf.keras.layers.Dense(units=15, activation='relu'),
        tf.keras.layers.Dense(units=10, activation='softmax'),
    ])
    model.summary()
    return model

def show_sample_image():
    sample = X_train[0].reshape(28, 28)
    plt.imshow(sample, cmap="gray")
    plt.title(f"Label: {y_train[0]}")
    plt.axis("off")
    plt.savefig("sample_digit.png")
    plt.show()
    print("✅ Sample image saved!")

if __name__ == "__main__":
    model = build_model()
    show_sample_image()
    model.save("digit_model_untrained.keras")
    print("\n✅ Model saved! Open 03_train_and_evaluate.py next.")