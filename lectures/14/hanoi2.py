#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:26:44 2018

@author: jlopes

Recursive Python function to solve tower of Hanoi

Adapted from:
    https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
"""


def tower_of_Hanoi(n, from_pole, to_pole, aux_pole):
    if n == 1:
        print("Moving disk {0} from {1} to {2}".format(1, from_pole, to_pole))
        return
    tower_of_Hanoi(n-1, from_pole, aux_pole, to_pole)
    print("Moving disk {0} from {1} to {2}".format(n, from_pole, to_pole))
    tower_of_Hanoi(n-1, aux_pole, aux_pole, from_pole)


# Initiate calls from source A to target C with auxiliary B
print("2 =========")
tower_of_Hanoi(2, "A", "C", "B")

print("3 =========")
tower_of_Hanoi(3, "A", "C", "B")

print("4 =========")
tower_of_Hanoi(4, "A", "C", "B")

print("5 =========")
tower_of_Hanoi(5, "A", "C", "B")
