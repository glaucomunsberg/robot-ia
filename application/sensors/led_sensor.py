import time
from machine import Pin  # pylint: disable=import-error
from common.synapses import Synapses


class LedSensor:
    """Initialize the LED sensor
    """

    _instance = None

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
            cls.pin = cls.synapses.led_pin
            cls.led = Pin(cls.pin, Pin.OUT)

        return cls._instance

    def __init__(self):
        self.synapses = Synapses()
        self.pin = self.synapses.led_pin
        self.led = Pin(self.pin, Pin.OUT)

    def read(self):
        """Read the LED value"""
        return self.led.value()

    def on(self):
        """Turn the LED on"""
        self.led.on()

    def off(self):
        """Check if the LED is on"""
        self.led.off()

    def is_on(self):
        """Check if the LED is on

        Returns:
            integer: 1 if the LED is on, 0 otherwise
        """
        return self.read() == 1

    # Check if the LED is on and off
    #  - times: the number of times to check
    def test(self, times: int = 3):
        """# Check if the LED is on and off

        Args:
            times (int, optional): repeated time. Defaults to 3.
        """
        print("LED Test started")
        for i in range(times):
            print(f"LED Test {i+1}")
            time.sleep(0.5)
            self.on()
            if self.is_on() != 1:
                print("LED Error: test LED on")
            time.sleep(0.5)
            self.off()
            if self.is_on() != 0:
                print("LED Error: test LED off")
        print("LED Test completed")
