#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:13:50 2019

@author: jlopes
"""

cities1 = frozenset(["Frankfurt", "Basel", "Freiburg"])
print(cities1)
# cities1.add("Strasbourg")  # 'frozenset' object has no attribute 'add'

cities2 = frozenset(["London", "Paris", "Madrid"])
print(cities2)

# make a dictionary
population = {}
population[cities1] = 10000000
population[cities2] = 30000000
print(population)

total = 0
for p in population:
    total += population[p]

print("\nTotal =", total)
