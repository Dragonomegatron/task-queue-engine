import json

from task import Task, PENDING, RUNNING


class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.tasks = []
        self.file_name = file_name

        self.load_tasks()

    def add_task(self, task):
        print(f"Added task: {task.name}")

        self.tasks.append(task)
        self.save_tasks()

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

    def save_tasks(self):
        with open(self.file_name, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)

                self.tasks = [Task.from_dict(task_data) for task_data in data]

                print("Loaded existing tasks")

        except FileNotFoundError:
            self.tasks = []