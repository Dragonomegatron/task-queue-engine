from Task import PENDING, RUNNING


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_next_task(self):
        for task in self.tasks:
            if task.status == PENDING:
                return task
        return None
    
    def all_done(self):
        for task in self.tasks:
            if task.status in [PENDING, RUNNING]:
                return False
        return True
