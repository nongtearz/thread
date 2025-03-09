import threading
import time
from tasks import cpu_heavy_task  # Import ฟังก์ชันจาก tasks.py

def main():
    num_tasks = 4
    threads = []
    start_time = time.time()

    # สร้างและเริ่ม thread สำหรับแต่ละงาน
    for i in range(num_tasks):
        t = threading.Thread(target=cpu_heavy_task, args=(i,))
        threads.append(t)
        t.start()

    # รอให้ทุก thread เสร็จสิ้น
    for t in threads:
        t.join()

    end_time = time.time()
    print(f"\nใช้เวลาไปทั้งหมด: {end_time - start_time:.2f} วินาที")

if __name__ == "__main__":
    main()