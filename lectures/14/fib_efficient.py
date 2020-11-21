#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:04:33 2018

@author: jlopes
"""


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
    return ans


d = {0: 0, 1: 1}
print()
print(fib_efficient(7, d))
print(fib_efficient(350, d))
