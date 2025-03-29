
from sensors.ultrassonic_sensor import UltrassonicSensor


def read_ultrassonic_sensor():
    """
    Read the ultrasonic sensor and return the distance.
    """
    sensor = UltrassonicSensor()
    distance = sensor.measure()
    return distance
