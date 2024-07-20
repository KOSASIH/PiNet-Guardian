import pandas as pd
from sklearn.ensemble import IsolationForest

class AnomalyDetection:
    def __init__(self):
        self.model = IsolationForest()

    def fit(self, data):
        self.model.fit(data)

    def predict(self, data):
        return self.model.predict(data)

    def visualize_anomalies(self, data):
        print("Visualizing anomalies...")
        anomalies = self.predict(data)
        plt.scatter(data[:, 0], data[:, 1], c=anomalies)
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.show()
