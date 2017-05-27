# -*- coding: utf-8 -*-
"""
Created on Fri May 26 23:46:21 2017

@author: ashishbansal
problem :
between two sets
the first line contains two space-separated integers describing the respective
 values n  of(the number of elements in set A ) and m(the number of elements in 
 set B).The second line contains n distinct space-separated integers describing . 
The third line contains m distinct space-separated integers describing .


"""

import sys
from fractions import gcd

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
A = map(int,raw_input().strip().split(' '))
B = map(int,raw_input().strip().split(' '))

def LCM(a, b):
    return (a*b)//gcd(a,b)

lcm = reduce(LCM, A, 1)
gcd = reduce(gcd, B)

lcm_copy = lcm

count = 0
while lcm <= gcd:
    if(gcd % lcm) == 0:
        count += 1
    lcm = lcm + lcm_copy

print(count)
