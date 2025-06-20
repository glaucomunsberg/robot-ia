---
title: Rule Protocol
description: The rule protocol used in the robot-ia project to define the rules that the robot must follow to execute the commands
tags:
  - programming
  - protocols
  - intention protocol
  - rule protocol
hide:
  - tags
---

Rules is the most important part of the intention protocol. It's the part that will define when the robot must do something or not from the sensors data.

## Example

At the exemplo below we have an example of a rule that the robot must stop when the ultrasonic sensor detect a wall at 5 cm.

```json
{
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
```
