# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 22:31:57 2018

@author: jlopes
"""


def avg(marks):
    assert len(marks) != 0, "List is empty."
    return sum(marks)/len(marks)


# tests
print()
mark2 = [55, 88, 78, 90, 79]
print("Average of mark2:", avg(mark2))

#mark1 = []
#print("Average of mark1:", avg(mark1))

# https://www.programiz.com/python-programming/assert-statement
