# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:32:12 2018

@author: jlopes
"""


def absolute_value(n):   # Buggy version
    """
    Compute the absolute value of n
    """
    if n < 0:
        return -n
    elif n >= 0:
#    elif n >= 0:
        return n


import sys

def test(did_pass):
    """
    Print the result of a test.
    """
    linenum = sys._getframe(1).f_lineno  # the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """
    Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)


test_suite()        # Here is the call to run the tests
