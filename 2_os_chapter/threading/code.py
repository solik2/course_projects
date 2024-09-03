import threading    
import time

num = 0

def increase_num():
    global num
    for i in range(1000000):
        num += 1

  

def decrease_num():
    global num
    for i in range(1000000):
        num -= 1

def show_num():
    global num
    for i in range(1000):    
        print(num)

    
t1 = threading.Thread(target = increase_num)  #create the thread t1
t2 = threading.Thread(target = decrease_num)  #create the thread t1
t1.start()
t2.start()
# t3 = threading.Thread(target = show_num)  #create the thread t1
# t3.start()

t1.join()
t2.join()
# t3.join()

print(f"main thread: finished and num is => {num}")
