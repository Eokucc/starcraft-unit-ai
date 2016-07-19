# coding=utf-8

import tensorflow as tf


class Network:

    def __init__(self, network_shape):
        self.sess = tf.Session()

        if len(network_shape) < 2:
            raise Exception("Error: Need to specify at least nr of inputs and outputs when creating network.")
        self.input_vars  = tf.placeholder(tf.float32, shape=[None, network_shape[0] ])
        self.correct_out = tf.placeholder(tf.float32, shape=[None, network_shape[-1]])

        last_layer = self.input_vars
        size_last_layer = network_shape[0]

#        self.layer_hidden=[]
        self.weights=[]
        self.biases=[]

        for size_next_layer in network_shape[1:-1]:
            W = self.weight_variable([size_last_layer,size_next_layer])
            b = self.bias_variable([size_next_layer])
            self.weights.append(W)
            self.biases.append(b)

            next_layer = self.predicted_out = tf.nn.relu(tf.matmul(last_layer,W) + b)

            last_layer = next_layer
            size_last_layer = size_next_layer


        W = self.weight_variable(network_shape[-2:])
        b = self.bias_variable([network_shape[-1]])
        self.weights.append(W)
        self.biases.append(b)
        self.predicted_out = tf.nn.relu(tf.matmul(last_layer,W) + b)
        self.sess.run(tf.initialize_all_variables())



    def evaluate(self,my_input):
        feed_dict={self.input_vars:[my_input]}
        return self.sess.run(self.predicted_out, feed_dict = feed_dict)[0]  # return first element of list (because input has one dimension)

    def weight_variable(self, shape):
      initial = tf.truncated_normal(shape, stddev=0.1)
      return tf.Variable(initial)

    def bias_variable(self, shape):
      initial = tf.constant(0.1, shape=shape)
      return tf.Variable(initial)
