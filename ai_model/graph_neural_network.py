import tensorflow as tf
from tensorflow import keras

class GraphNeuralNetwork:
    def __init__(self, num_layers, hidden_size):
        self.num_layers = num_layers
        self.hidden_size = hidden_size

    def graph_convolution(self, inputs, adjacency_matrix):
        outputs = []
        for i in range(self.num_layers):
            outputs.append(self.graph_convolution_layer(inputs, adjacency_matrix))
            inputs = outputs[-1]
        return outputs[-1]

    def graph_convolution_layer(self, inputs, adjacency_matrix):
        weights = keras.layers.Dense(self.hidden_size)(inputs)
        outputs = tf.matmul(adjacency_matrix, weights)
        return outputs

    def graph_pooling(self, inputs, pooling_matrix):
        outputs = tf.matmul(pooling_matrix, inputs)
        return outputs

    def graph_neural_network_model(self, inputs, adjacency_matrix, pooling_matrix):
        outputs = self.graph_convolution(inputs, adjacency_matrix)
        outputs = self.graph_pooling(outputs, pooling_matrix)
        return outputs
