#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:41:13 2018

@author: jlopes
"""

import random

#rolls = list((random.randint(1,6), random.randint(1,6)) for u in range(100))

rolls = []
for u in range(100):
    rolls.append(list((random.randint(1,6), random.randint(1,6))))
print(rolls)

def hardways(pair):
    d1, d2 = pair
    return d1 == d2 and d1+d2 in (4, 6, 8, 10)

frolls = filter(hardways, rolls)

print()
print(list(frolls))
# [(4, 4), (3, 3), (5, 5), (3, 3), (3, 3), (4, 4), (2, 2), (4, 4), (2, 2)]

print()
print(len(list(frolls)))  # 0, why??? 
#print(list(frolls))
