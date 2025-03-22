from common.synapses import Synapses
from machine import Pin  # pylint: disable=import-error

# Created by https://RandomNerdTutorials.com/micropython-esp32-esp8266-dc-motor-l298n/
# This file includes a class to control DC motors


class DCMotor:
    """the min_duty and max_duty are defined for 15000Hz frequency you can pass as arguments"""
    min_duty = 100
    max_duty = 1023
    synapses = Synapses()
    frequency = 15000
    motor_name = ""

    def __init__(self, motor_number: int = 0):
        self.motor_name = "Motor {motor_number}"
        if motor_number == 1:
            self.pin1 = Pin(self.synapses.motor_1_pin_1, Pin.OUT)
            self.pin2 = Pin(self.synapses.motor_1_pin_2, Pin.OUT)
        elif motor_number == 2:
            self.pin1 = Pin(self.synapses.motor_2_pin_1, Pin.OUT)
            self.pin2 = Pin(self.synapses.motor_2_pin_2, Pin.OUT)
        else:
            raise ValueError("motor_number must be 1 or 2")
        self.speed = 0

    def forward(self, speed):
        """speed value can be between 0 and 100"""
        self.speed = speed
        # self.enable_pin.duty(self.duty_cycle(speed))
        self.pin1.value(self.duty_cycle(speed))
        self.pin2.value(0)

    def backwards(self, speed):
        """speed value can be between 0 and 100"""
        self.speed = speed
        # self.enable_pin.duty(self.duty_cycle(speed))
        self.pin1.value(0)
        self.pin2.value(self.duty_cycle(speed))

    def stop(self):
        """stops the motor"""
        # self.enable_pin.duty(0)
        self.pin1.value(0)
        self.pin2.value(0)

    def duty_cycle(self, speed):
        """calculates the duty cycle value for the PWM signal"""
        if speed <= 0:
            duty_cycle = self.min_duty
        elif speed >= 100:
            duty_cycle = self.max_duty
        else:
            # duty_cycle = int(self.min_duty + (self.max_duty -
            #                 self.min_duty)*((speed - 1)/(100-1)))
            duty_cycle = int(self.min_duty + (self.max_duty -
                             self.min_duty) * ((speed - 1) / 99))
        print(f"duty cile: {duty_cycle}")
        return duty_cycle

    def set_max_duty(self, max_duty):
        """sets the max duty cycle value"""
        self.max_duty = max_duty

    def set_min_duty(self, min_duty):
        """sets the min duty cycle value"""
        self.min_duty = min_duty
