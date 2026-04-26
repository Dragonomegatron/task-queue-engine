from Task import RUNNING, PENDING, COMPLETED, FAILED

class TaskExecutor:
    def execute_task(self, task):
        try:
            print(f"Executing: {task.name}")
            task.status = RUNNING

            result = task.func()
            task.result = result

            task.status = COMPLETED
            print(f"Completed: {task.name} -> {task.result}")

        except Exception as e:
            task.retries += 1
            print(f"Error in {task.name}:{e}")

            if task.retries <= task.max_retries :
                print(f"Retrying {task.name}({task.retries}/{task.max_retries})")
                task.status = PENDING
            else :
                task.status = FAILED
                task.result = str(e)
                print(f"Failed: {task.name}")

