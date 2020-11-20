#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:21:22 2018

@author: jlopes

Adapted from: https://www.geeksforgeeks.org/python-sets/
"""


def intersect_lists(l1, l2, l3):
    # Converting the lists into sets
    s1 = set(l1)
    s2 = set(l2)
    s3 = set(l3)

    # Calculates intersection of sets on s1 and s2
    set1 = s1.intersection(s2)

    # Calculates intersection of sets on set1 and s3
    result_set = set1.intersection(s3)

    # Converts resulting set to list
    return list(result_set)


# Elements in List1
list1 = [1, 5, 10, 20, 40, 80, 100]

# Elements in List2
list2 = [6, 7, 20, 80, 100]

# Elements in List3
list3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(intersect_lists(list1, list2, list3))  # [80, 20]
