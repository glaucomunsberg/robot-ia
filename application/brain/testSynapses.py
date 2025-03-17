from sensors.buzzerSensor import BuzzerSensor
from sensors.ledSensor import LedSensor
from sensors.ultrassonicSensor import UltrassonicSensor
from sensors.temperatureSensor import TemperatureSensor


class TestSynapses:
    """Test the synapses of sensors
    """

    def __init__(self):
        self.led_sensor = LedSensor()
        self.buzzer_sensor = BuzzerSensor()
        self.ultrassonic_sensor = UltrassonicSensor()
        self.temperature_sensor = TemperatureSensor()

    def test(self):
        """Test the synapses of sensors"""
        self.led_sensor.test()
        self.buzzer_sensor.test()
        self.ultrassonic_sensor.test()
        self.temperature_sensor.test()

    def __str__(self):
        pass
