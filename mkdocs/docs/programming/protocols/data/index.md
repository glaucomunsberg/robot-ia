---
title: Data Protocol
description: The data protocol used in the robot-ia project to exchange information between the robot cortex and the controller.
tags:
  - programming
  - protocols
  - data protocol
hide:
  - tags
---

The robot sends the sensors data to the controller in a json format and this data can be used to monitor the robot's environment, status, etc. The data is sent in a json format and the controller can use this data to monitor the robot's environment and status.

Current the data protocol is composed by [**sensor data**](sensor.md) and [**actuator data**](sensor.md).

```mermaid
flowchart LR
    subgraph server API
        A[Request]
    end
    subgraph Microprocessor
        B[Executation]
        C[Sensors]
        D[Actuators]
    end
    
    A <--> B
    B --> C
    B --> D
    C -- **DATA PROTOCOL** --> B
    D -- **DATA PROTOCOL** --> B

```

## Example

The robot sends the sensors data to the controller in a json format and this data can be used to monitor the robot's environment and status, below is an example of the data sent from ultrasonic sensor to the controller.

```json
{
    "sensors": {
        "ultrasonic": {
            "distance": 10,
            "unit": "cm",
            "status": "online",
            "created_at": "2021-01-01T00:00:00"
        }
    }
}
```

You can read more about the [sensors data](sensor.md) and [actuators data](sensor.md) in the specific page.
