# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:08:12 2017

@author: ashishbansal
problem:

Given an integer,N, traverse its digits (1,2,...,n) and determine how many
 digits evenly divide N (i.e.: count the number of times N divided by
 each digit i has a remainder of 0 ). Print the number of evenly
 divisible digits.



"""

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(len([x for x in list(str(n)) if int(x)!=0 and n%int(x)==0]))
