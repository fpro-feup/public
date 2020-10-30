#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:08:43 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

# assignment is messy and error-prone
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# first take
def remove_punctuation(phrase):
    phrase_sans_punct = ""
    for letter in phrase:
        if letter not in punctuation:
            phrase_sans_punct += letter
    return phrase_sans_punct


#print()
#print(remove_punctuation("Well, I never did!"))
#print(remove_punctuation("Are you very, very, sure?"))

## second take with string
#import string
#
#
#def remove_punctuation(phrase):
#    phrase_sans_punct = ""
#    for letter in phrase:
#        if letter not in string.punctuation:
#            phrase_sans_punct += letter
#    return phrase_sans_punct
#
#
#print()
#print(remove_punctuation("Well, I never did!"))
#print(remove_punctuation("Are you very, very, sure?"))

##Composing together this function and the split method
#my_story = """
#Pythons are constrictors, which means that they will 'squeeze' the life
#out of their prey. They coil themselves around their prey and with
#each breath the creature takes the snake will squeeze a little tighter
#until they stop breathing completely. Once the heart stops the prey
#is swallowed whole. The entire animal is digested in the snake's
#stomach except for fur or feathers. What do you think happens to the fur,
#feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
#you guessed it --- snake POOP! """
#
#words = remove_punctuation(my_story).split()
#
#print()
#print(words)

