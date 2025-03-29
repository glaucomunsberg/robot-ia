import json


class Variables:
    """
    The class Synapses is used to store the pins of the devices. 
    The pins are used to control the devices
    """
    _instance = None
    file: dict = dict()
    configs: dict = dict()
    version: str = "0.0.0"
    debug: bool = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        self.file = self.read_config()
        self.configs = self.file['configs']
        self.version = self.file['version']
        self.debug = self.file['debug']

    def read_config(self):
        """read the configuration file from ../config.json and transform it into a dictionary"""
        with open('../../robot-ia.json', encoding="utf-8") as f:
            return json.load(f)

    def get_value(self, chain: list):
        """Get the value of a chain of keys in the dictionary"""
        value = self.configs
        for key in chain:
            if key in value:
                value = value[key]
            else:
                return None
        return value
