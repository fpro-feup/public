# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 21:37:45 2018

@author: jlopes
"""


def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")


# tests
print()
recursion_depth(0)
