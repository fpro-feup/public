#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:59:10 2018

@author: jlopes
"""


def fib_iter0(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
    return fib_ii


# pythonic version
def fib_iter(n):
    fib1, fib2 = 0, 1
    for _ in range(0, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1


print()
print(fib_iter(7))
print(fib_iter(350))
# Best case: O(1)
# Worst case: O(1) + O(n) + O(1)
