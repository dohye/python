# -*- coding: utf-8 -*-
"""
date : 191208
note : logistic regression_class (mnist example)
"""

import tensorflow as tf
import numpy as np

class logistic():

    def setup(self, num_features, num_classes, gpu):

        # gpu
        gpus = tf.config.experimental.list_physical_devices('GPU') # CUDA_VISIBLE_DEVICES에 포함된 GPU의 list 가져오기
        tf.config.experimental.set_visible_devices(gpus[gpu], 'GPU') # 텐서플로가 특정 GPU만 사용하도록 제한
        tf.config.experimental.set_memory_growth(gpus[gpu], True) # 특정 GPU의 메모리 증가를 허용
        # gpus[gpu]는 런타임에서 할당하는데 필요한 양만큼의 GPU 메모리를 할당하게 해줌
        
        # weights parameters(initialized)
        W = tf.Variable(tf.ones([num_features, num_classes]), name="weight")
        b = tf.Variable(tf.zeros([num_classes]), name="bias")

        self.W = W
        self.b = b
        
        self.num_features = num_features
        self.num_classes = num_classes

    def set_data(self): # 데이터 불러오기
        
        # data load
        from tensorflow.keras.datasets import mnist
        (x_train, y_train),(x_test,y_test) = mnist.load_data()
        
        x_train, x_test = np.array(x_train, np.float32), np.array(x_test, np.float32)
        x_train, x_test = x_train.reshape([-1, self.num_features]), x_test.reshape([-1,self.num_features])
        x_train, x_test = x_train/255., x_test/255. # scale transform

        return x_train, x_test, y_train, y_test # training에서 쓰기 위해 return받음

    def model(self, x, y): # placeholder가 없으므로 x,y를 training에서 batch만큼 받아오도록 수정함

        # logistic regression
        logits = tf.matmul(x, self.W) + self.b        
        pred = tf.nn.softmax(logits)
     
        # cost
        y_true = tf.one_hot(y, depth=self.num_classes)
        pred = tf.clip_by_value(pred, 1e-8, 1.)
        cost = -tf.reduce_mean(y_true * tf.math.log(pred) + (1 - y_true) * tf.math.log(1 - pred))

        # accuracy
        correct_prediction = tf.equal(tf.argmax(pred, 1),tf.cast(y, tf.int64))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
  
        # symbols in computation graph
        self.pred = pred
        self.cost = cost
        self.accuracy = accuracy
                
    def training(self, n_epochs, batch_size, learning_rate):
        
        # data
        x_train, x_test, y_train, y_test = self.set_data()
        train_data = tf.data.Dataset.from_tensor_slices((x_train, y_train))
        train_data = train_data.repeat().shuffle(x_train.shape[0]).batch(batch_size)

        # training
        for epoch, (batch_x, batch_y) in enumerate(train_data.take(n_epochs)):
            
            # gradient   
            optimizer = tf.optimizers.SGD(learning_rate)        
            
            with tf.GradientTape() as tape:
                self.model(batch_x, batch_y) 
                # batch_x, batch_y가 들어올 때마다 setup계산을 수행하면서 cost를 최적화 해야함
                
            parameters = [self.W, self.b]
            gradients = tape.gradient(self.cost, parameters)
            optimizer.apply_gradients(zip(gradients, parameters))

            if (epoch + 1) % 100 == 0:
                print("epoch: %i, loss: %f, accuracy: %f" % (epoch + 1, self.cost, self.accuracy))
                

#############################################################################
                
# dataset parameters
num_classes = 10
num_features = 784

# learning parameters
learning_rate = 0.01
batch_size = 256
n_epochs = 3000

# gpu number
gpu = 0

classifier = logistic()
classifier.setup(num_features, num_classes, gpu)
classifier.training(n_epochs, batch_size, learning_rate)

#############################################################################

