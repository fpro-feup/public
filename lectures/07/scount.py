#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:24:04 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

def count_a(text):
    count = 0
    for letter in text:
        if letter == "a":
            count += 1
    return count


print()
print(count_a("banana") == 3)
