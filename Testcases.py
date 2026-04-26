from Task import Task
from TaskManager import TaskManager
from TaskExecutor import TaskExecutor
from Worker import Worker
import time

def Hello():
    print("Hello, World!")

def Add():
    return 2 + 3

def Breathe():
    print("Breathe in...")
    time.sleep(5)
    print("Breathe out...")
    time.sleep(5)
    
manager = TaskManager()
executor = TaskExecutor()
worker = Worker(manager, executor)

manager.add_task(Task("Hello Task", Hello))
manager.add_task(Task("Add task", Add))
manager.add_task(Task("Breathe Task", Breathe))

worker.start()
