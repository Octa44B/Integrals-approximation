from math import exp
import threading
import time

s=0
a,b= 1,2
nThreads=4 #Number of threads to operate on, the functions will work on their own without multithreading so you can copy paste them in your code
lock = threading.Lock()

#Function to integrate
def fun(x):
    return x**2

### INTEGRALS APPROXIMATION METHODS
def midintegral(a,b,fun,n):
    """
    Integral of f from a to b with mid rectangles method
    Higher n means higer precision and more accurate results
    """
    global s
    ls = 0
    dx=(b-a)/n
    i=a
    while i<b:
        ls+=dx*fun(i+(dx/2))
        i+=dx
    with lock:
        s += ls

dx=1e-5
def trapintegral(a:float,b:float,f,dx:float):
    """
    Integral of f from a to b with traps method
    Lower dx means higer precision and more accurate results (Recommended: dx>1e-2)
    """
    global s
    ls=0
    i=a
    bmoddx=b%dx
    while i < b:
        ls+=dx*(f(i)+f(i+dx))/2
        i+=dx
    ls+=bmoddx*(f(b-bmoddx)+f(b))/2
    with lock:
        s+=ls

### TO TEST WHICH METHODS IS FASTER AND MORE ACCURATE
#test midintegral
n=33000
threads=[threading.Thread(target=midintegral, args=(a+((i*(b-a))/nThreads),a+((i+1)*(b-a)/nThreads),fun,n/nThreads,)) for i in range(nThreads)]
time1=time.time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(time.time()-time1)
print(s)

#test trapintegral 
s=0
time1=time.time()
threads=[threading.Thread(target=trapintegral, args=(a+((i*(b-a))/nThreads),a+((i+1)*(b-a)/nThreads),fun,dx*nThreads,)) for i in range(nThreads)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(time.time()-time1)
print(s)


