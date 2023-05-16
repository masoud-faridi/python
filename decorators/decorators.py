import time
from datetime import datetime
def summary_fn(fn):
    count=0
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tmp=time.perf_counter()
        ret = fn(*args, **kwargs)
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        total_time = time.perf_counter()-tmp
        print("function started: {}\n".format(fn.__name__))
        print("start_time :{} \n".format(start_time))
        print("end_time: {} \n".format(end_time))
        print("total_time: {}\n".format(total_time))
        print("count: {}".format(count))
        return ret
    return inner

import time
from datetime import datetime

def summary_fn(fn):
    """
    A decorator function that prints a summary of the function call.
    The summary includes the number of times the function has been called,
    start time, end time, and total time taken by the function.
    """
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        start_time = time.monotonic()
        ret = fn(*args, **kwargs)
        end_time = time.monotonic()
        total_time = end_time - start_time
        print("Function '{0}' summary:".format(fn.__name__))
        print("  Start time: {0}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        print("  End time: {0}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        print("  Total time: {0:.6f}".format(total_time))
        print("  Count: {0}".format(count))
        return ret
    return inner

def add(a,b):
  return a+b
add=summary_fn(add)

@summary_fn
def pw(a,b):
  return a**b

from math import sqrt
sqrt=summary_fn(sqrt)

add(1,4)
add(2,9)
pw(2,3)
pw(3,2)
sqrt(4)
sqrt(169)

