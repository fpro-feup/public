# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:28:52 2018

@author: jlopes
"""

user_input = input("Type a number: ")

try:
    # Try do do something that could fail.
    user_input_as_number = float(user_input)
except ValueError:
    # This will be executed if a "ValueError" is raised
    print("You did not enter a number.")
else:
    # This will be executed if not exception got raised in the "try"
    print("The square of your number is ", user_input_as_number**2)
finally:
    # This will be executed whether or not an exception is raised
    print("Thank you.")
