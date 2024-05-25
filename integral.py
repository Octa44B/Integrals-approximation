from math import exp
import threading
import time

s=0
a,b,dx= 1,2,1e-5
nThreads=4
lock = threading.Lock()

def fun(x):
    return x**2

def midintegral(a,b,fun,n):
    """
    Integral of f from a to b with mid rectangles method
    Higher n means higer precision and more accurate results
    """
    global s
    ls = 0
    dx=(b-a)/n
    i=a
    while i<=b:
        ls+=dx*fun(i+(dx/2))
        i+=dx
    with lock:
        s += ls

time1=time.time()
threads=[threading.Thread(target=midintegral, args=(a+((i*(b-a))/nThreads),a+((i+1)*(b-a)/nThreads),fun,33333,)) for i in range(nThreads)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(time.time()-time1)
print(s)


s=0

def trapintegral(a:float,b:float,f,dx:float):
    """
    Integral of f from a to b with traps method
    Lower dx means higer precision and more accurate results (Recommended: dx>1e-2)
    """
    global s
    ls=0
    i=a
    bmoddx=b%dx
    while i <= b:
        ls+=dx*(f(i)+f(i+dx))/2
        i+=dx
    ls+=bmoddx*(f(b-bmoddx)+f(b))/2
    with lock:
        s+=ls

time1=time.time()
threads=[threading.Thread(target=trapintegral, args=(a+((i*(b-a))/nThreads),a+((i+1)*(b-a)/nThreads),fun,dx,)) for i in range(nThreads)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(time.time()-time1)
print(s)


