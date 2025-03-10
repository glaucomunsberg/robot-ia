from common.synapses import Synapses
from common.singleton import SingletonMeta
from machine import Pin


class LedSensor:

    # Initialize the LED
    #   - led: the LED
    def __init__(self):
        self.synapses = Synapses()
        self.pin = self.synapses.LED_PIN
        self.led = Pin(self.pin, Pin.OUT)

    # Read the LED value
    def read(self):
        return self.led.value()

    # Turn the LED on
    def on(self):
        self.led.on()

    # Turn the LED off
    def off(self):
        self.led.off()

    # Check if the LED is on
    def is_on(self):
        return self.read() == 1

    # Check if the LED is on and off
    #  - times: the number of times to check
    def test(self, times: int = 3):
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
