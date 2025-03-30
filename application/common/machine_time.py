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
            cls.code = f"{current[0]:04d}{current[1]:02d}{current[2]:02d}{current[3]:02d}{current[4]:02d}{current[5]:02d}"  # pylint: disable=line-too-long

        return cls._instance

    def localtime(self) -> time.struct_time:
        """function that will return the current time
        Returns:
            time.struct_time: the current time
        """
        return time.localtime()

    def timestamp(self) -> str:
        """function that will return the current timestamp
        Returns:
            str: the current timestamp (year-month-day hour:minute:second)
        """
        current = time.localtime()
        return f"{current[0]:04d}-{current[1]:02d}-{current[2]:02d} {current[3]:02d}:{current[4]:02d}:{current[5]:02d}"  # pylint: disable=line-too-long

    def generate_code(self) -> str:
        """function that will return the current code based on the current time
        Returns:
            str: the current code (year, month, day, hour, minute, second)
        """
        current = time.localtime()
        return f"{current[0]:04d}{current[1]:02d}{current[2]:02d}{current[3]:02d}{current[4]:02d}{current[5]:02d}"  # pylint: disable=line-too-long

    def diff_time(self, start_at, end_at=None, mensure: str = 'second'):
        """ function that will return the difference between two times
        Args:
            start_at (time): the start time
            end_at (time): the end time
            mensure (str): the mensure of the time. It can be one of: second, minute, hour, day
        """
        if end_at is None:
            end_at = time.localtime()

        start = time.mktime(start_at)

        # calculate the difference between the two times
        diff = time.mktime(end_at) - start
        if mensure == 'second' or mensure == 'second':
            return diff
        elif mensure == 'minute':
            return diff / 60
        elif mensure == 'hour':
            return diff / 3600
        elif mensure == 'day':
            return diff / 86400
        else:
            raise ValueError(
                "mensure must be one of: second, minute, hour, day")
        # return the difference in seconds
