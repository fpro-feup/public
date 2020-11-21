#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:48:27 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


def function_a(n):     # Do things associated with state A
    if n == 0:
        return
    print('a')
    function_b(n - 1)  # Proceed to state B


def function_b(n):     # Do things associated with state B
    if n == 0:
        return
    print('b')
    function_a(n - 1)  # Proceed to state A


print()
function_a(5)
#print()
#function_b(5)
