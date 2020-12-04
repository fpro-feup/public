# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:44:20 2018

@author: jlopes
"""

# multiple assignment to work with a list of tuples
print()
for c, f in [("red", 18), ("black", 18), ("green", 2)]:
    print("{0} occurs {1}".format(c, f/38.0))


# the same using a dictionary and items()
#print()
#d = {'red':18, 'black':18, 'green':2}
#for c, f in d.items():
#    print("{0} occurs {1}".format(c, f/38.0))


# yet another example
#print()
#for r, g, b in [(0,0,0), (0x20,0x30,0x20), (0xff,0xff,0xff)]:
#    print("red: {0}, green: {1}, blue: {2}".format(255-r, 255-g, 255-b))
