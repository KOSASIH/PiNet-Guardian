import configparser

class ConfigParser:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_section(self, section):
        return self.config[section]

    def get_option(self, section, option):
        return self.config.get(section, option)
