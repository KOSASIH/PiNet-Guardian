import pandas as pd
import matplotlib.pyplot as plt

class DataAnalysis:
    def __init__(self):
        self.data = pd.DataFrame(columns=["timestamp", "traffic_data"])

    def initialize_data_storage(self):
        print("Initializing data storage...")
        self.data.to_csv("traffic_data.csv", index=False)

    def store_data(self, traffic_data):
        print("Storing traffic data...")
        self.data = self.data.append({"timestamp": time.time(), "traffic_data": traffic_data}, ignore_index=True)
        self.data.to_csv("traffic_data.csv", index=False)

    def visualize_data(self):
        print("Visualizing traffic data...")
        plt.plot(self.data["timestamp"], self.data["traffic_data"])
        plt.xlabel("Timestamp")
        plt.ylabel("Traffic Data")
        plt.show()
