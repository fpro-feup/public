#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:09:14 2018

@author: Shantanu Sharma

Python program to implement Hofstader Sequence using mutual recursion

https://www.geeksforgeeks.org/mutual-recursion-example-hofstadter-female-male-sequences/
"""


# female function
def h_female(n):
    if n == 0:
        return 1
    else:
        return n - h_male(h_female(n-1))


# male function
def h_male(n):
    if n == 0:
        return 0
    else:
        return n - h_female(h_male(n-1))


# Driver code
print()
print("F:", end=" ")
for i in range(21):
    print(h_female(i), end=" ")
print()
print("M:", end=" ")
for i in range(21):
    print(h_male(i), end=" ")
print()
