
import time
import sys

def show_time(f):

    def wrapper(*args, **kvargs):
        t1 = time.time()
        r=f(*args, **kvargs)
        t2 = time.time()
        print('Время', t2-t1)
        print('Память', sys.getsizeof(r))
    return wrapper

@show_time
def list_get(n):
    list_n = []
    for i in range(1, n+1):
        list_n.append(i)
    return list_n

@show_time
def list_gen(n):
    list_g = [i for i in range(1, n+1)]
    return list_g

@show_time
def list_sgen(n):
    list_sg = (i for i in range(1, n+1))
    return list_sg

@show_time
def list_gener(n):
    for i in range(1, n+1):
        yield(i)

list_get(1000000)

list_gen(1000000)

list_sgen(1000000)

list_gener(1000000)
