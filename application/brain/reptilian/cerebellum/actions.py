
from sensors.ultrasonic import Ultrasonic
from sensors.temperature import Temperature
from actuators.dc_motor import DCMotor
from common.machine_time import MachineTime


def read_ultrasonic_sensor():
    """
    Read the ultrasonic sensor and return the distance.
    """
    sensor = Ultrasonic()
    distance = sensor.measure()
    return distance


def actuators_with_rules(actuators: dict) -> None:
    """
    Read the actuators and return the action.
    """
    print("actuators:")
    print(actuators)
    motors = DCMotor()
    temperature = Temperature()
    ultrasonic = Ultrasonic()
    machine_time = MachineTime()
    start_time = machine_time.localtime()
    if not actuators:
        print("actuators is empty!")
        return None
    condiction = True
    while condiction:  # pylint: disable=too-many-nested-blocks
        print('Start loop...')
        for actuator in actuators:
            print(f"\nactuator:\n   {actuator}")
            for actuator_type in actuator:
                # print(f"\nactuator type: {actuator_type}")
                for actuator_data in actuator[actuator_type]:
                    # print(f"\nactuator data: {actuator_data}")
                    if actuator_data == "rules":
                        print(
                            f"\nactuator data rules: {actuator[actuator_type][actuator_data]}")
                        for rule in actuator[actuator_type][actuator_data]:
                            print(f"\nrule: {rule}")
                            if 'times' in rule:
                                for time in rule['times']:
                                    print(f"\ntime: {time}")
                                    time_data = rule['times'][time]
                                    print(f"\ntime data: {time_data}")
                                    if time == "elapsed":
                                        elapsed_time = time_data['time']
                                        unit = time_data['unit']
                                        condition = time_data['condition']
                                        elapsed_time_now = machine_time.diff_time(
                                            start_time,
                                            mensure=unit)
                                        print(
                                            f"elapsed_time: {elapsed_time}")
                                        print(f"unit: {unit}")
                                        print(f"condition: {condition}")
                                        print(
                                            f'elapsed_time_now: {elapsed_time_now}')
                                        if unit == "s" or unit == "second":
                                            elapsed_time = elapsed_time
                                        elif unit == "ms" or unit == "millisecond":
                                            elapsed_time = elapsed_time / 1000
                                        elif unit == "us" or unit == "microsecond":
                                            elapsed_time = elapsed_time / 1000000
                                        else:
                                            print(f"Unknown unit: {unit}")
                                            motors.stop()
                                        if condition == "greater_than":
                                            if elapsed_time_now > elapsed_time:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"]
                                                )

                                        elif condition == "less_than":
                                            if elapsed_time_now < elapsed_time:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"]
                                                )

                            if 'sensors' in rule:
                                for sensor in rule["sensors"]:
                                    # print(f"\nsensor: {sensor}")
                                    if sensor == "ultrasonic":
                                        distance = ultrasonic.measure()
                                        condition = rule["sensors"][sensor]["condition"]
                                        distance_rule = rule["sensors"][sensor]["distance"]
                                        action = actuator[actuator_type]["action"]
                                        # unit = rule["sensors"][sensor]["unit"]
                                        print(f"distance: {distance}")
                                        print(f"action: {action}")
                                        print(f'rule: {distance_rule}')
                                        if condition == "less_than":
                                            if distance_rule < distance:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "greater_than":
                                            if distance_rule > distance:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "equal":
                                            if distance_rule == distance:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "not_equal":
                                            if distance_rule != distance:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "greater_than_or_equal":
                                            if distance_rule >= distance:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "less_than_or_equal":
                                            if distance_rule <= distance:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        else:
                                            print(
                                                f"Unknown condition: {condition}")
                                            motors.stop()

                                    if sensor == "temperature":
                                        temperature_value = temperature.measure()
                                        condition = rule["sensors"][sensor]["condition"]
                                        temperature_rule = rule["sensors"][sensor]["temperature"]
                                        print(
                                            f"temperature: {temperature_value}")
                                        print(f"action: {action}")
                                        print(f'rule: {temperature_rule}')
                                        if condition == "less_than":
                                            if temperature_rule < temperature_value:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "greater_than":
                                            if temperature_rule > temperature_value:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "equal":
                                            if temperature_rule == temperature_value:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "not_equal":
                                            if temperature_rule != temperature_value:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "greater_than_or_equal":
                                            if temperature_rule >= temperature_value:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        elif condition == "less_than_or_equal":
                                            if temperature_rule <= temperature_value:
                                                helper_actuator_motor(
                                                    motors,
                                                    actuator[actuator_type]["action"],
                                                    actuator[actuator_type]["weels"])
                                        else:
                                            print(
                                                f"Unknown condition: {condition}")
                                            motors.stop()
    # motors.stop()
    print("End loop...")
    return None


def helper_actuator_motor(motors: DCMotor, action, weels):
    """Helper function to control the motor action."""
    for weel in weels:
        motors.set_weels(weel)
        speed = weels[weel]
        if 'forward' == action:
            motors.forward(
                speed)
        elif 'backward' == action:
            motors.backwards(
                speed)
        elif 'left' in action:
            motors.left(
                speed)
        elif 'right' in action:
            motors.right(
                speed)
        elif 'stop' in action:
            motors.stop()
