import time


class Worker:
    def __init__(self, manager, executor):
        self.manager = manager
        self.executor = executor

    def start(self):
        while True:
            task = self.manager.get_next_task()

            if task:
                self.executor.execute(task)

                # save after execution
                self.manager.save_tasks()

            else:
                if self.manager.all_done():
                    print("All tasks completed. Worker stopping.")
                    break

            time.sleep(1)