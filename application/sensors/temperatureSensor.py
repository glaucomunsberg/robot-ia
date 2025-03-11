from time import sleep

import dht
from common.synapses import Synapses
from machine import Pin


class TemperatureSensor:
    """ Class TemperatureSensor
        - measure: measure the temperature
        - test: test the temperature sensor
        - sensor: the temperature sensor
        - pin: the pin of the temperature sensor"""

    def __init__(self):
        self.synapses = Synapses()
        self.pin = self.synapses.temperature_pin
        self.sensor = dht.DHT11(Pin(self.pin))

    def measure(self, tries=3):
        """Measure the temperature"""
        temp = 0
        temp_f = 0
        hum = 0
        for i in range(tries):
            try:
                sleep(1)
                self.sensor.measure()
                temp = self.sensor.temperature()
                hum = self.sensor.humidity()
                temp_f = temp * (9/5) + 32.0
                return temp, temp_f, hum
            except OSError as e:
                print('Failed to read sensor.')
                print(f"{e}")
        return temp, temp_f, hum

    def test(self):
        """Test the temperature sensor"""

        print("Temperature Sensor Test started")
        temp, temp_f, hum = self.measure()
        print(f"Temperature: {temp} C")
        print(f"Temperature: {temp_f} F")
        print(f"Humidity: {hum} %")
        print("Temperature Sensor Test completed")

# Compare this snippet from application/main.py:
