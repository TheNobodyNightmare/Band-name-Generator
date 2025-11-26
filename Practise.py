import time

def measure(func, *args):
    t0 = time.time()
    result = func(*args)
    t1 = time.time()
    return result, (t1 - t0)

