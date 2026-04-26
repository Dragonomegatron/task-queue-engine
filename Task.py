import uuid

MAXRETRIES = "max_retries"
PENDING = "pending"
RUNNING = "running"
COMPLETED = "completed"
FAILED = "failed"

class Task:
    def __init__(self, name, func, max_retries=3):
        self.id = str(uuid.uuid4())
        self.name = name
        self.func = func

        self.status = PENDING
        self.result = None

        self.retries = 0
        self.max_retries = max_retries
        
    
    def __str__(self):
        return f"[{self.id}]{self.name} | Status: {self.status} | Retries: {self.retries}"
