# -*- coding: utf-8 -*-
"""
Made from the following tutorial:
https://www.youtube.com/watch?v=Zi4i7Q0zrBs&list=PL7yh-TELLS1EZGz1-VDltwdwZvPV-jliQ&index=8
"""


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import sys
import random

os.chdir(os.path.dirname(sys.argv[0]))


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Set epochs=3 later
model.fit(x_train, y_train, epochs=3)

loss, accuracy= model.evaluate(x_test, y_test)
print("Accuracy:", accuracy)
print("Loss:", loss)

model.save('digits.model')


samp = random.sample(range(1,9+1), 5)

#for x in range(1,9+1):
for x in samp:
    img = cv.imread(f'{x}.png')[:,:,0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    print('The result is probably', np.argmax(prediction))
    
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()