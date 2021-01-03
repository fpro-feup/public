# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:49:14 2018

@author: jlopes
"""

with open("files/players.txt") as f:
    content = f.read()
    
words = content.split()

print()
print("There are {0} words in the file.".format(len(words)))
