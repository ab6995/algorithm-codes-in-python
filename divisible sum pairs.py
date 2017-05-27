# -*- coding: utf-8 -*-
"""
Created on Fri May 26 23:46:21 2017

@author: ashishbansal
problem :
divisible sum pairs

"""

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')))
# write your code here
count=0
for i in range(len(a) - 1):
    for j in range(1+i , len(a)):
        if (a[i]+a[j])%k == 0:
            count = count + 1
print(count)