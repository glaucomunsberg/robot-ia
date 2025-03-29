from brain.neocortex.parietal.cognition.command_decoder import CommandDecoder


class CommandDecoderTest:
    """Test class for CommandDecoder."""

    def __init__(self):
        self.decoder = CommandDecoder()

    def test(self):
        """Test method."""
        print("Test empty list...")
        test_list = []
        self.decoder.decode(test_list)
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
        self.decoder.decode(test_list)
