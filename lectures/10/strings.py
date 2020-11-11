#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 16:16:20 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

print()
#### split
song = "The rain in Spain..."
words = song.split()
print(words)

words = song.split("ai")
print(words)

print()
#### join
words = song.split()
glue = ";"
phrase = glue.join(words)
print(phrase)
print(" --- ".join(words))
print("".join(words))
