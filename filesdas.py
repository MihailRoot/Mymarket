import tensorflow as tf
from tensorflow import keras as k
from tensorflow.keras.datasets import fashion_mnist
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense,Flatten,Conv2D

(x_train,y_train), (x_test,y_test) = fashion_mnist.load_data()

y_train = np.asarray(x_train).astype('float32').reshape((-1,1))
x_train = np.asarray(y_train).astype('float32').reshape((-1,1))
x_train,y_train / 255
x_test,y_test / 255

model = k.Sequential()

model.add(Conv2D(64,21,3,input_shape=(400,28,32)))

model.add(Conv2D(120,51,12,input_shape=(400,28,41)))

model.compile(loss='binary_crossentropy',metrics=["accuracy"],optimizer='adam')
model.fit(x_train,y_train,epochs=10)
plt.show()