import time

from common.synapses import Synapses
from machine import PWM, Pin  # pylint: disable=import-error


class BuzzerSensor:
    """This class is used to control the buzzer of the device.
    The buzzer can play a melody and the melody can be customized
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
            cls.synapses = Synapses()
            cls.pin = cls.synapses.buzzer_pin
            cls.buzzer = PWM(Pin(cls.pin, Pin.OUT),
                             freq=cls.synapses.buzzer_frenquency,
                             duty=cls.synapses.buzzer_duty
                             )
            cls.tones = {
                'c': 262,
                'd': 294,
                'e': 330,
                'f': 349,
                'g': 392,
                'a': 440,
                'b': 494,
                'C': 523,
                ' ': 0,
            }

        return cls._instance

    def play(self, melody: str, rhythm: list, interval_time: int):
        """_summary_Play the melody

        Args:
            melody (str): notes of the melody
            rhythm (list): rhythm of the melody
            interval_time (int): interval time
        """
        for tone, length in zip(melody, rhythm):
            self.buzzer.freq(self.tones[tone])
            time.sleep(interval_time/length)
        self.buzzer.deinit()

    def test(self):
        """Test the buzzer"""
        print("Buzzer Test started")
        melody = 'cdefgabC'
        rhythm = [8, 8, 8, 8, 8, 8, 8, 8]
        interval_time = 5
        self.play(melody, rhythm, interval_time)
        print("Buzzer Test completed")
