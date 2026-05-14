import uuid

PENDING = "pending"
RUNNING = "running"
COMPLETED = "completed"
FAILED = "failed"


class Task:
    def __init__(self, name, func_name, max_retries=2):
        self.id = str(uuid.uuid4())
        self.name = name
        self.func_name = func_name

        self.status = PENDING
        self.result = None

        self.retries = 0
        self.max_retries = max_retries

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "func_name": self.func_name,
            "status": self.status,
            "result": self.result,
            "retries": self.retries,
            "max_retries": self.max_retries
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["name"], data["func_name"], data["max_retries"])

        task.id = data["id"]
        task.status = data["status"]
        task.result = data["result"]
        task.retries = data["retries"]

        return task

    def __str__(self):
        return f"[{self.id}] {self.name} | {self.status} | retries={self.retries}"