# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 22:43:29 2018

@author: jlopes
"""

import math

number_list = [10, -5, 1, 2, 'apple']

print()
for number in number_list:
    try:
        number_factorial = math.factorial(number)
    except TypeError:
        print("\nFactorial is not supported for given input type.")
    except ValueError:
        print("\nFactorial only accepts positive integer values.", number, " is not a positive integer.")
    else:
        print("\nThe factorial of", number, "is", number_factorial)
    finally:
        print("Release any resources in use.")


# https://code.tutsplus.com
