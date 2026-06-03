import tensorflow as tf
import numpy as np

(X_train,y_train),(X_test,y_test)=tf.keras.datasets.mnist.load_data()
X_train=X_train.reshape(-1,784)/255.0
X_test=X_test.reshape(-1,784)/255.0

z=np.array([2.0,1.0,0.1])
e=np.exp(z)
print("Softmax:",e/e.sum())

model=tf.keras.Sequential([tf.keras.layers.Dense(25,activation="relu"),tf.keras.layers.Dense(15,activation="relu"),tf.keras.layers.Dense(10,activation="linear")])
model.compile(optimizer="adam",loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=["accuracy"])
model.fit(X_train,y_train,epochs=10,batch_size=32,validation_split=0.1)
logits=model.predict(X_test[7:8])
probs=tf.nn.softmax(logits).numpy()[0]
print("Predicted:",probs.argmax(),"True:",y_test[7])
