import threading
import time
from tasks import cpu_heavy_task, io_bound_task  # Import functions from tasks.py

def run_tasks(task_func, num_tasks, task_type):
    threads = []
    start_time = time.time()

    # Create and start threads for each task
    for i in range(num_tasks):
        t = threading.Thread(target=task_func, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    end_time = time.time()
    print(f"\nTotal time for {task_type}: {end_time - start_time:.2f} seconds")

def main():
    num_tasks = 4

    print("=== Testing CPU-bound tasks (affected by GIL) ===")
    run_tasks(cpu_heavy_task, num_tasks, "CPU-bound")

    print("\n=== Testing I/O-bound tasks (not affected by GIL) ===")
    run_tasks(io_bound_task, num_tasks, "I/O-bound")

if __name__ == "__main__":
    main()