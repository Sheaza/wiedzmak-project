import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator


train_img_gen = ImageDataGenerator(rescale=1./255,
                                    shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True)

train_set = train_img_gen.flow_from_directory('training',
                                               target_size=(227, 227),
                                               batch_size=32,
                                               class_mode="categorical")
print(train_set.class_indices.keys())

test_img_gen = ImageDataGenerator(rescale=1./255)
test_set = test_img_gen.flow_from_directory('test',
                                             target_size=(227, 227),
                                             batch_size=32,
                                             class_mode="categorical")

cnn = tf.keras.models.Sequential()
cnn.add(tf.keras.layers.Conv2D(filters=32,
                                kernel_size=3,
                                activation='relu',
                                input_shape=[227, 227, 3]))

cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='valid'))
cnn.add(tf.keras.layers.Conv2D(filters=32,
                                kernel_size=3,
                                activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='valid'))
cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
cnn.add(tf.keras.layers.Dense(units=4, activation='sigmoid'))

cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
cnn.fit(x=train_set, validation_data=test_set, epochs=25)
cnn.save('neuralnet')
