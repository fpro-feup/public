# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 21:33:44 2018

@author: jlopes
"""


def any_odd(xs): # Buggy version
    """
    Return True if there is an odd number in xs, a list of integers.
    """
    for v in xs:
        if v % 2 == 1:
            return True
        else:
            return False

print()
print(any_odd([1, 2, 3]))  # True
print(any_odd([2, 3]))     # False
print(any_odd([]))         # None


def any_odd(xs):
    """
    Return True if there is an odd number in xs, a list of integers.
    """
    for v in xs:
        if v % 2 == 1:
            return True
    return False

print()
print(any_odd([1, 2, 3]))  # True
print(any_odd([2, 3]))     # True
print(any_odd([]))         # False
#
#
#def any_odd(xs):
#    """
#    Return True if there is an odd number in xs, a list of integers.
#    """
#    count = 0
#    for v in xs:
#        if v % 2 == 1:
#            count += 1  # Count the odd numbers
#    return count > 0    # Aha! a programmer who understands that Boolean
#                        # expressions are not just used in if statements!
#
#print()
#print(any_odd([1, 2, 3]))  # True
#print(any_odd([2, 3]))     # True
#print(any_odd([]))         # False
