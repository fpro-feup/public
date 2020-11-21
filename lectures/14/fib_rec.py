#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:55:15 2018

@author: jlopes
"""


def fib_rec(n):
    """ assumes n an int >= 0 """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


print()
print(fib_rec(7))
print(fib_rec(35))
# Worst case O(2^n)
