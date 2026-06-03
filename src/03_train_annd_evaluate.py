import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(-1, 784) / 255.0
X_test  = X_test.reshape(-1, 784)  / 255.0

def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(units=25, activation='relu'),
        tf.keras.layers.Dense(units=15, activation='relu'),
        tf.keras.layers.Dense(units=10, activation='softmax'),
    ])
    return model

def compile_model(model):
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

def train_model(model):
    history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)
    return history

def evaluate_model(model):
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print(f"Test loss:     {test_loss:.4f}")
    print(f"Test accuracy: {test_acc:.4f}")

def plot_history(history):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.plot(history.history['accuracy'], label='Train')
    ax1.plot(history.history['val_accuracy'], label='Val')
    ax1.set_title("Accuracy over Epochs")
    ax1.legend()
    ax1.grid(True)
    ax2.plot(history.history['loss'], label='Train')
    ax2.plot(history.history['val_loss'], label='Val')
    ax2.set_title("Loss over Epochs")
    ax2.legend()
    ax2.grid(True)
    plt.tight_layout()
    plt.savefig("training_curves.png")
    plt.show()
    print("Training curves saved!")

if __name__ == "__main__":
    model = build_model()
    compile_model(model)
    history = train_model(model)
    evaluate_model(model)
    plot_history(history)
    model.save("digit_model_trained.keras")
    print("Done! Open 04_multiclass_softmax.py next.")