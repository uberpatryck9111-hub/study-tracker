import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(-1, 784) / 255.0
X_test  = X_test.reshape(-1, 784)  / 255.0

def my_softmax(z):
    return np.exp(z) / np.sum(np.exp(z))

def test_softmax():
    z = np.array([2.0, 1.0, 0.1])
    probs = my_softmax(z)
    print("Softmax input:  " + str(z))
    print("Softmax output: " + str(probs))
    print("Sum: " + str(round(float(np.sum(probs)), 6)) + " should be 1.0")

def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(units=25, activation='relu'),
        tf.keras.layers.Dense(units=15, activation='relu'),
        tf.keras.layers.Dense(units=10, activation='linear'),
    ])
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )
    return model

def predict_one(model, index=0):
    image = X_test[index:index+1]
    logits = model.predict(image)
    probs = tf.nn.softmax(logits).numpy()[0]
    pred = np.argmax(probs)
    true_label = y_test[index]
    print("True label: " + str(true_label))
    print("Predicted:  " + str(pred))
    for digit, p in enumerate(probs):
        bar = "X" * int(p * 40)
        marker = " <- predicted" if digit == pred else ""
        print("Digit " + str(digit) + ": " + str(round(float(p), 4)) + "  " + bar + marker)
    plt.imshow(X_test[index].reshape(28, 28), cmap="gray")
    plt.title("True: " + str(true_label) + " Predicted: " + str(pred))
    plt.axis("off")
    plt.savefig("prediction_sample.png")
    plt.show()

if __name__ == "__main__":
    test_softmax()
    model = build_model()
    print("Training...")
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)
    predict_one(model, index=7)
    print("You completed all 4 exercises!")