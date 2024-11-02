from collections import deque
import time
import threading
orders = ['pizza','samosa','pasta','biryani','burger']
place_order, serve_order = deque(), deque()

def placing_order(input):
    for i in input:
     place_order.appendleft(i)
     time.sleep(0.5)

def serving_order():
 time.sleep(1)
 while True:
    if len(place_order)== 0:
      print('Que is empty')
      time.sleep(2)
      break
    else:
        popped_order =  place_order.pop()
        serve_order.append(popped_order)
        print(f'The served order is {popped_order}')
    time.sleep(2)

t1 = threading.Thread(target=placing_order,args=(orders,))
t2 = threading.Thread(target=serving_order)

t1.start()
t2.start()

t1.join()
t2.join()
print('The entire thread is completed')


empty_list,new_list = deque(),deque()
# for i in range(1,11):
#     x = ((bin(i))[2:])
#     print(x)

empty_list.appendleft(1)
def front(input):
    return input[len(empty_list) - 1]

while len(new_list)<10:
        empty_list.appendleft(int(str(front(empty_list))+'0'))
        empty_list.appendleft(int(str(front(empty_list))+'1'))
        new_list.append(empty_list.pop())

for i in new_list:
   print(i)
