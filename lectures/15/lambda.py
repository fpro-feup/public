# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 20:23:15 2018

@author: jlopes
"""

job_data = [
   ('121', 'Yates', 'NY', 5094),
   ('122', 'Wyoming', 'NY', 8722),
   ('001', 'Albany', 'NY', 162692),
   ('003', 'Allegany', 'NY', 11986),
   ]

job_data.sort(key=lambda x: x[1])

print()
print(job_data)


# parametrised lambda
spins = [(23, "red"), (21, "red"), (0, "green"), (24, "black")]


def by_color(color):
    return lambda t: color == t[1]

print()
print(spins)
print(list(filter(by_color("red"), spins)))
print(list(filter(by_color("green"), spins)))

# using it in comprehensions
by_red = by_color("red")
print()
print([s for s in spins if by_red(s)])  # [(23, 'red'), (21, 'red')]
