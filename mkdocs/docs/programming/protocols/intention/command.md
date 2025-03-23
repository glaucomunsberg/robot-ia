## Command
The commands are the actions that the robot must execute to reach the goal. The protocol is composed by a list of command.

## Command Types

Currently the commands are composed by two types of commands:

### Sensors

The sensors are the commands that the robot must execute a `action` like `read`.

### Actuators

The actuators are the commands that the robot must execute a `action` like `forward` or `stop`. 


## Example

Below we have an example of a command that the robot read the sensor and move the weel to the forward direction.


```json
{
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
                    }
                }
            },
            {
                "weel": {
                    "action": "stop",
                    "speed": 0,
                    "weels": {
                        "left": 0,
                        "right": 0
                    }
                }
            }
        ]
    }
  ]
}
```