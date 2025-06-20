---
title: Sensors Data
description: The sensors data is the information that the robot sends to the controller to monitor its environment and status.
tags:
  - programming
  - protocols
  - sensor protocol
  - data protocol
hide:
  - tags
---

The robot sends the sensors data to the controller in a json format and this data can be used to monitor the robot's environment and status.
The sensors data includes information about the ultrasonic sensor, temperature sensor, LED, and buzzer. Each sensor has its own set of attributes that provide detailed information about its readings and status.

## Format

### List of Sensors

- `sensors`: This is the main object that contains all the sensors data.
  - `ultrasonic`: This object contains the data from the ultrasonic sensor.
  - `temperature`: This object contains the data from the temperature sensor.
  - `led`: This object contains the data from the LED.
  - `buzzer`: This object contains the data from the buzzer.

```json
{
    "sensors": {
        "ultrasonic": {
        },
        "temperature": {
        },
        "led": {
        },
        "buzzer": {
        }
        // ...
    }
}
```

## Example

The following is an example of the sensors data that the robot sends to the controller. The data includes information about the ultrasonic sensor, temperature sensor, LED, and buzzer.

### Ultrasonic

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

- `ultrasonic`: This object contains the data from the ultrasonic sensor.
- `distance`: The distance measured by the ultrasonic sensor.
- `unit`: The unit of measurement for the distance (e.g., cm, m).
- `created_at`: The timestamp when the data was created.
- `status`: The status of the sensor (e.g., online, offline).

### Temperature

```json
{
    "sensors": {
        "temperature": {
            "temperature": 25,
            "temperature_unit": "celsius",
            "humidity": 50,
            "status": "online",
            "created_at": "2021-01-01T00:00:00"
        }
    }
}
```

- `temperature`: This object contains the data from the temperature sensor.
- `temperature`: The temperature measured by the sensor.
- `temperature_unit`: The unit of measurement for the temperature (e.g., celsius, fahrenheit).
- `humidity`: The humidity measured by the sensor.  
- `created_at`: The timestamp when the data was created.
- `status`: The status of the sensor (e.g., online, offline).

### Led

```json
{
    "sensors": {
        "led": {
            "color": "red",
            "intensity": 100,
            "status": "online",
            "created_at": "2021-01-01T00:00:00"
        }
    }
}
```

- `led`: This object contains the data from the LED.
- `color`: The color of the LED.
- `intensity`: The intensity of the LED (0-100).
- `created_at`: The timestamp when the data was created.
- `status`: The status of the LED (e.g., online, offline).

### Buzzer

```json
{
    "sensors": {
        "buzzer": {
            "frequency": 1000,
            "duration": 1000,
            "status": "online",
            "created_at": "2021-01-01T00:00:00"
        }
    }
}
```

- `buzzer`: This object contains the data from the buzzer.
- `frequency`: The frequency of the buzzer sound.
- `duration`: The duration of the buzzer sound.
- `created_at`: The timestamp when the data was created.
- `status`: The status of the buzzer (e.g., online, offline).

### Offline and without data

```json
{
    "sensors": {
        "ultrasonic": {
            "distance": null,
            "unit": null,
            "status": "offline",
            "created_at": "2021-01-01T00:00:00"
        },
        "temperature": {
            "temperature": null,
            "temperature_unit": null,
            "humidity": null,
            "status": "online",
            "created_at": "2021-01-01T00:00:00"
        },
    }
}
```
