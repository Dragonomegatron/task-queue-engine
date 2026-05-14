def hello():
    print("Hello World")


def add():
    return 2 + 3


def crash():
    return 1 / 0


def slow_task():
    import time
    time.sleep(5)
    return "Slow task completed"