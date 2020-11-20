#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:21:22 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

print()
english_spanish = {"one": "uno", "two": "dos", "three": "tres"}

#### use kyes()
for key in english_spanish.keys():
    # The order of the k's is the order of insertion as of python 3.7
    print("Got key", key, "which maps to value", english_spanish[key])

print()
keys = list(english_spanish.keys())
print(keys)

# Iterating over a dictionary implicitly iterates over its keys
print()
for key in english_spanish:
    print("Got key", key)

#### use values()
print()
values = list(english_spanish.values())
print(values)

#### use items()
print()
print(list(english_spanish.items()))

print()
for (key, value) in english_spanish.items():
    print("Got key", key, "which maps to value", value)

#### membership
print()
print("one" in english_spanish)
print("six" in english_spanish)
# Note that 'in' tests keys, not values
print("tres" in english_spanish)

# looking up a non-existent key in a dictionary causes a runtime error
print()
print(english_spanish["dog"])
