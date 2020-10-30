# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 22:18:43 2018

@author: jlopes
"""

### Updating Tuples

tup1 = (12, 34.56)

# Following action is not valid for tuples
# tup1[0] = 100

# So let's create a new tuple as follows
tup1 = (100,) + tup1[1:]
print(tup1)
  
### Delete Tuples
 
#tup = ('physics', 'chemistry', 2017, 2018)
#
#print()
#print(tup)
#
#del tup

#print("After deleting tup : ")
#print(tup)

### Basic Tuples Operations

#tup = (1, 2, 3) + (4, 5, 6)
#print()
#print(tup)

#print()
#print(len((1, 2, 3)))

#print()
#print(('Hi!',) * 4)

#print()
#print(3 in (1, 2, 3))

#print()
#for x in (1, 2, 3):
#    print(x)

### Indexing, Slicing

#L = ('spam', 'Spam', 'SPAM!')
#
#print()
#print(L[2])
#print(L[-2])
#print(L[1:])

### No Enclosing Delimiters

#tup = 'abc', -4.24e93, 18+6.6j, 'xyz'
#
#print()
#print(tup)

### Built-in Tuple Functions

#tuple1, tuple2 = (123, 'xyz', 'zara', 'abc'), (456, 700, 200)
#
#print()
##print("Max value element : ", max(tuple1))
#print("Max value element : ", max(tuple2))
