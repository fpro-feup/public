#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:34:23 2018

@author: jlopes
"""

print()
# nested exceptions 1
try:
    try:
        raise ValueError('1')
    except TypeError:
        print("Caught the type error")
except ValueError:
    print("Caught the value error!")

# nested exceptions 2
#try:
#    try:
#        raise ValueError('1')
#    except TypeError:
#        pass
#    except ValueError:
#        print("Caught the inner valueError!")
#except ValueError:
#    print("Caught the outer value error!'")
