#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:39:02 2019

@author: jlopes
"""


# iteractive version
def factorial(n):
    fact = 1
    if n > 1:
        for i in range(2, n+1):
            fact *= i
    return fact


# recursive version
def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial_r(n-1)


# Drive code
n = int(input("Enter a positive integer: "))
print("Factorial of {0} is {1}".format(n, factorial(n)))
print("Factorial of {0} is {1}".format(n, factorial_r(n)))
