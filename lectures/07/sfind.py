#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:13:43 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


def my_find(haystack, needle):
    """
    Find and return the index of needle in haystack.
    Return -1 if needle does not occur in haystack.
    """
    for index, letter in enumerate(haystack):
        if letter == needle:
            return index          # short-circuit evaluation
    return -1


#haystack = "Bananarama!"
#
#print()
#print(my_find(haystack,'a'))
#
## the standard find method
#print(haystack.find('a'))
