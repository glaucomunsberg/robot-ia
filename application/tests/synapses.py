from time import sleep

from actuators.dc_motor import DCMotor
from actuators.buzzer import Buzzer
from actuators.led import Led
from sensors.ultrasonic import Ultrasonic
from sensors.temperature import Temperature


class TestSynapses:
    """Test the synapses of sensors
    """

    def __init__(self):
        self.led_sensor = Led()
        self.buzzer_sensor = Buzzer()
        self.ultrasonic_sensor = Ultrasonic()
        self.temperature_sensor = Temperature()
        self.motors = DCMotor()

    def test(self):
        """Test the synapses of sensors"""
        self.led_sensor.test()
        self.buzzer_sensor.test()
        self.ultrasonic_sensor.test()
        self.temperature_sensor.test()

    def test_motor(self):
        """Test the synapses of motors"""
        for set_weels in ['left', 'right']:
            self.motors.set_weels(set_weels)
            print(f"start test motor {self.motors.current_weels}...")
            self.motors.stop()
            self.motors.forward(100)
            sleep(3)
            self.motors.stop()
            self.motors.backwards(100)
            sleep(3)
            self.motors.stop()
            self.motors.backwards(100)
            sleep(3)
            self.motors.stop()
        print("end test motor...")

    def __str__(self):
        "pass"
