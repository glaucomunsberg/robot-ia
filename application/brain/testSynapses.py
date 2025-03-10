from common.singleton import SingletonMeta
from sensors.buzzerSensor import BuzzerSensor
from sensors.ledSensor import LedSensor
from sensors.ultrassonicSensor import ultrassonicSensor


class TestSynapses(metaclass=SingletonMeta):

    def __init__(self):
        self.ledSensor = LedSensor()
        self.buzzerSensor = BuzzerSensor()
        self.ultrassonicSensor = ultrassonicSensor()

    def test(self):
        self.ledSensor.test()
        self.buzzerSensor.test()
        self.ultrassonicSensor.test()
