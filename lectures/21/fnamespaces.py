# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 22:17:20 2018

@author: jlopes
"""


def f():
    n = 7
    print("printing n inside of f:", n)


def g():
    n = 42
    print("printing n inside of g:", n)


n = 11
print()
print("printing n before calling f:", n)
f()
print("printing n after calling f:", n)
g()
print("printing n after calling g:", n)
