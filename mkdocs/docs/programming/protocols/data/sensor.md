
## Sensors Data

The robot sends the sensors data to the controller in a json format and this data can be used to monitor the robot's environment and status.

### Format

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

### ultrasonic
```json
{
    "sensors": {
        "ultrasonic": {
            "distance": 10,
            "unit": "cm",
            "created_at": "2021-01-01T00:00:00"
        }
    }
}
```

### temperature
```json
{
    "sensors": {
        "temperature": {
            "temperature": 25,
            "temperature_unit": "celsius",
            "humidity": 50,
            "created_at": "2021-01-01T00:00:00"
        }
    }
}
```

### led
```json
{
    "sensors": {
        "led": {
            "color": "red",
            "intensity": 100,
            "created_at": "2021-01-01T00:00:00"
        }
    }
}
```

### buzzer
```json
{
    "sensors": {
        "buzzer": {
            "frequency": 1000,
            "duration": 1000,
            "created_at": "2021-01-01T00:00:00"
        }
    }
}