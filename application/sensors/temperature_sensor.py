from time import sleep
import dht  # pylint: disable=import-error
from machine import Pin  # pylint: disable=import-error
from common.synapses import Synapses
from brain.cortex import Cortex
from brain.limbic.temporal.hippocampus import Hippocampus


class TemperatureSensor:
    """ Class TemperatureSensor
        - measure: measure the temperature
        - test: test the temperature sensor
        - sensor: the temperature sensor
        - pin: the pin of the temperature sensor"""
    _instance = None
    last_measure = {
        "type": "temperature",
        "temperature": -1,
        "temperature_f": -1,
        "humidity": -1
    }

    def __new__(cls, *args, **kwargs):  # pylint: disable=unused-argument
        """
        trigger_pin: Output pin to send pulses
        echo_pin: Readonly pin to measure the distance. The pin should be protected with 1k resistor
        echo_timeout_us: Timeout in microseconds to listen to echo pin. 
        By default is based in sensor limit range (4m)
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls.synapses = Synapses()
            cls.cortex = Cortex()
            cls.hippocampus = Hippocampus()
            cls.pin = cls.synapses.temperature_pin
            cls.sensor = dht.DHT11(Pin(cls.pin))
        return cls._instance

    def measure(self, tries=3):
        """Measure the temperature"""
        temp = 0
        temp_f = 0
        hum = 0
        for _ in range(tries):
            try:
                sleep(1)
                self.sensor.measure()
                temp = self.sensor.temperature()
                hum = self.sensor.humidity()
                temp_f = temp * (9/5) + 32.0
                self.set_last_measure(temp, temp_f, hum)
                return temp, temp_f, hum
            except OSError as e:
                print('Failed to read sensor.')
                print(f"{e}")
        return temp, temp_f, hum

    def set_last_measure(self, temp, temp_f, hum):
        """Set the last measure"""
        self.last_measure["temperature"] = temp
        self.last_measure["temperature_f"] = temp_f
        self.last_measure["humidity"] = hum
        self.cortex.add_task(func=self.hippocampus.store_memory,
                             task_type="SENSOR",
                             priority=3,
                             args=self.last_measure)

    def test(self):
        """Test the temperature sensor"""

        print("Temperature Sensor Test started")
        temp, temp_f, hum = self.measure()
        print(f"Temperature: {temp} C")
        print(f"Temperature: {temp_f} F")
        print(f"Humidity: {hum} %")
        print("Temperature Sensor Test completed")

# Compare this snippet from application/main.py:
