import pandas as pd
from sklearn.ensemble import IsolationForest

class RealTimeAnomalyDetection:
    def __init__(self):
        self.model = IsolationForest()

    def fit(self, data):
        self.model.fit(data)

    def predict(self, data):
        predictions = self.model.predict(data)
        return predictions

    def detect_anomalies(self, data):
        predictions = self.predict(data)
        anomalies = []
        for i, prediction in enumerate(predictions):
            if prediction == -1:
                anomalies.append(data.iloc[i])
        return anomalies
