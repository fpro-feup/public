# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:35:11 2018

@author: jlopes

Time and compare pop() with pop(0).
The dataset gets bigger by 10^6 each cicle and there's 10^3 executions for
each measurement for more accuracy.
"""

import timeit

# print the header
print("\n{:>9s} {:>9s} {:>10s}".format("len(x)", "in list", "in set"))


# start by 100 000 and increase by 100 000 in each iteration
SIZE = 10**5
# repeat each operations 1 000 times
REP = 10**3
for size in range(SIZE, 12*SIZE+1, SIZE):

    # find 900 000 in list
    tl_stmt = "9*10**5 in c"                           # the operation
    tl_setup = "c = list(range(" + str(size) + "))"    # the list gets bigger
    pl = timeit.timeit(tl_stmt, tl_setup, number=REP)  # timeit for 1000 pops

    #  find 900 000 in dict
    ts_stmt = "9*10**5 in s"                           # the operation
    ts_setup = "s = set(range(" + str(size) + "))"     # the set gets bigger
    ps = timeit.timeit(ts_stmt, ts_setup, number=REP)  # timeit for 1000 pops

    # print the results
    print("{:9d} {:9.5f} {:10.5f}".format(size, pl, ps))

print("The Winter is coming!")
