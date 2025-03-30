import time
from machine import Pin, time_pulse_us  # pylint: disable=import-error
from common.synapses import Synapses


class Ultrasonic:
    """
    Driver to use the untrasonic sensor HC-SR04.
    The sensor range is between 2cm and 4m.
    The timeouts received listening to echo pin are converted to OSError('Out of range')
    """
    _instance = None

    synapses = Synapses()
    # echo_timeout_us is based in chip range limit (400cm)
    last_measure = {
        "type": "ultrasonic",
        "distance": -1,
        "unit": "cm",
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
            cls.echo_timeout_us = cls.synapses.ultrasonic_echo_timeout_us
            # Init trigger pin (out)
            cls.trigger = Pin(
                cls.synapses.ultrasonic_trigger_pin, mode=Pin.OUT, pull=None)
            cls.trigger.value(0)

            # Init echo pin (in)
            cls.echo = Pin(cls.synapses.ultrasonic_echo_pin,
                           mode=Pin.IN, pull=None)
            cls._history = []
            cls._history_size = 5  # Número de medições para calcular a média
            # cls.hippocampus = Hippocampus()
            # cls.cortex = Cortex()
        return cls._instance

    def _send_pulse_and_wait(self):
        """
        Send the pulse to trigger and listen on echo pin.
        We use the method `machine.time_pulse_us()` to get the microseconds
        until the echo is received.
        """
        self.trigger.value(0)  # Stabilize the sensor
        time.sleep_us(5)  # pylint: disable= no-member
        self.trigger.value(1)
        # Send a 10us pulse.
        time.sleep_us(10)   # pylint: disable= no-member
        self.trigger.value(0)
        try:
            pulse_time = time_pulse_us(
                self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110:  # 110 = ETIMEDOUT
                raise OSError('Out of range') from ex
            raise ex

    def distance_mm(self):
        """
        Get the distance in milimeters without floating point operations.
        """
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.34320 mm/us that is 1mm each 2.91us
        # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582
        mm = pulse_time * 100 // 582
        return mm

    def distance_cm(self):
        """
        Get the distance in centimeters with floating point operations.
        It returns a float
        """
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.034320 cm/us that is 1cm each 29.1us
        cms = (pulse_time / 2) / 29.1
        return cms

    def measure(self, measure_type: str = "cm", tries: int = 2) -> int:
        """
        Read the sensor and send the distance to the server.
        Filters out values that deviate significantly from the recent history.
        """
        distance = -1
        while tries > 0 and distance < 0:
            try:
                if measure_type == "cm":
                    new_distance = self.distance_cm()
                elif measure_type == "mm":
                    new_distance = self.distance_mm()
                else:
                    raise ValueError("Invalid measure type")

                if len(self._history) >= self._history_size:
                    avg_distance = sum(self._history) / len(self._history)
                    to_compare = (
                        abs(new_distance - avg_distance) / avg_distance)
                    if to_compare > 0.2:  # 30% threshold
                        print(
                            f"Discarded: {new_distance} (avg: {avg_distance}) value {to_compare}")
                        tries -= 1
                        continue
                self.last_measure["distance"] = new_distance
                self.last_measure["unit"] = measure_type
                self._history.append(new_distance)
                if len(self._history) > self._history_size:
                    self._history = self._history[-self._history_size:]
                tries -= 1
                distance = new_distance
                # self.cortex.add_task(func=self.hippocampus.store_memory,
                #                      task_type="SENSOR",
                #                      priority=3,
                #                      kwargs={
                #                          "memory": self.last_measure
                #                      })
            except OSError as ex:
                print("Ultrasonic Error:", ex)
                tries -= 1
        return distance

    def test(self, times: int = 3) -> int:
        """
        Test the sensor. It sends 3 pulses and prints the distance.
        """
        print("Sensor test started")
        distance = 0
        for i in range(times):
            print(f"Test {i+1}")
            try:
                distance = self.distance_cm()
                print(f"Distance: {distance} cm")
            except OSError as ex:
                print("Ultrasonic Error:", ex)
        print("Sensor test completed")
        return distance
