from machine import Pin
from common.synapses import Synapses


class LedSensor:
    """Initialize the LED sensor
    """

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
            self.on()
            if self.is_on() == 1:
                print("LED Testing on...")
            else:
                print("LED Error: test LED on")
            self.off()
            if self.is_on() == 0:
                print("LED Testing off...")
            else:
                print("LED Error: test LED off")
        print("LED Test completed")
