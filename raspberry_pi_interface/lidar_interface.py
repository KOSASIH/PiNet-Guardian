import serial

class LidarInterface:
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.lidar = serial.Serial(self.serial_port, 115200)

    def read_lidar_data(self):
        data = self.lidar.readline()
        return data.decode("utf-8")

    def send_lidar_command(self, command):
        self.lidar.write(command.encode("utf-8"))
