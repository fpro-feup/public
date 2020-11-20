#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:10:51 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

print()
# my dict
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)

del inventory["pears"]
print(inventory)
#
inventory["bananas"] = 0
print(inventory)

inventory["bananas"] += 200
print(inventory)
#
#print("len", len(inventory))
