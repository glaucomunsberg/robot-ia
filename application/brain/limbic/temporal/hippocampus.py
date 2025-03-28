from common.machine_time import MachineTime


class Hippocampus:
    """
    The Hippocampus is a part of the limbic system that is vital
    for the formation of new memories and the retrieval of old ones.
    """

    memory = []
    _instance = None
    time_machine = None

    def __new__(cls, *args, **kwargs):  # pylint: disable=unused-argument
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.time_machine = MachineTime()
            cls.memory = []
        return cls._instance

    def store_memory(self, memory: dict):
        """Add a memory in the hippocampus."""
        if not isinstance(memory, dict):
            raise ValueError("Memory must be a dictionary.")
        if "type" not in memory:
            raise ValueError("Memory must have a type.")
        if "timestamp" not in memory:
            memory["timestamp"] = self.time_machine.timestamp()
        self.memory.append(memory)

    def recall_memory(self):
        """Recall all the memories stored in the hippocampus."""
        return self.memory

    def recycle_memory(self, size: int = -1, kind: str = ""):
        """Recycle and keep the most recent memories."""
        if size > -1 and kind != "":
            self.memory = [
                memory for memory in self.memory if memory["type"] == kind][-size:]
        elif size > -1:
            self.memory = self.memory[-size:]
        elif kind != "":
            self.memory = [
                memory for memory in self.memory if memory["type"] == kind]

    def forget_memory(self):
        """Forget all the memories stored in the hippocampus."""
        self.memory = []
        return "All memories have been forgotten."
