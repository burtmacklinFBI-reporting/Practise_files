import time
import threading
from threading import Thread


def sleepMe(i):
    print("Thread %i will sleep." % i) #this is a different notation, the right side value that is %i will be going into the %i in the string like an integer.
    time.sleep(5)
    print("Thread %i is awake" % i) 

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Threads: %i." % threading.active_count())
    

