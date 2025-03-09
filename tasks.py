def cpu_heavy_task(task_id):
    """งานหนักด้าน CPU เพื่อให้ชน GIL"""
    print(f"เริ่มงาน {task_id}")
    result = 0
    #heavy task
    for i in range(10**7):
        result += i ** 2
    print(f"งาน {task_id} เสร็จสิ้น ผลลัพธ์: {result:,}")
    return result