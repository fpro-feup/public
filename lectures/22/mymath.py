# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:58:40 2018

@author: jlopes

my toy math library
"""


def squareit(n):
    return n * n


def cubeit(n):
    return n*n*n


def main():
    anum = int(input("(1) Please enter a number: "))
    print(squareit(anum))
    print(cubeit(anum))


# this source or is it an import?
print("(1)", __name__)

# call main() only if the Python interpreter is running this source file
if __name__ == "__main__":
    main()
