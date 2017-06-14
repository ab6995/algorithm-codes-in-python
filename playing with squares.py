# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:08:12 2017

@author: ashishbansal
problem:

Watson gives two integers (A and B) to Sherlock and asks if he can count 
the number of square integers between A and B (both inclusive).


Note: A square integer is an integer which is the square of any integer.
 For example, 1, 4, 9, and 16 are some of the square integers as they are 
 squares of 1, 2, 3, and 4, respectively.




"""

import math
t = int(input())
for _ in range(t):
    a, b = input().strip().split(' ')
    a = int(a)
    b = int(b)
    
    sqrtA = math.ceil(math.sqrt(a))
    sqrtB = math.floor(math.sqrt(b))
    print(sqrtB - sqrtA + 1)