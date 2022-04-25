import tensorflow as tf
from random import randint
# import matplotlib.pyplot as plt
# https://github.com/El-Chiang/CatFace

data_dir = 'testdata'
batch_size = 16
img_size = (256, 256)
seed = randint(1, 10000)
print('Seed:', seed)

train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='training',
    seed=seed,
    # image_size=img_size,
    batch_size=batch_size
)
val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='validation',
    seed=seed,
    # image_size=img_size,
    batch_size=batch_size
)

class_names = train_ds.class_names
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

num_classes = len(class_names)
nb_epoch = 16
nb_filters = 32  # number of convolutional filter
nb_pool = 2  # size of pooling area for max pooling
nb_conv = 3  # convolution kernal size
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255),
    # tf.keras.layers.Conv2D(32, 3, activation='relu'),
    # tf.keras.layers.MaxPooling2D(),
    # tf.keras.layers.Dropout(0.1),
    # tf.keras.layers.Conv2D(32, 3, activation='relu'),
    # tf.keras.layers.MaxPooling2D(),
    # tf.keras.layers.Dropout(0.1),
    # tf.keras.layers.Flatten(),
    # tf.keras.layers.Dense(128, activation='relu'),
    # tf.keras.layers.Dense(num_classes)
    tf.keras.layers.Conv2D(nb_filters, nb_conv, nb_conv, activation='relu', input_shape=(1, )+img_size),
    tf.keras.layers.Conv2D(nb_filters, nb_conv, nb_conv),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(nb_pool, nb_pool)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(num_classes),
    tf.keras.layers.Activation('softmax')
])
'''
    model = Sequential()
    model.add(Conv2D(nb_filters, nb_conv, nb_conv,
                            border_mode='valid', 
                            activation='relu',  # use rectifier linear units: max(0.0, x)
                            input_shape=(1, 150, 150)))
    # second convolution layer with 6 filters of size 3*3
    model.add(Conv2D(nb_filters, nb_conv, nb_conv))
    model.add(Activation('relu'))
    # max pooling layer, pool size is 2*2
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
    # drop out of max-pooling layer, drop out rate is 0.25
    model.add(Dropout(0.25))
    # flatten inputs from 2d to 1d
    model.add(Flatten())
    # add fully connected layer with 128 hidden units
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    # output layer with softmax
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))
'''
model.compile(
    optimizer='adam',
    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=8
)

