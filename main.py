
import time
from Task import Task
from TaskManager import TaskManager
from TaskExecutor import TaskExecutor
from Worker import Worker




def hello():
    print("Hello")

def add():
    return 2 + 3

def crash():
    return 1 / 0

if __name__ == "__main__":
    manager = TaskManager()
    executor = TaskExecutor()
    worker = Worker(manager, executor)

    manager.add_task(Task("Task 1", hello))
    manager.add_task(Task("Task 2", add))
    manager.add_task(Task("Task 3", crash))

    worker.start()

    print("\nFinal Task States")
    for task in manager.tasks:
        print(task)