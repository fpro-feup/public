#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:02:10 2018

@author: jlopes

Brad Miller and David Ranum, Learning with Python: Interactive Edition.
"""


def listsum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


print()
print(listsum([1, 3, 5, 7, 9]))
