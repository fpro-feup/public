# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:41:04 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

import math


def circle_stats(r):
    """ Return (circumference, area) of a circle of radius r """
    circumference = 2 * math.pi * r
    area = math.pi * r * r
    return (circumference, area)

print()
print(circle_stats(1))
