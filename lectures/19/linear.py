#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:41:08 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3 (RLE), 2012
"""


def search_linear(xs, target):
    """ Don't do this!  """
    """ Find and return the index of target in sequence xs """
    for v in xs:
        if v == target:
            return xs.index(v)
    return -1


#def search_linear(xs, target):
#    """ Find and return the index of target in sequence xs """
#    i = 0
#    while i < len(xs):
#        if xs[i] == target:
#            return i
#        else:
#            i += 1
#    return -1


#def search_linear(xs, target):
#    """ Find and return the index of target in sequence xs """
#    i = -1
#    for v in xs:
#        i += 1
#        if v == target:
#            return i
#    return -1


#def search_linear(xs, target):
#    """ Find and return the index of target in sequence xs """
#    for (i, v) in enumerate(xs):
#        if v == target:
#            return i
#    return -1


ls = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]
print()
print(search_linear(ls, 1))
print(search_linear(ls, 17))
print(search_linear(ls, 53))
