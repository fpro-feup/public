#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:36:33 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3 (RLE), 2012
"""


def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0        # lower bound
    ub = len(xs)  # upper bound
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
            return -1   # NOT found!

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # comment next if not debugging
        print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
              .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time


ls = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47]
print()
print(search_binary(ls, 1))
print(search_binary(ls, 17))
print()
ls = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]
print(search_binary(ls, 1))
print(search_binary(ls, 17))
