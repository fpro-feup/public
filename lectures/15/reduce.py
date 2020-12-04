#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:04:18 2018

@author: jlopes
"""


def plus(a, b):
    return a+b


def oddn(n):
    return 2*n+1


# without reduce()
for i in range(10):
    sq = 0
    for s in map(oddn, range(i)):
        sq = plus(sq, s)
    print(i, sq)

print("Total is {0}".format(sq))

# with reduce()
import functools

sq = functools.reduce(plus, map(oddn, range(i)), 0)
print()
print("Total is {0}".format(sq))
