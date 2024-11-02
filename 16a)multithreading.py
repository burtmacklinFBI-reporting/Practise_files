# multithreading is very useful when you are working with multiple tasks and you want to utilize the time when the system is asleep.

# Here is a code without multithreading and we are measuring the time it will take to execute the code

import time
def square_list(input):
    print("calculating square of numbers")
    for i in input:
        time.sleep(0.2)
        print(f'This square of {i} is {i**2}')
        
def cube_list(input):
    print("calculating cube of numbers") 
    for i in input:
        time.sleep(0.2)
        print(f'This cube of {i} is {i**3}')

arr = [2,3,4,5,9]
t = time.time() # this line captures the exact time when this function is called
print(f'This is the time.time(): {t}')
square_list(arr)
cube_list(arr)
print(f'This is the later time.time(): {time.time()}') 
print(f'done in: {time.time()-t}') 
# Time taken is 2.0417699813842773
print('hah.. I am done with all of my work now')

# now let me solve the same problem with multithreading.

import time
import threading

def square_list(input):
    print("calculating square of numbers")
    for i in input:
        time.sleep(0.2)
        print(f'This square of {i} is {i**2}')
        
def cube_list(input):
    print("calculating cube of numbers")
    for i in input:
        time.sleep(0.2)
        print(f'This cube of {i} is {i**3}')

arr = [2,3,4,5,9]
t = time.time()


t1 = threading.Thread(target=square_list,args=(arr, ))
t2 = threading.Thread(target=cube_list,args=(arr, ))#n Python, if you want to create a tuple with only one element, you need to add a trailing comma like this. For multiple arguments you wouldnt be needing the trailing comma

t1.start()
t2.start() # both of them will be started parallelly

t1.join()
t2.join() # after the t1 or t2 is done completely join back to main query flow like the mom and the multitasking example in the  word document

print(f'done in: {time.time()-t}') 
#1.0180580615997314 this is the time taken with multithreading almost half of the time than normal one
print('hah.. I am done with all of my work now')


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
    