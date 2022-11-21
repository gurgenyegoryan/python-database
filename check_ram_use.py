#Method 1

#https://www.geeksforgeeks.org/monitoring-memory-usage-of-a-running-python-program/
#https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/

# importing the module
import tracemalloc

# code or function for which memory
# has to be monitored
def app():
	lt = []
	for i in range(0, 20):
		lt.append(i)

# starting the monitoring
tracemalloc.start()

# function call
app()

# displaying the memory
print(tracemalloc.get_traced_memory())

# stopping the library
tracemalloc.stop()
