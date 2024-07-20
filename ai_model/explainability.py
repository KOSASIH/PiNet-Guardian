import tensorflow as tf
from tensorflow import keras

class Explainability:
    def __init__(self, model):
        self.model = model

    def saliency_map(self, input_data):
        print("Generating saliency map...")
        gradients = tf.gradients(self.model.output, input_data)
        saliency_map = tf.abs(gradients)
        return saliency_map

    def feature_importance(self):
        print("Calculating feature importance...")
        feature_importance = tf.keras.backend.sum(self.model.layers[-1].weights[0], axis=0)
        return feature_importance

    def visualize_explainability(self, input_data):
        print("Visualizing explainability...")
        saliency_map = self.saliency_map(input_data)
        feature_importance = self.feature_importance()
        plt.imshow(saliency_map, cmap="hot")
        plt.xlabel("Feature Importance")
        plt.ylabel("Saliency Map")
        plt.show()
