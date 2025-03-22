# Communication Protocol

## Introduction

We use the concept of [`ideia`](idea.md) to represent the data that the robot sends to the controller, the concept of [`command`](command.md) to represent the commands that the controller sends to the robot with conecept of [`rules`](rule.md) to represent condictions to run commands or abort a idea in executation. In some cases, the robot can send the [data](sensor.md) from sensors to the controller to be stored in a database.


### Workflow

Each **idea** is running in the robot through the [`cortex`](../brain/cortex.md) and the robot sends the data to the controller. The controller sends the commands to the robot to execute the idea. 

```mermaid
---
config:
  layout: fixed
---
flowchart TB
    CORTEX["Cortext"] --> IDEAS[["Ideias"]]
    IDEAS -- next idea to be run --> IDEA["walk forward"]
    IDEA --> CMD1["command 1"] & CMD2["command 2"]
    CMD2 --> C_RULES2{"rules"}
    C_RULES2 --> CR1_2["condiction 1"]
```


### Format

We use a [json syntax](https://www.json.org/json-en.html){ target='\_blank' } protocol to communicate between the robot and the controller. The robot sends the data to the controller and the controller sends the commands to the robot. Below is a general format of the data that the robot sends to the controller.

```json
{
  "ideia": {
    "name": "",
    "description": "",
    "commands": [
        {
            "command_1": [
                {
                    "component_name": {
                        "rules": [ ]
                    }
                }
            ]
        }
    ]
  }
}
```

You can find more information about the syntax in the [ideia](idea.md), [command](command.md) and [rule](rule.md) pages.


## Exemple

"I want move until find a wall" is an `ideia` and that idea can be translated to a list with `command` and `rules` to the robot go to foward. Lets construct the idea, commands and rules to the robot go ahead.

### Ideia

The idea is composed by directives that the robot must follow to reach the goal. We create a `name` and a `description` to the idea is a text field that describes the idea.

```json
{
  "ideia": {
    "name": "go to forward",
    "description": "I want to start walking until I find a wall",
    "commands": []
  }
}
```

### Commands

The commands are the actions that the robot must execute to reach the goal. The commands are composed by a list of command. To the robot go foward we need:

- Read the ultrasonic sensor
- Move the weel to the forward direction.
- Stop the weel

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

### Rules

Well, we need to create a rules to when the robot must forward or stop. At this case we create a rule to stop the robot when the ultrasonic sensor detect a wall at 5 cm and keep the robot moving until the ultrasonic sensor detect a wall at 5 cm.

```json
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
```
### Data

In some cases the robot can read the sensors and this data follow the [sensors syntax](sensor.md). Bellow you will find the complete json  with the data from current read ultrasonic sensor.

```json
{
  "sensors": {
    "ultrasonic": {
      "distance": 10,
      "unit": "cm"
    }
  }
}
```

## Result

The result of protocol is a json file that you will use to send in [API](../API/index.md) and the API send this command to the [Cortex](../brain/cortex.md) to be run.


### Format

Bellow you will find the complete json file with the idea, commands and rules to the robot go to forward.

```json
{
  "name": "go to forward",//(1)
  "description": "I want to start walking until I find a wall",
  "commands": [ //(2)
    {
        "sensors": { //(3)
            "ultrasonic": {
                "action": "read"
            }
        }
    },
    {
        "actuators": [ //(4)
            {
                "weel": {
                    "action": "forward",
                    "speed": 100,
                    "weels": {
                        "left": 100,
                        "right": 100
                    },
                    "rules": [ //(5)
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
                    "rules": [ //(6)
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
}
```

1. `ideia` is composed by a `name` and a `description` to the idea is a text field that describes the idea.

2. `commands` is composed by a list of command. To the robot go foward we need to read the ultrasonic sensor, move the weel to the forward direction and stop the weel.

3. A command to read the sensor ultrasonic.

4. A command to move the weel to the forward direction and stop the weel.

5. The rules to keep forward. This rule is compose by a condiction that is the ultrasonic sensor not detect a wall at 5 cm

6. The rules to stop the robot. This rule is composed when the ultrasonic sensor detect a wall at 5 cm.

### Workflow

The workflow of the idea running in the robot Cortex is represented in the flowchart below.

```mermaid
flowchart TB
    CORTEX[Cortext] --> IDEAS[["`Ideias`"]]
    IDEAS -- run idea **go to forward** --> IDEA[walk forward]
    IDEA --> CMD1[read ultrassonic]
    IDEA --> CMD2[forward the weels]
    IDEA --> CMD3[fa:fa-car stop weels]
    CMD2 --> C_RULES2{rules}
    C_RULES2 --> CR1_2[ultrassonic > 5 cm]
    CMD3 --> C_RULES3{rules}
    C_RULES3 --> CR1_3[ultrassonic < 5 cm]
```

---

This section show abstract concepts about the communication protocol, the next sections will show the robot communication protocol and the components used in the robot communication protocol.

<div class="grid cards" markdown>

-   :octicons-light-bulb-16:{ .lg .middle } __Idea__

    ----

    More about the *idea* and *goals* to be reached by the robot. Learn more about the syntax and the structure of the idea.

    [:octicons-arrow-right-24: Idea Section](idea.md)

-   :octicons-command-palette-16:{ .lg .middle } __Command__

    ----

    More about the *robot commands* and *actions* to reach the goal. Learn more about the `sensors` and `actuators` commands.

    [:octicons-arrow-right-24: Command Section](command.md)

-   :material-directions-fork:{ .lg .middle } __Rules__

    ----

    More about the *robot rules* and *conditions*  to each command. Learn more about the logical `condition` that run the command

    [:octicons-arrow-right-24: Rule Section](rule.md)
</div>
