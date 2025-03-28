import time


class MachineTime:
    """
    Control the time of the machine, and return the current code based on the current time
    """
    _instance = None
    code = None

    def __new__(cls, *args, **kwargs):  # pylint: disable=unused-argument
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            current = time.localtime()
            cls.code = f"{current[0]}{current[1]}{current[2]}{current[3]}{current[4]}{current[5]}"

        return cls._instance

    def timestamp(self) -> str:
        """function that will return the current timestamp
        Returns:
            str: the current timestamp (year-month-day hour:minute:second)
        """
        current = time.localtime()
        return f"{current[0]}-{current[1]}-{current[2]} {current[3]}:{current[4]}:{current[5]}"

    def current_code(self) -> str:
        """function that will return the current code based on the current time
        Returns:
            str: the current code (year, month, day, hour, minute, second)
        """
        current = time.localtime()
        return f"{current[0]}{current[1]}{current[2]}{current[3]}{current[4]}{current[5]}"
