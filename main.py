import psutil
import time

print("Hello, World!")

for i in range (10):
    # Get the current CPU usage
    cpu_percent = psutil.cpu_percent()
    
    # Get the current memory usage
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent

    # Print the results
    print("CPU Usage:", cpu_percent, "%")
    print("Memory Usage:", memory_percent, "%")

    # Wait for 10 seconds
    time.sleep(10)
