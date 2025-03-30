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
                            "action": "mensure",
                        },
                        "temperature": {
                            "action": "mensure",
                        }
                    }
                },
                {
                    "actuators": [
                        {
                            "weel": {
                                "action": "backward",
                                "weels": {
                                    "right": 100,
                                    "left": 100
                                },
                                "rules": [
                                    {
                                        "times": {
                                            "elapsed": {
                                                "time": 10,
                                                "unit": "second",
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
                                "weels": {
                                    "right": 0,
                                    "left": 0
                                },
                                "rules": [
                                    {
                                        "times": {
                                            "elapsed": {
                                                "time": 10,
                                                "unit": "second",
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

        print("Test go to forward stop if at 5cm...")
        test_list = [{
            "name": "go to forward",
            "description": "I want to start walking until I find a wall",
            "commands": [
                {
                    "sensors": {
                        "ultrasonic": {
                            "action": "mensure",
                        },
                        "temperature": {
                            "action": "mensure",
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
                                    "all": 100
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
                                    "all": 0
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
        # self.decoder.decode(test_list)
