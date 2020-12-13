#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:53:18 2019

@author: jlopes

Comparing four different ways we might generate a list of n numbers
starting with 0

Adapted from: "Brad Miller and David Ranum, Problem Solving with 
Algorithms and Data Structures using Python (Chapter 3)"
"""

# with a for loop and concatenation
def concat(size):
    l = []
    for i in range(size):
        l = l + [i]


# with a for loop and append()
def append(size):
    l = []
    for i in range(size):
        l.append(i)


# using a list comprehension
def comp(size):
    l = [i for i in range(size)]


# using list()
def listf(size):
    l = list(range(size))


# time it 
import timeit

# print the header
print("\n{:>6s} {:>8s} {:>8s} {:>8s} {:>9s} "
      .format("Size", "listf", "comp", "append", "concat"))

# start by 1 000 and increase by 1 000 in each iteration
SIZE = 10**3
# repeat each operations 1 000 times
REP = 10**3
for s in range(SIZE, 6*SIZE+1, SIZE):
    # time listf(s)
    t1 = timeit.timeit("listf(s)", "from __main__ import listf, s", number=REP)
    # time comp(s)
    t2 = timeit.timeit("comp(s)", "from __main__ import comp, s", number=REP)
    # time append(s)
    t3 = timeit.timeit("append(s)", "from __main__ import append, s", number=REP)
    # time concat(s)
    t4 = timeit.timeit("concat(s)", "from __main__ import concat, s", number=REP)
    print("{:>6d} {:>8.5f} {:>8.5f} {:>8.5f} {:>9.5f}"
          .format(s, t1, t2, t3, t4))
