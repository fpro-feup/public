#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:29:26 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


def find2(haystack, needle, start):
    for index, letter in enumerate(haystack[start:]):
        if letter == needle:
            return index + start
    return -1


#print()
#print(find2("banana", "a", 2) == 3)


## Better with an optionalparameter
#def find(haystack, needle, start=0, end=-1):
#    for index,letter in enumerate(haystack[start:end]):
#        if letter == needle:
#            return index + start
#    return -1
#
#
#print()
#print(find("banana", "a", 2) == 3)
