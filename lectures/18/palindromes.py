#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:11:16 2019

@author: jlopes

Adapted from: https://realpython.com/introduction-to-python-generators/
"""


def infinite_sequence():
    """Generates an infinite sequence."""
    num = 0
    while True:
        yield num
        num += 1


def is_palindrome(num):
    """Tests if num is a palindrome."""
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    return num == reversed_num


# it's better to hit the interrupt
for n in infinite_sequence():
    if is_palindrome(n):
        print(n)
