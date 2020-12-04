# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 23:54:21 2018

@author: jlopes
"""

import random

square = sum((2*a+1) for a in range(10))

print()
print([(2*a+1) for a in range(10)])
print("Sum =", square)

#column_1 = tuple(3*b+1 for b in range(12))
#
#print()
#print(column_1)

# defines an iterator that will produce 100 values
rolls = ((random.randint(1,6), random.randint(1,6)) for u in range(100))


hardways = any(d1 == d2 for d1, d2 in rolls)

print()
print(hardways)

# this generator has an internal state: it can only be used once.
print("rolls")
for t in rolls:
    print(t)
print("rolls again")
for t in rolls:
    print(t)
