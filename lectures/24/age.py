# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 21:25:19 2018

@author: jlopes
"""

def get_age(age):
    if age < 0 or age > 120:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age".format(age))
        raise my_error
    return age

age = int(input("Please enter your age: "))
print(get_age(age))
