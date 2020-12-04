"""
# -*- coding: utf-8 -*-
Created on Mon Dec  3 19:58:14 2018

@author: jlopes
"""

job_data = [
   ('121', 'Yates', 'NY', 5094),
   ('122', 'Wyoming', 'NY', 8722),
   ('001', 'Albany', 'NY', 162692),
   ('003', 'Allegany', 'NY', 11986),
   ]

print()
print(job_data)

# standard sort
job_data.sort()
print()
print(job_data)

# sort by key
def by_state(a):
    return a[1]

job_data.sort(key=by_state)
print()
print(job_data)
