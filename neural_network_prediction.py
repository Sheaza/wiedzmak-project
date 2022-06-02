import os

import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from tensorflow import keras
from oils import Oil
import joblib


class NeuralNet():

    model = None

    def __init__(self):
        self.model = keras.models.load_model('neuralnet')  # loading the model

    def predict(self, data):
        target_img = tf.keras.utils.load_img(data,
                                           target_size=(227, 227)) # loading image
        target_img = tf.keras.utils.img_to_array(target_img)
        target_img = np.expand_dims(target_img, axis=0)

        prediction = self.model.predict(target_img, batch_size=1)
        monster_class = np.argmax(prediction, axis=1)
        if monster_class == 0:
            print('Model predicted: Bandit')
        elif monster_class == 1:
            print('Model predicted: Griffin')
        elif monster_class == 2:
            print('Model predicted: Leshy')
        else:
            print('Model predicted: Wolf')
        return Oil(monster_class[0]) # return adequate oil enum

# tests

# model = tf.keras.models.load_model('C:\\Users\\user\\Desktop\\gowno\\wiedzmak-project\\neuralnet')  # loading the model
# test_img = tf.keras.utils.load_img('training/wolf/012-Eclipse-Sticks-Her-Tongue-Out.jpg', target_size=(227, 227))
# test_img = tf.keras.utils.img_to_array(test_img)
# test_img = np.expand_dims(test_img, axis=0)
#
# predict_x = model.predict(test_img, batch_size=1)
# classes_x = np.argmax(predict_x, axis=1)
# print(classes_x)