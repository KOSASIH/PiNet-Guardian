import socket

class SocketHandler:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self, server_ip, server_port):
        self.socket.connect((server_ip, server_port))

    def send_data(self, data):
        self.socket.sendall(data.encode("utf-8"))
