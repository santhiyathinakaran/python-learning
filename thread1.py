from threading import Thread
from datetime import datetime
import time
def first():
	for i in range(1,10):
		print(i)
		time.sleep(1)
def second():
	for i in range(10,20):
		print(i)
		time.sleep(1)
start_time=datetime.now()
start=time.time()
print("starting time:",start_time.strftime("%H:%M:%S"))
t1=Thread(target=first)
t2=Thread(target=second)
t1.start()
t2.start()
t1.join()
t2.join()
end_time=datetime.now()
end=time.time()
print("ending time:",end_time.strftime("%H:%M:%S"))
print("time taken:",round(end-start,2),"seconds")


