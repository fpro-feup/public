#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:18:26 2018

@author: jlopes
"""

letter_counts = {}
s = """ 
This parrot is no more! It has ceased to be! 
It’s expired and gone to meet its maker! 
This is a late parrot! It’s a stiff! 
Bereft of life, it rests in peace! 
If you hadn’t nailed it to the perch, it would be pushing up the daisies! 
It’s run down the curtain and joined the choir invisible! 
This is an ex-parrot!
"""
for letter in s:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

print()
print(letter_counts)

# display the frequency table in alphabetical order
letter_items = list(letter_counts.items())  # item gives a promise
letter_items.sort()

print()
print(letter_items)

### NOT for now
# use sorted() for values
