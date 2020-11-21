# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:50:03 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


# This is a particularly inefficient algorithm, and this could be solved
# far more efficient iteratively or using memoisation
def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t


import time

def computing(n):
    print("Computing... ", end="", flush=True)
    t0 = time.clock()
    result = fib(n)
    t1 = time.clock()
    print()
    print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

nn = [10, 20, 30, 35, 40]
for n in nn:
    computing(n)

