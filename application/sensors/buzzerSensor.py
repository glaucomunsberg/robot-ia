from machine import Pin, PWM
from common.singleton import SingletonMeta
from common.synapses import Synapses
import time

# Buzzer class
#   This class is used to control the buzzer of the device
#   The buzzer can play a melody and the melody can be customized


class BuzzerSensor:

    # Initialize the buzzer
    #   - BUZZER_PIN: the pin number of the buzzer
    #   - BUZZER_FREQUENCY: the frequency of the buzzer
    #   - BUZZER_DUTY: the duty cycle of the buzzer
    #   - tones: the tones of the buzzer
    def __init__(self):
        self.synapses = Synapses()
        self.pin = self.synapses.BUZZER_PIN
        self.buzzer = PWM(Pin(self.pin, Pin.OUT),
                          freq=self.synapses.BUZZER_FREQUENCY,
                          duty=self.synapses.BUZZER_DUTY
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

    # Play the melody
    #   - melody: the melody to play
    #   - rhythm: the rhythm of the melody
    #   - interval_time: the interval time
    def play(self, melody: str, rhythm: list, interval_time: int):
        for tone, length in zip(melody, rhythm):
            self.buzzer.freq(self.tones[tone])
            time.sleep(interval_time/length)
        self.buzzer.deinit()

    # Play the melody of the buzzer test
    def test(self):
        melody = 'cdefgabC'
        rhythm = [8, 8, 8, 8, 8, 8, 8, 8]
        interval_time = 5
        self.play(melody, rhythm, interval_time)
        print("Buzzer Test completed")
