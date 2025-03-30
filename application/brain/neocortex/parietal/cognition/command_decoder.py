import json
import time
from brain.reptilian.cerebellum.actions import actuators_with_rules
from brain.cortex import Cortex
from common.machine_time import MachineTime
from common.variables import Variables
from sensors.ultrasonic import Ultrasonic
from sensors.temperature import Temperature


class CommandDecoder:
    """Commands decodes in commands"""

    _instance = None
    cortex = None
    sensor_list = ['ultrasonic', 'temperature']
    sensor_ultrasonic = None
    sensor_temperature = None
    ideas = []
    ideas_count = 0

    variables = None

    def __new__(cls, *args, **kwargs):  # pylint: disable=unused-argument
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.cortex = Cortex()
            cls.time_machine = MachineTime()
            cls.sensor_ultrasonic = Ultrasonic()
            cls.sensor_temperature = Temperature()
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
            self.ideas_count += 1
            if not isinstance(idea, dict):
                print(f"ideia {ideia_count} type {type(idea)} converting...")
                if self.variables.debug:
                    print(f"ideia: {idea}")
                idea = json.loads("{"+idea)
            if self.variables.debug:
                print(f"ideia: {idea}")
            time.sleep(1)
            if not 'code' in idea:
                idea['code'] = f'{self.time_machine.generate_code()}-{self.ideas_count}'
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
                            if sensor == "ultrasonic":
                                self.cortex.add_task(func=self.sensor_ultrasonic.measure,
                                                     task_type="SENSOR")
                            if sensor == "temperature":
                                self.cortex.add_task(func=self.sensor_temperature.measure,
                                                     task_type="SENSOR")

                            # if self.variables.debug:
                            #     print(f"---> READ THE SENSOR 2  {sensor} <---")
                            # self.cortex.add_task(func=read_ultrasonic_sensor,
                            #                      task_type="SENSOR")
                    if "actuators" in command:
                        self.cortex.add_task(func=actuators_with_rules,
                                             task_type="ACTUATOR",
                                             kwargs={
                                                 "actuators": command["actuators"]
                                             })
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
