from common.synapses import Synapses
from common.variables import Variables
from machine import Pin  # pylint: disable=import-error

# Created by https://RandomNerdTutorials.com/micropython-esp32-esp8266-dc-motor-l298n/
# This file includes a class to control DC motors


class DCMotor:
    """the min_duty and max_duty are defined for 15000Hz frequency you can pass as arguments"""
    min_duty = 100
    max_duty = 1023
    synapses = None
    frequency = 15000

    _instance = None
    variables = None
    weels_set_avaliable = ['left', 'right', 'front', 'back', 'left_front',
                           'left_back', 'right_front', 'right_back', 'all']
    current_weels = 'all'

    # {
    #     'left': [],
    #     'right': [],
    #     'front': [],
    #     'back': [],
    #     'left_front': [],
    #     'left_back': [],
    #     'right_front': [],
    #     'right_back': [],
    #     'all': [],
    # }
    def __new__(cls, *args, **kwargs):  # pylint: disable=unused-argument
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.synapses = Synapses()
            cls.variables = Variables()
            cls.left_front = Pin(cls.synapses.motor_1_pin_1, Pin.OUT)
            cls.left_back = Pin(cls.synapses.motor_1_pin_2, Pin.OUT)
            cls.right_front = Pin(cls.synapses.motor_2_pin_1, Pin.OUT)
            cls.right_back = Pin(cls.synapses.motor_2_pin_2, Pin.OUT)
        return cls._instance

    def __init__(self, weels_set: str = 'all'):
        if weels_set not in self.weels_set_avaliable:
            raise ValueError(
                f"set_weels must be one of {self.weels_set_avaliable}")
        self.set_weels(weels_set)
        # if motor_number == 1:
        #     self.pin1 = Pin(self.synapses.motor_1_pin_1, Pin.OUT)
        #     self.pin2 = Pin(self.synapses.motor_1_pin_2, Pin.OUT)
        # elif motor_number == 2:
        #     self.pin1 = Pin(self.synapses.motor_2_pin_1, Pin.OUT)
        #     self.pin2 = Pin(self.synapses.motor_2_pin_2, Pin.OUT)
        # else:
        #     raise ValueError("motor_number must be 1 or 2")
        self.speed = 0
        current_values = self.get_motors_values()
        if current_values['median'] > 0:
            self.stop()

    def set_weels(self, weels_set: list):
        """sets the weels to be used"""
        if weels_set not in self.weels_set_avaliable:
            raise ValueError(
                f"set_weels must be one of {self.weels_set_avaliable}")
        self.current_weels = weels_set

    def get_current_weels_pins(self):
        """returns the current weels set"""
        if self.current_weels == 'left':
            return [self.left_front, self.left_back]
        if self.current_weels == 'right':
            return [self.right_front, self.right_back]
        if self.current_weels == 'left_front':
            return [self.left_front]
        if self.current_weels == 'left_back':
            return [self.left_back]
        if self.current_weels == 'right_front':
            return [self.right_front]
        if self.current_weels == 'right_back':
            return [self.right_back]
        if self.current_weels == 'front':
            return [self.left_front, self.right_front]
        if self.current_weels == 'back':
            return [self.left_back, self.right_back]
        if self.current_weels == 'all':
            return [self.left_front, self.left_back,
                    self.right_front, self.right_back]
        raise ValueError(
            f"set_weels must be one of {self.weels_set_avaliable} not {self.current_weels}")

    def forward(self, speed):
        """speed value can be between 0 and 100"""
        self.speed = speed
        # self.enable_pin.duty(self.duty_cycle(speed))
        # self.pin1.value(self.duty_cycle(speed))
        # self.pin2.value(0)

        motors = self.get_current_weels_pins()
        motors[0].value(0)
        if len(motors) > 1:
            motors[1].value(self.duty_cycle(speed))
        if len(motors) > 2:
            motors[2].value(0)
        if len(motors) > 3:
            motors[3].value(self.duty_cycle(speed))

    def left(self, speed):
        """speed value can be between 0 and 100"""
        self.speed = speed
        # self.enable_pin.duty(self.duty_cycle(speed))
        # self.pin1.value(0)
        # self.pin2.value(self.duty_cycle(speed))
        motors = self.get_current_weels_pins()
        motors[0].value(0)
        if len(motors) > 1:
            motors[1].value(0)
        if len(motors) > 2:
            motors[2].value(0)
        if len(motors) > 3:
            motors[3].value(self.duty_cycle(speed))

    def right(self, speed):
        """speed value can be between 0 and 100"""
        self.speed = speed
        # self.enable_pin.duty(self.duty_cycle(speed))
        # self.pin1.value(0)
        # self.pin2.value(self.duty_cycle(speed))
        motors = self.get_current_weels_pins()
        motors[0].value(0)
        if len(motors) > 1:
            motors[1].value(self.duty_cycle(speed))
        if len(motors) > 2:
            motors[2].value(0)
        if len(motors) > 3:
            motors[3].value(0)

    def backwards(self, speed):
        """speed value can be between 0 and 100"""
        self.speed = speed
        # self.enable_pin.duty(self.duty_cycle(speed))
        # self.pin1.value(0)
        # self.pin2.value(self.duty_cycle(speed))
        motors = self.get_current_weels_pins()
        motors[0].value(self.duty_cycle(speed))
        if len(motors) > 1:
            motors[1].value(0)
        if len(motors) > 2:
            motors[2].value(self.duty_cycle(speed))
        if len(motors) > 3:
            motors[3].value(0)

    def stop(self):
        """stops the motor"""
        # self.enable_pin.duty(0)
        # self.pin1.value(0)
        # self.pin2.value(0)
        motors = self.get_current_weels_pins()
        motors[0].value(0)
        if len(motors) > 1:
            motors[1].value(0)
        if len(motors) > 2:
            motors[2].value(0)
        if len(motors) > 3:
            motors[3].value(0)

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
        if self.variables.debug:
            print(f"duty cile: {duty_cycle}")
        return duty_cycle

    def get_motors_values(self):
        """returns the current motors values"""
        values = {
            'left_front': self.left_front.value(),
            'left_back': self.left_back.value(),
            'right_front': self.right_front.value(),
            'right_back': self.right_back.value(),
        }
        values['median'] = (values['left_front'] + values['left_back'] +
                            values['right_front'] + values['right_back']) / 4
        return values

    def set_max_duty(self, max_duty):
        """sets the max duty cycle value"""
        self.max_duty = max_duty

    def set_min_duty(self, min_duty):
        """sets the min duty cycle value"""
        self.min_duty = min_duty
