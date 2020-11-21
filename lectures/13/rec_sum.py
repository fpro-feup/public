# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:25:59 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


def recursive_sum(nested_number_list):
    """
    Returns the total sum of all elements in nested_number_list
    """
    print("called with: ", nested_number_list)
    total = 0
    for element in nested_number_list:
        if type(element) is list:
            total += recursive_sum(element)
        else:
            total += element
    return total


print()
print(recursive_sum([1, 2, [11, 13], 8]))
print()
print(recursive_sum([]))
