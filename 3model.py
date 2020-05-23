from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import matplotlib.pyplot as plt

import sys
import os
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense, Activation
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras import callbacks
import time

start = time.time()

DEV = False
argvs = sys.argv
argc = len(argvs)

if argc > 1 and (argvs[1] == "--development" or argvs[1] == "-d"):
  DEV = True

if DEV:
  epochs = 2
else:
  epochs = 20

train_data_path = 'cats_and_dogs_filtered/train/'
validation_data_path ='cats_and_dogs_filtered/validation/'


img_width, img_height = 150, 150
batch_size = 60
samples_per_epoch = 1000
validation_steps = 200
nb_filters1 = 32
nb_filters2 = 64
conv1_size = 3
conv2_size = 2
pool_size = 2
classes_num = 2
lr = 0.0008



model = Sequential()
model.add(Convolution2D(nb_filters1, 5, padding ="same", input_shape=(150,150, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(2,2))


model.add(Convolution2D(256, 3, padding ="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(2,2))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation("relu"))

model.add(Dense(classes_num, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=lr),
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    rescale=1. / 255, rotation_range=45,
                    )


test_datagen = ImageDataGenerator(rescale=1. / 255
                   )




train_generator = train_datagen.flow_from_directory(
    train_data_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',seed=50,shuffle=True,color_mode="rgb")




validation_generator = test_datagen.flow_from_directory(
    validation_data_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',shuffle=False,color_mode="rgb")

"""
Tensorboard log
"""
log_dir = './tf-log/'
tb_cb = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=0)
cbks = [tb_cb]


history = model.fit_generator(
    train_generator,
    steps_per_epoch=samples_per_epoch // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=validation_steps // batch_size
)
model.save('modelnews.h5')

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss=history.history['loss']
val_loss=history.history['val_loss']







model.save('model9.h5')
model.save_weights('weights.h5')

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

from keras.models import load_model
import cv2
model = load_model('model9.h5')


img = cv2.imread('aero1.jpg')
img = cv2.resize(img,(150,150))
img = np.reshape(img,[1,150,150,3])

classes = model.predict_classes(img)

print(classes)
