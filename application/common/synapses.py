# pylint: disable=missing-module-docstring
# pylint: disable=too-many-instance-attributes
from common.machine_time import MachineTime


class Synapses:
    """
    The class Synapses is used to store the pins of the devices. 
    The pins are used to control the devices
    """
    _instance = None
    code = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.code = MachineTime().current_code()

        return cls._instance

    def __init__(self):

        # buzzer_pin
        self.buzzer_pin = 14  # [ignore]
        self.buzzer_frenquency = 440
        self.buzzer_duty = 512

        # led_pin
        self.led_pin = 15

        # ultrassonic_trigger_pin
        self.ultrassonic_trigger_pin = 16
        self.ultrassonic_echo_pin = 17
        self.ultrassonic_echo_timeout_us = 500*2*30

        # temperature_pin
        self.temperature_pin = 13

        # motor_pins
        self.motor_1_pin_1 = 48
        self.motor_1_pin_2 = 47
        self.motor_2_pin_1 = 45
        self.motor_2_pin_2 = 36

    def current_pins(self):
        """Get the current pins

        Returns:
            dict: the current pins
        """
        return {
            "buzzer_pin": self.buzzer_pin,
            "led_pin": self.led_pin,
            "ultrassonic_trigger_pin": self.ultrassonic_trigger_pin,
            "ultrassonic_echo_pin": self.ultrassonic_echo_pin,
            "ultrassonic_echo_timeout_us": self.ultrassonic_echo_timeout_us,
            "temperature_pin": self.temperature_pin
        }

    def __str__(self):
        return str(self.current_pins())
