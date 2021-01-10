# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:31:15 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

import time


def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

SIZE = 10000000  # Lets have 10 million elements in the list
testdata = range(SIZE)

print('...', flush=True)

t0 = time.perf_counter()
my_result = do_my_sum(testdata)
t1 = time.perf_counter()

print("my_result    = {0} (time taken = {1:.4f} seconds)"
      .format(my_result, t1-t0))

print('...', flush=True)

t2 = time.perf_counter()
their_result = sum(testdata)
t3 = time.perf_counter()
print("their_result = {0} (time taken = {1:.4f} seconds)"
      .format(their_result, t3-t2))
