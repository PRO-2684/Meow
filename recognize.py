import tensorflow as tf
from sys import argv
from os.path import isfile
from numpy import argmax


AUTOTUNE = tf.data.experimental.AUTOTUNE
model = tf.keras.models.load_model('./model')
cats = ['a', 'b', 'c', 'd', 'e', 'f']

def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    # image /= 255.0  # normalize to [0,1] range
    return image

paths = [path for path in argv if (isfile(path) and path.endswith('.jpg'))]
path_ds = tf.data.Dataset.from_tensor_slices(paths)
img_ds = path_ds.map(load_and_preprocess_image).batch(len(path_ds)).prefetch(buffer_size=AUTOTUNE)
prediction = [ probs for probs in model(next(iter(img_ds))) ]
for index, probs in enumerate(prediction):
    cat_n = argmax(probs)
    cat = cats[cat_n]
    prob = probs[cat_n]
    print(f'"{paths[index]}": Cat "{cat}", probability {prob * 100:.3f}%.')



