import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())

num_of_cpus = platform.processor()
cpuCount= os.cpu_count()
print('Number of cpus: ', cpuCount)

from psutil import virtual_memory
amount_of_memory = virtual_memory().total
print("Amount of memory is:", amount_of_memory)

import socket
ip_address = socket.gethostbyname(socket.gethostname())
print("Name of IP Address is,", ip_address)

# Compute the CPU strength score
import timeit
def cpu_strength_score():
    s = 0
    for i in range(1,1000):
        s += i
    return s

cpu_strength_score = timeit.timeit(cpu_strength_score)
print("CPU strenght score:", cpu_strength_score)

