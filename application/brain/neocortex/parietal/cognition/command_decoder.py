import json
from brain.cortex import Cortex
from sensors.ultrassonic_sensor import UltrassonicSensor
from brain.reptilian.cerebellum.actions import read_ultrassonic_sensor
import time


class CommandDecoder:

    """Commands decodes in commands"""

    _instance = None
    cortex = None
    sensor_ultrassonic = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.cortex = Cortex()
            cls.sensor_ultrassonic = UltrassonicSensor()
        return cls._instance

    def decode_from_text(self, text) -> None:
        """Set commands to decode."""
        print(f"Type: {type(text)}")
        commands = {}
        try:
            json_string = json.dumps(text)
            commands = json.loads(json_string)
            # transfrom json in dict
        except Exception as e:
            print(f"Error decoding JSON: {e}")

        self.decode([commands])

    def decode(self, commands: list) -> None:
        """Set commands to decode."""
        ideia_count = 0
        for idea in commands:
            if type(idea) is not dict:
                print(f"ideia {ideia_count} type {type(idea)} converting...")
                print(f"ideia: {idea}")
                idea = json.loads("{"+idea)
            print(f"ideia: {idea}")
            time.sleep(1)
            # print(f"  name: {idea['name']}")
            ideia_count += 1
            if "commands" in idea:
                for command in idea["commands"]:
                    print(f"  command...")
                    if "sensors" in command:
                        for sensor in command["sensors"]:
                            print(f"    sensor: {sensor}")
                            print(
                                f"      action: {command['sensors'][sensor]['action']}")
                            print(f"---> READ THE SENSOR 1 {sensor} <---")
                            self.cortex.add_task(func=self.sensor_ultrassonic.read,
                                                 task_type="SENSOR")
                            print(f"---> READ THE SENSOR 2  {sensor} <---")
                            self.cortex.add_task(func=read_ultrassonic_sensor,
                                                 task_type="SENSOR")

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
        """Test method."""
        print("Test empty list...")
        test_list = []
        self.decode(test_list)
        print("Test go to forward...")
        test_list = [{
            "name": "go to forward",
            "description": "I want to start walking until I find a wall",
            "commands": [
                {
                    "sensors": {
                        "ultrasonic": {
                            "action": "read"
                        }
                    }
                },
                {
                    "actuators": [
                        {
                            "weel": {
                                "action": "forward",
                                "speed": 100,
                                "weels": {
                                    "left": 100,
                                    "right": 100
                                },
                                "rules": [
                                    {
                                        "sensors": {
                                            "ultrasonic": {
                                                "distance": 5,
                                                "unit": "cm",
                                                "condition": "less_than"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "weel": {
                                "action": "stop",
                                "speed": 0,
                                "weels": {
                                    "left": 0,
                                    "right": 0
                                },
                                "rules": [
                                    {
                                        "sensors": {
                                            "ultrasonic": {
                                                "distance": 5,
                                                "unit": "cm",
                                                "condition": "greater_than"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }]
        self.decode(test_list)
