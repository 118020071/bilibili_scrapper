#!/usr/bin/env python
#-*- coding: utf8 -*-
 
import sys
import time
import string
import threading
import datetime

## Try 1

# def func(y):
#     print('round 1, 1s sleep', y)
#     time.sleep(1)
#     print('done')

# x = threading.Thread(target=func, args=(0,))#pass argument in the args=()

# x.start() # start new thread x

# print(threading.activeCount())

## Try 2

# def func(n, litera, loop):

#     for i in range(1, n+1):
#         print("Loop",loop,"literation:", litera, "at", i)
#         time.sleep(0.01)

# def func2(n, litera, loop):

#     for i in range(1, n+1):
#         print("Loop",loop,"literation:", litera, "at", i)
#         time.sleep(0.02)


# x = threading.Thread(target=func, args=(10, 1))
# x.start()#start 1 threads

# y = threading.Thread(target=func, args=(10, 2))
# y.start()#start 2 threads

# threadL = []

# for i in range(1,10):
#     if (i%2 != 0):
#         x = threading.Thread(target=func, args=(10,1, i))
#     else:
#         x = threading.Thread(target=func2, args=(10, 2, i))
    
#     x.start()
#     threadL.append(x)

# for i in threadL:
#     i.join()

#Thread synchronazation
# x.join() #do not pass this line until all threads in x is done
# y.join()

def func2(q, value, w):
    print("func 2", "loop1", q, "loop2", w)
    value["loop1-%d-loop2-%d"%(q,w)] = value.get("loop1-%d-loop2-%d"%(q,w), -q**2)
    time.sleep(0.2)

def func(j,value):
    # print("func at loop",i)
    print("func 1", "loop", j)
    value["loop1-%d"%j] = value.get("loop1-%d"%j, j**2)
    tL2 = []
    for k in range(0,10):
        x2 = threading.Thread(target=func2 , args=(k,value, k))
        x2.start()
        tL2.append(x2)

    for i in tL2:
        i.join()

    time.sleep(0.1)

tL = []
value = {}
for i in range(0,10):
    x = threading.Thread(target=func, args=(i,value))
    x.start()
    tL.append(x)


for i in tL:
    i.join()
print(value)

print("Done")