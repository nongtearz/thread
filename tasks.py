import time

def cpu_heavy_task(task_id):
    """CPU-bound task affected by GIL"""
    print(f"Starting CPU-bound task {task_id}")
    result = 0
    # Adjusted computation to take approximately 1 second (machine-dependent)
    for i in range(5**6):  # 5^6 = 15625 iterations
        result += i ** 3  # Using cube to increase computation load
    print(f"CPU-bound task {task_id} completed. Result: {result:,}")
    return result

def io_bound_task(task_id):
    """I/O-bound task not affected by GIL"""
    print(f"Starting I/O-bound task {task_id}")
    # Simulate I/O operation with a 1-second delay
    time.sleep(1)  # Adjusted to 1 second to match CPU-bound task
    print(f"I/O-bound task {task_id} completed")
    return f"Result from I/O {task_id}"