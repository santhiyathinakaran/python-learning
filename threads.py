
from threading import Thread
def first():
	for i in range(1,101):
		print(i)
def second():
	for i in range(200,301):
		print(i)
		
t1=Thread(target=first)
t2=Thread(target=second)
t1.start()
t2.start()
t1.join()
t2.join()

