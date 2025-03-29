# pylint: disable=import-error
from common.variables import Variables
from common.machine_time import MachineTime


class Cortex:
    """
    Cortex is the brain task processor. It is responsible for managing the tasks
    and executing
    """

    _instance = None
    tasks = []
    counter = 0
    variables = None
    machine_time = None

    def __new__(cls, *args, **kwargs):  # pylint: disable=unused-argument
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.variables = Variables()
            cls.machine_time = MachineTime()
            cls.tasks = []
            cls.counter = 0
        return cls._instance

    def generate_hash(self) -> str:
        """Generate a hash based on the current timestamp."""
        return f"{self.machine_time.generate_code()}-{(self.counter+1):04d}"  # pylint: disable=line-too-long

    def add_task(self, func, task_type, priority=3, args=None, kwargs=None) -> None:  # pylint: disable=too-many-arguments too-many-positional-arguments
        """Add a task to the task list. With priority, type and function to execute
        Args:
            func (function): The function to execute
            task_type (str): The type of the task
            priority (int, optional): The priority of the task. Defaults to 3.
        """
        if priority < 0 or priority > 6:
            raise ValueError(
                f"Priority must be 0 until 6 Evenly, Low, Normal, High, Critical not {priority}")
        if task_type not in {"SENSOR", "BRAIN", "ACTION", "PROCESS"}:
            raise ValueError(
                f"Type most be one of SENSOR, BRAIN, ACTION, PROCESS not {task_type}")

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
            print(f"Execução {task_hash} do tipo {task_type}...")
            try:
                if kwargs and args:
                    result = func(*args, **kwargs)
                elif kwargs:
                    result = func(**kwargs)
                elif args:
                    result = func(*args)
                else:
                    result = func()
                if self.variables.debug:
                    print(f" args:{args} and kwargs:{kwargs}")
                    print(f"Task {task_hash} result: {result}")

            except MemoryError:
                print(f"Cortex Memory Error: {task_hash}")
            except OSError as e:
                print(f"Cortex OS Error: {task_hash} -> {e}")
            except TypeError as e:
                print(f"Cortex Type Error: {task_hash} -> {e}")
            except RuntimeError as e:
                print(f"Cortex Runtime Error: {task_hash} -> {e}")
            except Exception as e:  # pylint: disable=broad-except
                print(f"Cortex Error: {task_hash} -> {e}")
