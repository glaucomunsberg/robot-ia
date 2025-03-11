# Communication Protocol

We use a json protocol to communicate between the robot and the controller. The robot sends the data to the controller and the controller sends the commands to the robot.
## Introduction


## Sensors Data

The robot sends the sensors data to the controller in a json format. The data is sent in a fixed time interval.

```json
{
    "sensors": {
        "ultrasonic": {
            "distance": 10,
            "unit": "cm"
        },
        "temperature": {
            "temperature": 25,
            "temperature_unit": "celsius",
            "humidity": 50
        },
        "led": {
            "color": "red",
            "intensity": 100
        },
        "buzzer": {
            "frequency": 1000,
            "duration": 1000
        }
    }
}
```
## Commands

The controller sends the commands to the robot in a json format. The commands are sent in a fixed time interval.

```json
{
    "commands": {
        "led": {
            "action": "read"
        },
        "buzzer": {
            "action": "read"
        },
        "ultrasonic": {
            "action": "read"
        },
        "temperature": {
            "action": "read"
        },
        "weel": {
            "action": "move",
            "direction": "forward",
            "speed": 100,
            "weels": {
                "left": 100,
                "right": 100
            },
            "duration": 1000
        }
    }
}
```