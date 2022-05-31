import tensorflow as tf


AUTOTUNE = tf.data.experimental.AUTOTUNE
model = tf.keras.models.load_model('./model')
eval_ds = tf.keras.utils.image_dataset_from_directory('./ustc_eval')
loss, accu = model.evaluate(eval_ds)
print("Test loss:", loss)
print("Test accuracy:", accu)
