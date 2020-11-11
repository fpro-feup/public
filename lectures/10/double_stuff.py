#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:56:14 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

print()
######### a modifier or inpure function
def double_stuff(a_list):
    """ Overwrite each element in a_list with double its value. """
    for (index, stuff) in enumerate(a_list):
        a_list[index] = 2 * stuff


things = [2, 5, 9]
print(things)
double_stuff(things)
print(things)

print()
######### a version as pure function (does not change its arguments)
def double_stuff2(a_list):
    """ Return a new list which contains
        doubles of the elements in a_list.
    """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
double_stuff2(things)
print(things)
things = double_stuff2(things)
print(things)

# first evaluate the right hand side, then assign the resulting value
# to the variable
