#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 16:34:35 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

def f(n):
    """ Find the first positive integer between 101 and less
        than n that is divisible by 21
    """
    for i in range(101, n):
        if (i % 21 == 0):
            return i
        
print()
print(f(110))
print(f(1000000000))
# In the second test, if range were to eagerly go about building
# a list with all those elements, you would soon exhaust
# your computer’s available memory and crash the program

# Before Python3, range was not lazy
