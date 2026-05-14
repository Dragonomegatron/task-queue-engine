from task import RUNNING, COMPLETED, FAILED, PENDING
from task_registry import TASK_REGISTRY


class TaskExecutor:
    def execute(self, task):
        try:
            print(f"Executing: {task.name}")

            task.status = RUNNING

            func = TASK_REGISTRY.get(task.func_name)

            if not func:
                raise ValueError("Function not found")

            result = func()

            task.result = result
            task.status = COMPLETED

            print(f"Completed: {task.name} -> {task.result}")

        except Exception as e:
            task.retries += 1

            print(f"Error in {task.name}: {e}")

            if task.retries <= task.max_retries:
                print(f"Retrying {task.name} ({task.retries}/{task.max_retries})")
                task.status = PENDING

            else:
                task.status = FAILED
                task.result = str(e)

                print(f"Task failed permanently: {task.name}")