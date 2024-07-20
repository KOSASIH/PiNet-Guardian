import matplotlib.pyplot as plt

def visualize_data(data):
    plt.plot(data["timestamp"], data["traffic_data"])
    plt.xlabel("Timestamp")
    plt.ylabel("Traffic Data")
    plt.show()
