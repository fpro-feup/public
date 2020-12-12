#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:36:12 2018

@author: jlopes
"""

def factorialR(n):
    """Recursive factorial function with a assert."""
    assert isinstance(n, int) and n >= 1
    return 1 if n <= 1 else n * factorialR(n-1)

print()
print(factorialR(5))
print(factorialR(0))
print(factorialR('a'))
