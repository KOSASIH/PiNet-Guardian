import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

class AnomalyDetectionModel:
    def __init__(self):
        self.model = None
        self.scaler = MinMaxScaler()

    def load_model(self):
        print("Loading AI model...")
        self.model = keras.models.load_model("anomaly_detection_model.h5")

    def predict(self, traffic_data):
        print("Predicting anomalies...")
        scaled_data = self.scaler.transform(traffic_data)
        predictions = self.model.predict(scaled_data)
        anomalies = [i for i, x in enumerate(predictions) if x > 0.5]
        return anomalies
