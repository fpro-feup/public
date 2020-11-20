#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:19:53 2018

@author: jlopes
"""
# This is a particularly inefficient algorithm, and this could be solved
# far more efficient iteratively or using memoisation


def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t


print("\nStarting...")
print(fib(36))

# using memoisation
alreadyknown = {0: 0, 1: 1}


def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]


print("\nStarting...")
print(fib(720))   # that's 20x
