import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger("PiNetGuardian")
        self.logger.setLevel(logging.INFO)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
