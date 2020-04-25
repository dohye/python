"""
date : 191205
note : logistic regression (mnist example)
"""

import tensorflow as tf
import numpy as np

# dataset parameters
num_classes = 10
num_features = 784

# learning parameters
learning_rate = 0.01
batch_size = 256

# data load
from tensorflow.keras.datasets import mnist
(x_train, y_train),(x_test,y_test) = mnist.load_data()

x_train, x_test = np.array(x_train, np.float32), np.array(x_test, np.float32)
x_train, x_test = x_train.reshape([-1, num_features]), x_test.reshape([-1,num_features])
x_train, x_test = x_train/255., x_test/255. # scale

train_data = tf.data.Dataset.from_tensor_slices((x_train,y_train))
train_data = train_data.repeat().shuffle(x_train.shape[0]).batch(batch_size) # shuffle은 원하는 만큼

# weight, bias
W = tf.Variable(tf.ones([num_features, num_classes]), name="weight")
b = tf.Variable(tf.ones([num_classes]), name="bias")

# function
 
def logistic_regression(x):
    logits = tf.matmul(x,W)+b
    predictions = tf.nn.softmax(logits)
    return predictions

def cross_entropy(y_pred, y_true):
    y_true = tf.one_hot(y_true, depth=num_classes)
    y_pred = tf.clip_by_value(y_pred, 1e-8, 1.)
    loss = -tf.reduce_mean(y_true * tf.math.log(y_pred)+(1-y_true) * tf.math.log(1-y_pred))
    return loss

def accuracy(y_pred, y_true):
    correct_prediction = tf.equal(tf.argmax(y_pred,1),tf.cast(y_true, tf.int64))
    acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    return acc

## gradient
optimizer = tf.optimizers.SGD(learning_rate)

def gradient(x,y):
    with tf.GradientTape() as g:
        pred = logistic_regression(x) # loss 계산을 위해 추가
        loss = cross_entropy(pred,y)
    
    gradients = g.gradient(loss, [W,b])
    optimizer.apply_gradients(zip(gradients,[W,b]))

## training
for epoch, (batch_x, batch_y) in enumerate(train_data.take(3000)):
    gradient(batch_x, batch_y)

    pred = logistic_regression(batch_x)
    loss = cross_entropy(pred, batch_y)
    acc = accuracy(pred,batch_y)

    if (epoch + 1) % 100 == 0:
       print("epoch: %i, loss: %f, accuracy: %f" % (epoch + 1, loss, acc))
