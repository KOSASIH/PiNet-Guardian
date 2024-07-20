import tensorflow as tf
from tensorflow import keras

class AttentionModule:
    def __init__(self, num_heads, hidden_size):
        self.num_heads = num_heads
        self.hidden_size = hidden_size

    def attention(self, query, key, value):
        attention_scores = tf.matmul(query, key, transpose_b=True)
        attention_scores = attention_scores / tf.sqrt(self.hidden_size)
        attention_weights = tf.nn.softmax(attention_scores, axis=-1)
        output = tf.matmul(attention_weights, value)
        return output

    def multi_head_attention(self, query, key, value):
        outputs = []
        for i in range(self.num_heads):
            output = self.attention(query, key, value)
            outputs.append(output)
        output = tf.concat(outputs, axis=-1)
        return output

    def attention_layer(self, inputs):
        query = keras.layers.Dense(self.hidden_size)(inputs)
        key = keras.layers.Dense(self.hidden_size)(inputs)
        value = keras.layers.Dense(self.hidden_size)(inputs)
        output = self.multi_head_attention(query, key, value)
        return output
