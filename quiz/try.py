import time
time_start = time.perf_counter()	
list = []
time_spent = 0
for i in range(20000000):
	list.append(i)
end_time = time.perf_counter()
time_spent += end_time - time_start

print(time_spent)
