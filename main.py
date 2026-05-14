from task import Task
from task_manager import TaskManager
from task_executor import TaskExecutor
from worker import Worker


if __name__ == "__main__":
    manager = TaskManager()
    executor = TaskExecutor()
    worker = Worker(manager, executor)

    # only create tasks if none exist
    if not manager.tasks:
        manager.add_task(Task("Hello Task", "hello"))
        manager.add_task(Task("Addition Task", "add"))
        manager.add_task(Task("Crash Task", "crash"))
        manager.add_task(Task("Slow Task", "slow_task"))

    worker.start()

    print("\nFinal Task States:")

    for task in manager.tasks:
        print(task)