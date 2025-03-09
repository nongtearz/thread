import time
import os

def cpu_heavy_task(task_id):
    """CPU-bound task affected by GIL"""
    print(f"Starting CPU-bound task {task_id}")
    result = 0
    # Adjusted computation to take approximately 1 second on a fast machine
    for i in range(10**7):  # 10^7 = 10 million iterations
        result += i ** 2  # Using square to target ~1 second
    print(f"CPU-bound task {task_id} completed. Result: {result:,}")
    return result

def io_bound_task(task_id):
    """I/O-bound task not affected by GIL, simulating file I/O"""
    print(f"Starting I/O-bound task {task_id}")
    filename = f"temp_file_{task_id}.txt"
    
    # Simulate I/O by writing a large amount of data to a file
    with open(filename, 'w') as f:
        for i in range(10000):  # Write 10,000 lines
            f.write(f"Line {i} of task {task_id}\n")
    
    # Simulate I/O by reading the file back
    with open(filename, 'r') as f:
        data = f.read()
    
    # Clean up the temporary file
    os.remove(filename)
    
    print(f"I/O-bound task {task_id} completed")
    return f"Processed file for task {task_id}"