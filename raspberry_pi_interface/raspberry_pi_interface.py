import RPi.GPIO as GPIO
import socket

class RaspberryPiInterface:
    def __init__(self):
        self.GPIO = GPIO
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def initialize_hardware(self):
        print("Initializing Raspberry Pi hardware...")
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get_network_traffic_data(self):
        print("Getting network traffic data...")
        data = self.socket.recv(1024)
        return data.decode("utf-8")
