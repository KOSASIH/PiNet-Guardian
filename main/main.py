import os
import sys
import time
from ai_model import AnomalyDetectionModel
from raspberry_pi_interface import RaspberryPiInterface
from network_communication import NetworkCommunication
from data_analysis import DataAnalysis

class PiNetGuardian:
    def __init__(self):
        self.ai_model = AnomalyDetectionModel()
        self.rpi_interface = RaspberryPiInterface()
        self.network_communication = NetworkCommunication()
        self.data_analysis = DataAnalysis()

    def start_system(self):
        print("Starting PiNet Guardian system...")
        self.rpi_interface.initialize_hardware()
        self.network_communication.connect_to_network()
        self.ai_model.load_model()
        self.data_analysis.initialize_data_storage()

    def monitor_network_traffic(self):
        print("Monitoring network traffic...")
        while True:
            traffic_data = self.rpi_interface.get_network_traffic_data()
            self.ai_model.predict(traffic_data)
            self.data_analysis.store_data(traffic_data)
            time.sleep(1)

    def run(self):
        self.start_system()
        self.monitor_network_traffic()

if __name__ == "__main__":
    pignet_guardian = PiNetGuardian()
    pignet_guardian.run()
