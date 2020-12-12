#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:37:38 2018

@author: jlopes
"""

# list vs generator comprehensions
list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)

print()
print(list_comp)
print(gen_exp)
#print(next(iter(gen_exp)))

# list comprehensions
comp_list = [x * 2 for x in range(10)] 

#print()
#print(comp_list)

comp_list = [x ** 2 for x in range(7) if x % 2 == 0]
#print(comp_list)

# dict comprehensions
dict_comp = {x: chr(65+x) for x in range(1, 11)}
#print()
#print(dict_comp)
#print(type(dict_comp))

# an iterable and an iterator
simple_list = [1, 2, 3]
my_iterator = iter(simple_list)
#print()
#print(my_iterator)
#print(next(my_iterator))
#print(next(my_iterator))

# generator expressions
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
#print()
#print(gen_exp)
#for x in gen_exp:
#    print(x)

