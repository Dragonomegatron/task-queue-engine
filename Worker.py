import time

class Worker:
    def __init__(self, manager, executor):
        self.manager = manager
        self.executor = executor

    def start(self):
        while True:
            task = self.manager.get_next_task()
            if task:
                self.executor.execute_task(task)
            else :
                if self.manager.all_done():
                    print("All tasks completed. Stopping worker.")
                    break
            time.sleep(1) 