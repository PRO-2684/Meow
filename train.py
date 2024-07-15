import tensorflow as tf
from random import randint
from argparse import ArgumentParser
# import matplotlib.pyplot as plt
# To js: https://www.cnblogs.com/tujia/p/13862365.html
# https://github.com/El-Chiang/CatFace

parser = ArgumentParser(description='Train and save model for recognizing.')
parser.add_argument('-i', '--input', help='Image dataset directory for training.', required=True)
parser.add_argument('-o', '--output', help='Output model directory.', default='./model')
args = parser.parse_args()
data_dir = args.input
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
nb_epoch = 8
nb_filters = 32  # number of convolutional filter
nb_pool = 2  # size of pooling area for max pooling
nb_conv = 3  # convolution kernal size
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255), # normalize pixel values to be between 0 and 1
    tf.keras.layers.Conv2D(nb_filters, nb_conv, nb_conv, activation='relu', input_shape=(3,) + img_size), # 3 is the number of channels: RGB
    tf.keras.layers.Conv2D(nb_filters, nb_conv, nb_conv), # 3 is the number of channels: RGB
    tf.keras.layers.Activation('relu'), # ReLU activation function
    tf.keras.layers.MaxPooling2D(pool_size=(nb_pool, nb_pool)), # max pooling layer
    tf.keras.layers.Dropout(0.2), # apply dropout to prevent overfitting
    tf.keras.layers.Flatten(), # flatten the 2D arrays for fully connected layers
    tf.keras.layers.Dense(128, activation='relu'), # dense layer with 128 neurons
    tf.keras.layers.Activation('relu'), # ReLU activation function
    tf.keras.layers.Dropout(0.3), # apply dropout to prevent overfitting
    tf.keras.layers.Dense(num_classes), # dense layer with num_classes neurons
    tf.keras.layers.Activation('softmax') # softmax activation function
])
model.compile(
    optimizer='adam',
    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=['accuracy']
)
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=nb_epoch
)
model.save(args.output)
