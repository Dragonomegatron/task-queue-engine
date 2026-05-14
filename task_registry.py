from testcases import hello, add, crash, slow_task


TASK_REGISTRY = {
    "hello": hello,
    "add": add,
    "crash": crash,
    "slow_task": slow_task
}