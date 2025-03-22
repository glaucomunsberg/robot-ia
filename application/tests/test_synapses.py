from time import sleep

from application.actuators.dc_motor import DCMotor
from application.sensors.buzzer_sensor import BuzzerSensor
from application.sensors.led_sensor import LedSensor
from application.sensors.ultrassonic_sensor import UltrassonicSensor
from application.sensors.temperature_sensor import TemperatureSensor


class TestSynapses:
    """Test the synapses of sensors
    """

    def __init__(self):
        self.led_sensor = LedSensor()
        self.buzzer_sensor = BuzzerSensor()
        self.ultrassonic_sensor = UltrassonicSensor()
        self.temperature_sensor = TemperatureSensor()
        self.motors = list()
        self.motors.append(DCMotor(1))
        self.motors.append(DCMotor(2))

    def test(self):
        """Test the synapses of sensors"""
        self.led_sensor.test()
        self.buzzer_sensor.test()
        self.ultrassonic_sensor.test()
        self.temperature_sensor.test()

    def test_motor(self):
        """Test the synapses of motors"""
        for motor in self.motors:
            print(f"start test motor {motor.motor_name}...")
            motor.stop()
            motor.forward(100)
            sleep(3)
            motor.stop()
            motor.backwards(100)
            sleep(3)
            motor.stop()
            motor.backwards(100)
            sleep(3)
            motor.stop()
        print("end test motor...")

    def __str__(self):
        pass
