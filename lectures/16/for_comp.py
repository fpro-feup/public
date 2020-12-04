# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 23:44:47 2018

@author: jlopes
"""

# expression does not depend on for-clause
#zeros = [0 for i in range(10)]
#
#print()
#print(zeros)

# expression depends on the for-clause
#odd = [v*2+1 for v in range(10)]
#
#print()
#print(odd)

# create a dictionary
dict= {k: v for k, v in zip(['a', 'b', 'c'], [1, 2, 3])}
print()
print(dict)

# semantics example
#string = "Hello 12345 World"
#
#print()
#for n in [int(x) for x in string if x.isdigit()]:
#    print(n*n)
