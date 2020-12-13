#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:35:32 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3 (RLE), 2012
"""


# utility function
def load_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    return file_content


# In a sorted list, to remove dups, we simply have to remember the most recent
# item that was inserted into the result, and avoid inserting it again
def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent duplicates from xs
        have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result


# Books are full of punctuation, and have mixtures of lowercase and uppercase
# letters. We need to clean up the contents of the book. This will involve
# removing punctuation, and converting everything to the same case
# (lowercase, because our vocabulary is all in lowercase)
def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """
    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")
    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


# clean book
def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    file_content = load_from_file(filename)
    wds = text_to_words(file_content)
    return wds


# Now we're ready to read in our book
all_words = get_words_in_book("AliceInWonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)
print()
print("There are {0} words in the book. Only {1} are unique."
      .format(len(all_words), len(book_words)))
print("The first 12 words are:\n{0}".format(book_words[:12]))
