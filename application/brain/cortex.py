# pylint: disable=import-error
import utime
from machine import RTC  # or import from machine depending on your micropython version
rtc = RTC()
rtc.datetime((2019, 5, 1, 4, 13, 0, 0, 0))


class Cortex:
    """
    Cortex is the brain task processor. It is responsible for managing the tasks
    and executing
    """

    _instance = None
    tasks = []
    counter = 0

    def __new__(cls, *args, **kwargs):  # pylint: disable=unused-argument
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.tasks = []
            cls.counter = 0
        return cls._instance

    def generate_hash(self) -> str:
        """Generate a hash based on the current timestamp."""
        timestamp = str(utime.ticks_ms())
        print(f"time: {timestamp.encode('utf-8')}")
        timestamp = timestamp.encode('utf-8')
        return timestamp[:8]

    def add_task(self, *args, func, task_type, priority=3, **kwargs) -> None:
        """Add a task to the task list. With priority, type and function to execute
        Args:
            func (function): The function to execute
            task_type (str): The type of the task
            priority (int, optional): The priority of the task. Defaults to 3.
        """
        if 0 <= priority or priority >= 6:
            raise ValueError(
                "The priority must be between 0 and 6 Evenly, Low, Normal, High, Critical")
        if task_type not in {"SENSOR", "BRAIN", "ACTION", "PROCESS"}:
            raise ValueError(
                f"type most be one of EVENTUALY, LOW, NORMAL, HIGH_PRIORITY, CRITICAL not {task_type}")

        task_hash = self.generate_hash()
        self.tasks.append((priority, self.counter, task_hash,
                          task_type, func, args, kwargs))
        self.counter += 1

    def run(self) -> None:
        """Execute the next task in the list"""
        if len(self.tasks) == 0:
            print("Any task to execute.")
        else:
            # Order by priority and counter
            self.tasks.sort(key=lambda x: (x[0], x[1]))
            _, _, task_hash, task_type, func, args, kwargs = self.tasks.pop(0)
            print(f"Executando tarefa {task_hash} do tipo {task_type}...")
            try:
                print(f" result:{func(*args, **kwargs)}")
            except Exception as e:  # pylint: disable=broad-except
                print(f"Erro na tarefa {task_hash}: {e}")
