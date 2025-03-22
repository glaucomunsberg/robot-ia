import asyncio
from common.machine_time import MachineTime


class Steam:
    """Responsible for the basic functions of the robot, such as reading sensors, 
    controlling actuators, and managing the battery. The reptilian brain is 
    responsible for the robot's survival and basic functions.
    """

    _instance = None
    code = None
    task = None
    loop = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.code = MachineTime().current_code()

        return cls._instance

    async def periodic(self):
        """function that will run periodically"""
        total = 5
        while total > 0:
            total -= 1
            print('periodic')
            Steam()
            await asyncio.sleep(1)

    async def start(self):
        """function that will start the periodic function
        and stop it after 5 seconds
        """
        self.loop = asyncio.get_event_loop()
        self.task = self.loop.create_task(self.periodic())
        try:
            self.loop.run_until_complete(self.task)
        except asyncio.CancelledError:
            pass

    def stop(self):
        """function that will stop the periodic function
        after 5 seconds
        """
        self.task.cancel()
