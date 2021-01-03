# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 17:01:34 2018

@author: jlopes
"""

import random

# Create a black box object that generates random numbers
rng = random.Random()

# Return an int, one of 1, 2, 3, 4, 5, 6
dice_throw = rng.randrange(1, 7)

print()
print(dice_throw)

# scale the results
#print(rng.random() * 5.0)

# randrange can also take an optional step argument
random_odd = rng.randrange(1, 100, 2)

#print()
#print(random_odd)

# create a deck and shuffle the cards
cards = list(range(52))

#print()
#print(cards)

rng.shuffle(cards)
#print()
#print(cards)
# shuffle cannot work directly with a lazy promise

# deterministic random sequence
#print()
#drng = random.Random(123)
#print(drng.random())
#drng = random.Random(123000)
#print(drng.random())
