#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:35:32 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3 (RLE), 2012
"""

import time


# utility function
def load_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    return file_content


# split vocabulary in words
def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    file_content = load_from_file(filename)
    wds = file_content.split()
    return wds


# now read a sensible size vocabulary
bigger_vocab = load_words_from_file("vocab.txt")
#print()
#print("There are {0} words in the vocab, starting with\n {1} "
#      .format(len(bigger_vocab), bigger_vocab[:6]))


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


# Instead of searching for every word in the dictionary (either by linear or
# binary search), why not use a variant of the merge to return the words that
# occur in the book, but not in the vocabulary.
def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted.  Return a new
        list of words from wds that do not occur in vocab.
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:   # Good, word exists in vocab
            yi += 1

        elif vocab[xi] < wds[yi]:  # Move past this vocab word,
            xi += 1

        else:                      # Got word that is not in vocab
            result.append(wds[yi])
            yi += 1


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
print()
print("Finding missing words...", end='')
t0 = time.perf_counter()
all_words.sort()
book_words = remove_adjacent_dups(all_words)
missing_words = find_unknowns_merge_pattern(bigger_vocab, book_words)
t1 = time.perf_counter()
print(" took {0:.4f} seconds.".format(t1-t0))
print()
# Even more stunning performance here:
print("There are {0} unknown words.\nStarting with:\n{1}"
      .format(len(missing_words), missing_words[:12]))
