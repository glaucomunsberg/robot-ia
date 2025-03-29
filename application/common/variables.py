import json
from common.machine_time import MachineTime


class Variables:
    """
    The class Synapses is used to store the pins of the devices. 
    The pins are used to control the devices
    """
    _instance = None
    code = None
    file: dict = dict()
    configs: dict = dict()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.code = MachineTime().current_code()

        return cls._instance

    def __init__(self):
        self.file = self.read_config()
        self.configs = self.file['configs']

    def read_config(self):
        """read the configuration file from ../config.json and transform it into a dictionary"""
        with open('../../robot-ia.json', encoding="utf-8") as f:
            return json.load(f)
