#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:53:27 2019

@author: jlopes

Adapted from: https://www.geeksforgeeks.org/python-sets/
"""

from string import ascii_lowercase as asc_lower

print(len(asc_lower), asc_lower)
print()


def is_pangram(s):
    """
    Function to check if all elements are present or not
    """
    return set(asc_lower) - set(s.lower()) == set()


# tests
strng1 = "The quick brown fox jumps over the lazy dog"
strng2 = "geeks for geeks"
strngs = [strng1, strng2]

for s in strngs:
    if is_pangram(s):
        print("The string '{0}' is a pangram".format(s))
    else:
        print("The string '{0}' isn't a pangram".format(s))
