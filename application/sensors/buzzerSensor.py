import time

from common.synapses import Synapses
from machine import PWM, Pin


class BuzzerSensor:
    """This class is used to control the buzzer of the device.
    The buzzer can play a melody and the melody can be customized
    """

    def __init__(self):
        self.synapses = Synapses()
        self.pin = self.synapses.buzzer_pin
        self.buzzer = PWM(Pin(self.pin, Pin.OUT),
                          freq=self.synapses.buzzer_frenquency,
                          duty=self.synapses.buzzer_duty
                          )
        self.tones = {
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
