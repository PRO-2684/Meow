import tensorflow as tf
from  argparse import ArgumentParser


parser = ArgumentParser(description='Evaluate model accuracy and loss.')
parser.add_argument('-m', '--model', help='Model directory path.', default='./model')
parser.add_argument('-e', '--eval', help='Image dataset directory for evaluating.')
args = parser.parse_args()
AUTOTUNE = tf.data.experimental.AUTOTUNE
model = tf.keras.models.load_model(args.model)
eval_ds = tf.keras.utils.image_dataset_from_directory(args.eval)
loss, accu = model.evaluate(eval_ds)
print("Test loss:", loss)
print("Test accuracy:", accu)
