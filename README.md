# Task Queue Engine

A lightweight Python task queue and job scheduler with automatic retry logic, task status tracking, and worker-based execution.

## Features

- **Task Queue Management**: Queue and execute tasks in order
- **Automatic Retries**: Built-in retry mechanism with configurable max retries
- **Status Tracking**: Real-time status updates (PENDING, RUNNING, COMPLETED, FAILED)
- **Worker Pattern**: Dedicated worker threads execute tasks from the queue
- **Error Handling**: Graceful error handling with detailed error messages
- **Unique Task IDs**: Each task is assigned a unique UUID for tracking

## Installation

Clone the repository:
```bash
git clone https://github.com/Dragonomegatron/task-queue-engine.git
cd task-queue-engine
```

No external dependencies required - uses Python standard library only.

## Quick Start

```python
from Task import Task
from TaskManager import TaskManager
from TaskExecutor import TaskExecutor
from Worker import Worker

# Create components
manager = TaskManager()
executor = TaskExecutor()
worker = Worker(manager, executor)

# Define your tasks
def hello():
    print("Hello")

def calculate():
    return 2 + 3

# Add tasks to queue
manager.add_task(Task("Say Hello", hello))
manager.add_task(Task("Calculate", calculate))

# Execute all tasks
worker.start()

# Check final status
for task in manager.tasks:
    print(task)
```

## Task Status States

- **PENDING**: Task is waiting to be executed
- **RUNNING**: Task is currently executing
- **COMPLETED**: Task executed successfully
- **FAILED**: Task failed after all retries exhausted

## Configuration

Create a task with custom max retries:

```python
task = Task("My Task", my_function, max_retries=5)
```

Default max retries is 3.

## Project Structure

```
├── Task.py              # Task class definition and status constants
├── TaskManager.py       # Manages task queue
├── TaskExecutor.py      # Executes individual tasks with retry logic
├── Worker.py            # Worker that pulls and executes tasks
├── main.py              # Example usage
└── README.md            # This file
```

## Example Output

```
Executing: Say Hello
Hello
Completed: Say Hello -> None
Executing: Calculate
Completed: Calculate -> 5

Final Task States
[uuid-1]Say Hello | Status: completed | Retries: 0
[uuid-2]Calculate | Status: completed | Retries: 0
```

## Requirements

- Python 3.6+

## License

MIT License - feel free to use in your projects
