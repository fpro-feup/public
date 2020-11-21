#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:46:21 2018

@author: jlopes
"""


def is_palindrome_iter(s):
    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def is_pal(s):
        # Using predefined function to reverse to string
        rev = ''.join(reversed(s))
        # Checking if both string are equal or not
        if (s == rev):
            return True
        return False

    return is_pal(to_chars(s))


print()
print(is_palindrome_iter("Aba"))
print(is_palindrome_iter("Able was I, ere I saw Elba"))
