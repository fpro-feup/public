#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:31:53 2018

@author: jlopes
"""

import urllib.request

url = "https://www.ietf.org/rfc/rfc793.txt"
destination_filename = "files/rfc793.txt"

## Using module urllib
#urllib.request.urlretrieve(url, destination_filename)
#
#print("\nWritten in", destination_filename)

## Now with requests
#import requests
#
#response = requests.get(url)
#
#print()
#print(response.text)

# We may as well do
#for line in response:
#    print(line)
