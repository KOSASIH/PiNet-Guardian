import RPi.GPIO as GPIO

class GPIOController:
    def __init__(self):
        self.GPIO = GPIO

    def set_gpio_mode(self, mode):
        self.GPIO.setmode(mode)

    def setup_gpio_pin(self, pin, direction, pull_up_down):
        self.GPIO.setup(pin, direction, pull_up_down)
