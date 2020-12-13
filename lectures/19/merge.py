# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:10:48 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3 (RLE), 2012
"""


def merge(xs, ys):
    """ Merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0   # i-th element of xs
    yi = 0   # i-th element of ys

    while True:
        if xi >= len(xs):           # If xs list is finished,
            result.extend(ys[yi:])  # Add remaining items from ys
            return result           # And we're done.

        if yi >= len(ys):           # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


ls1 = friends = ["Joe", "Zoe", "Brad"]
ls2 = friends = ["Angelina", "Zuki", "Thandi", "Paris"]
print()
ls1.sort()
print(ls1)
ls2.sort()
print(ls2)
print()
ls3 = merge(ls1, ls2)
print(ls3)
