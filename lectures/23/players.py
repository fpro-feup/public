# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:49:14 2018

@author: jlopes
"""

with open("files/players.txt", "r") as input_file:
    all_lines = input_file.readlines()

print("\nRead.")

#all_lines.sort()
#
#print("Sorted.")
#
#with open("files/sorted_players.txt", "w") as output_file:
#    for line in all_lines:
#        output_file.write(line)
#
#print("Written.")
