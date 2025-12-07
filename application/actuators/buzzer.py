import time

from common.synapses import Synapses
from machine import PWM, Pin  # pylint: disable=import-error


class Buzzer:
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
            cls._instance = super().__new__(cls)
            cls.synapses = Synapses()
            cls.pin = cls.synapses.buzzer_pin
            cls.buzzer = PWM(Pin(cls.pin, Pin.OUT),
                             freq=cls.synapses.buzzer_frenquency,
                             duty=0  # Inicia silencioso
                             )
            cls.tones = {
                'c': 262,
                'd': 294,
                'e': 330,
                'f': 349,
                'fs': 370,  # F# (Fá sustenido)
                'g': 392,
                'a': 440,
                'b': 494,
                'C': 523,
                'D': 587,
                'E': 659,
                'F': 698,
                'Fs': 740,  # F# oitava superior
                'G': 784,
                'A': 880,
                'B': 988,
                # Removido ' ': 0 para evitar erro de frequência
            }

        return cls._instance

    def play(self, melody: str, rhythm: list, interval_time: int, duty=None):
        """_summary_Play the melody

        Args:
            melody (str): notes of the melody
            rhythm (list): rhythm of the melody
            interval_time (int): interval time
        """
        if duty is not None:
            self.buzzer.duty(duty)
        else:
            self.buzzer.duty(self.synapses.buzzer_duty)
        for tone, length in zip(melody, rhythm):
            if tone in self.tones:
                self.buzzer.freq(self.tones[tone])
            else:
                # Para caracteres não reconhecidos (como ' '), silencia
                self.buzzer.duty(0)
            time.sleep(interval_time/length)
        # Alterado de deinit() para duty(0) para manter PWM ativo
        self.buzzer.duty(0)

    def test(self):
        """Test the buzzer"""
        print("Buzzer Test started")
        melody = 'cdefgabC'
        rhythm = [8, 8, 8, 8, 8, 8, 8, 8]
        interval_time = 5
        self.play(melody, rhythm, interval_time)
        print("Buzzer Test completed")

    def play_advanced(self, notes_data: list):
        """Play melody with advanced control over duty cycle and timing

        Args:
            notes_data (list): List of tuples (note, duration, duty_cycle)
        """
        for note_info in notes_data:
            if len(note_info) == 3:
                note, duration, duty = note_info
            else:
                note, duration = note_info
                duty = self.synapses.buzzer_duty

            if note in self.tones and self.tones[note] > 0:
                # Nota válida com frequência > 0
                self.buzzer.freq(self.tones[note])
                self.buzzer.duty(duty)
                time.sleep(duration)
            else:
                # Pausa/silêncio - apenas ajusta duty para 0, mantém freq anterior
                self.buzzer.duty(0)
                time.sleep(duration)

        self.buzzer.duty(0)  # Silenciar ao final    def test_nokia_tune(self):
        """Test the buzzer with Nokia Tune melody with improved sound quality"""
        print("Nokia Tune Test started")

        # Nokia Tune original: E-D-F#-G-C-B-D-C
        # Com duty cycles variados para melhorar o som
        nokia_notes = [
            ('E', 0.25, 300),   # E nota inicial - duty mais baixo para suavidade
            (' ', 0.05, 0),     # Pequena pausa
            ('D', 0.25, 300),   # D
            (' ', 0.05, 0),     # Pequena pausa
            ('fs', 0.5, 400),   # F# - duty médio, nota mais longa
            (' ', 0.1, 0),      # Pausa
            ('G', 0.5, 400),    # G - duty médio, nota mais longa
            (' ', 0.2, 0),      # Pausa entre frases
            ('C', 0.25, 350),   # C - duty ligeiramente maior
            (' ', 0.05, 0),     # Pequena pausa
            ('B', 0.25, 350),   # B
            (' ', 0.05, 0),     # Pequena pausa
            ('D', 0.5, 450),    # D - duty alto, nota mais longa
            (' ', 0.1, 0),      # Pausa
            ('C', 0.5, 450),    # C final - duty alto, nota mais longa
        ]
        print("Nokia Tune Test completed")

    def test_nokia_tune_classic(self):
        """Test the buzzer with classic Nokia Tune (original version)"""
        print("Classic Nokia Tune Test started")

        # Versão mais fiel ao original com duty cycle otimizado
        classic_notes = [
            ('E', 0.2, 256),    # E - duty equilibrado
            ('D', 0.2, 256),    # D
            ('fs', 0.4, 384),   # F# - mais longo, duty mais alto
            ('G', 0.4, 384),    # G - mais longo, duty mais alto
            (' ', 0.15, 0),     # Pausa entre frases
            ('C', 0.2, 256),    # C
            ('B', 0.2, 256),    # B
            ('D', 0.4, 384),    # D - mais longo, duty mais alto
            ('C', 0.4, 384),    # C final - mais longo, duty mais alto
        ]

        self.play_advanced(classic_notes)
        print("Classic Nokia Tune Test completed")

    def test_duty_variations(self):
        """Test different duty cycle values to demonstrate sound quality differences"""
        print("Duty Cycle Variations Test started")

        # Tocar a mesma nota com diferentes duty cycles
        test_note = 'a'  # Lá 440Hz
        # Diferentes valores de duty
        duties = [128, 256, 384, 512, 640, 768, 896]

        print("Playing note 'A' with different duty cycles:")
        for duty in duties:
            print(f"  Duty {duty}/1024 ({duty/1024*100:.1f}%)")
            self.buzzer.freq(self.tones[test_note])
            self.buzzer.duty(duty)
            time.sleep(0.8)
            self.buzzer.duty(0)  # Pausa entre as notas
            time.sleep(0.2)

        print("Duty Cycle Variations Test completed")
        print("Observe como diferentes duty cycles afetam o volume e timbre do buzzer")
