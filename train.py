import tensorflow as tf
from random import randint
from os import listdir
# import matplotlib.pyplot as plt
# To js: https://www.cnblogs.com/tujia/p/13862365.html
# https://github.com/El-Chiang/CatFace

data_dir = 'ustc'
batch_size = 16
img_size = (256, 256)
seed = randint(1, 10000)
print('Seed:', seed)
def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, img_size)
    return image
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
    tf.keras.layers.Conv2D(nb_filters, nb_conv, nb_conv, activation='relu', input_shape=(3,) + img_size),
    tf.keras.layers.Conv2D(nb_filters, nb_conv, nb_conv),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(nb_pool, nb_pool)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(num_classes),
    tf.keras.layers.Activation('softmax')
])
model.compile(
    optimizer='adam',
    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=['accuracy']
)
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=8
)
model.save('./model_964')
