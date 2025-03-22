# pylint: disable=import-error
import utime
from machine import RTC  # or import from machine depending on your micropython version
rtc = RTC()
rtc.datetime((2019, 5, 1, 4, 13, 0, 0, 0))


class Cortex:
    """Classe que gerencia as tarefas do sistema."""

    _instance = None
    tasks = []
    counter = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.tasks = []
            cls.counter = 0
        return cls._instance

    def generate_hash(self) -> str:
        """Gera um hash único baseado na data e hora."""
        timestamp = str(utime.ticks_ms())
        print(f"time: {timestamp.encode('utf-8')}")
        timestamp = timestamp.encode('utf-8')
        return timestamp[:8]

    def add_task(self, *args, func, task_type, priority=3, **kwargs) -> None:
        """Adiciona uma nova tarefa à fila de execução com prioridade (0 a 5), hash e tipo."""
        if not (0 <= priority <= 5):
            raise ValueError("A prioridade deve estar entre 0 e 5.")
        if task_type not in {"SENSOR", "BRAIN", "ACTION", "PROCESS"}:
            raise ValueError(
                "O tipo de tarefa deve ser SENSOR, BRAIN, ACTION ou PROCESS.")

        task_hash = self.generate_hash()
        self.tasks.append((priority, self.counter, task_hash,
                          task_type, func, args, kwargs))
        self.counter += 1
        # Ordena por prioridade e ordem de chegada
        self.tasks.sort(key=lambda x: (x[0], x[1]))

    def run(self) -> None:
        """Executa de forma síncrona, respeitando a prioridade e FIFO dentro da prioridade."""
        if len(self.tasks) == 0:
            print("Nenhuma tarefa para executar.")
        else:
            _, _, task_hash, task_type, func, args, kwargs = self.tasks.pop(0)
            print(f"Executando tarefa {task_hash} do tipo {task_type}...")
            try:
                print(f" result:{func(*args, **kwargs)}")
            except Exception as e:
                print(f"Erro na tarefa {task_hash}: {e}")


# Exemplo de uso
# task_processor = Cortex()


# def task1():
#     for i in range(5):
#         print(f"Tarefa 1 - Iteração {i}")
#         utime.sleep(1)


# def task2():
#     for i in range(3):
#         print(f"Tarefa 2 - Iteração {i}")
#         utime.sleep(2)


# def task3():
#     print("Tarefa 3 - Alta prioridade executando!")


# def task4():
#     print("Tarefa 4 - Alta prioridade executando!")


# task_processor.add_task(func=task1, task_type="PROCESS", priority=4)
# task_processor.add_task(func=task2, task_type="SENSOR", priority=2)
# task_processor.add_task(func=task3, task_type="BRAIN", priority=0)
# task_processor.add_task(func=task4, task_type="ACTION", priority=0)
