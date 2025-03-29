import json
import time
from brain.reptilian.cerebellum.actions import read_ultrassonic_sensor
from brain.cortex import Cortex
from sensors.ultrassonic_sensor import UltrassonicSensor
from sensors.temperature_sensor import TemperatureSensor
from common.variables import Variables


class CommandDecoder:

    """Commands decodes in commands"""

    _instance = None
    cortex = None
    sensor_ultrassonic = None
    variables = None

    def __new__(cls, *args, **kwargs):  # pylint: disable=unused-argument
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.cortex = Cortex()
            cls.sensor_ultrassonic = UltrassonicSensor()
            cls.temperature_sensor = TemperatureSensor()
            cls.variables = Variables()
        return cls._instance

    def decode_from_text(self, text) -> None:
        """Set commands to decode."""
        if self.variables.debug:
            print(f"Type: {type(text)}")
        commands = {}
        try:
            json_string = json.dumps(text)
            commands = json.loads(json_string)
        except Exception as e:  # pylint: disable=broad-except
            print(f"Decoder Error: {e}")
         # transfrom json in dict
        self.decode([commands])

    def decode(self, commands: list) -> None:  # pylint: disable=too-many-branches too-many-statements
        """Set commands to decode."""
        ideia_count = 0
        for idea in commands:  # pylint: disable=too-many-nested-blocks
            if not isinstance(idea, dict):
                print(f"ideia {ideia_count} type {type(idea)} converting...")
                if self.variables.debug:
                    print(f"ideia: {idea}")
                idea = json.loads("{"+idea)
            if self.variables.debug:
                print(f"ideia: {idea}")
            time.sleep(1)
            # print(f"  name: {idea['name']}")
            ideia_count += 1
            if "commands" in idea:
                for command in idea["commands"]:
                    if self.variables.debug:
                        print("  command...")
                    if "sensors" in command:
                        for sensor in command["sensors"]:
                            if self.variables.debug:
                                print(f"    sensor: {sensor}")
                                print(
                                    f"      action: {command['sensors'][sensor]['action']}")
                                print(f"---> READ THE SENSOR 1 {sensor} <---")
                            if sensor == "ultrassonic":
                                self.cortex.add_task(func=self.sensor_ultrassonic.measure,
                                                     task_type="SENSOR")
                            if sensor == "temperature":
                                self.cortex.add_task(func=self.temperature_sensor.measure,
                                                     task_type="SENSOR")

                            # TODO: add action to sensor as shortcuts like that
                            if self.variables.debug:
                                print(f"---> READ THE SENSOR 2  {sensor} <---")
                            self.cortex.add_task(func=read_ultrassonic_sensor,
                                                 task_type="SENSOR")
            # pylint: disable=line-too-long
            # if "actuators" in command:
            #     for actuator in command["actuators"]:
            #         print(f"    actuator...")
            #         for actuator_type in actuator:
            #             print(f"      type: {actuator_type}")
            #             for action in actuator[actuator_type]:
            #                 print(f"        action: {action}")
            #                 print(
            #                     f"        speed: {actuator[actuator_type][action]['speed']}")
            #                 for weel in actuator[actuator_type][action]["weels"]:
            #                     print(f"        weel: {weel}")
            #                     print(
            #                         f"          speed: {actuator[actuator_type][action]['weels'][weel]}")
            #                     for rule in actuator[actuator_type][action]["rules"]:
            #                         print(f"          rule...")
            #                         for sensor in rule["sensors"]:
            #                             print(
            #                                 f"            sensor: {sensor}")
            #                             print(
            #                                 f"              distance: {rule['sensors'][sensor]['distance']}")
            #                             print(
            #                                 f"              unit: {rule['sensors'][sensor]['unit']}")
            #                             print(
            #                                 f"              condition: {rule['sensors'][sensor]['condition']}")
        print("End of commands...")
        print("")

    def test(self) -> None:
        """Test the decoder
        """
        print("Test decoder...")
