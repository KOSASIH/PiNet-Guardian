import socket

class NetworkCommunication:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_network(self):
        print("Connecting to decentralized network...")
        self.socket.connect(("192.168.1.100", 8080))

    def send_data(self, data):
        print("Sending data to network...")
        self.socket.sendall(data.encode("utf-8"))
