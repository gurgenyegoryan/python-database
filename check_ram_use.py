#Method 1

#https://www.geeksforgeeks.org/monitoring-memory-usage-of-a-running-python-program/
#https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/

# importing the module
# import tracemalloc
#
# # code or function for which memory
# # has to be monitored
# def app():
# 	lt = []
# 	for i in range(0, 20):
# 		lt.append(i)
#
# # starting the monitoring
# tracemalloc.start()
#
# # function call
# app()
#
# # displaying the memory
# print(tracemalloc.get_traced_memory())
#
# # stopping the library
# tracemalloc.stop()


# importing the library
from memory_profiler import profile

# instantiating the decorator
@profile
# code for which memory has to
# be monitored
def my_func():
	x = [x for x in range(0, 1000)]
	y = [y * 100 for y in range(0, 1500)]
	del x
	return y


if __name__ == '__main__':
	my_func()

import os, psutil
process = psutil.Process(os.getpid(python))
print(process.memory_info().rss / 1024)
