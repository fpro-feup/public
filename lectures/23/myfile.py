# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:18:54 2018

@author: jlopes
"""

# With mode "w", if there is no file named first.txt on the disk, it will
# be created. 
# If there already is one, it will be replaced by the file we are writing

with open("first.txt", "w") as myfile:
    myfile.write("My first file written from Python\n")
    myfile.write("---------------------------------\n")
    myfile.write("Hello, world!\n")

print("\nDone.\n")

#with open("first.txt", "r") as my_handle:
#    for the_line in my_handle:
#        # Do something with the line we just read. Here we just print it.
#        print(the_line, end="")

#f = open("foo.txt", "r")  # FileNotFoundError
