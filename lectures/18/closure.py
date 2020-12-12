#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:52:16 2018

@author: jlopes

David Mertz, Functional Programming in Python
"""


def make_adder(n):
    times = 10

    def adder(m):
        return times * (m + n)

    return adder


add5_f = make_adder(5)  # "functional"

print()
print(add5_f(100))       # 150
