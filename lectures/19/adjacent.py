# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:30:07 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3 (RLE), 2012
"""


# In a sorted list, to remove dups, we simply have to remember the most recent
# item that was inserted into the result, and avoid inserting it again
def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent duplicates from xs
        have been removed. """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result


ls = friends = ["Joe", "Zoe", "Joe", "Angelina", "Zuki", "Thandi", "Zuki"]
print()
ls.sort()
print(ls)
ls = remove_adjacent_dups(ls)
print(ls)

# The amount of work done in this algorithm is linear — each item in xs causes
# the loop to execute exactly once, and there are no nested loops.
