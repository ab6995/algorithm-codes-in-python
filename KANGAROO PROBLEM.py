# -*- coding: utf-8 -*-
"""
Created on Thu May 25 23:48:57 2017

@author: ashishbansal
PROBLEM:
There are two kangaroos on an x-axis ready to jump in the positive direction 
(i.e, toward positive infinity). The first kangaroo starts at location x1,  and
 moves at a rate of v1,meters per jump. The second kangaroo starts at location 
 x2, and moves at a rate of v2 meters per jump. Given the starting locations
 and movement rates for each kangaroo, can you determine if they'll ever land
 at the same location at the same time?


"""
import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if v1 > v2 and (x2-x1)%(v1-v2) == 0:
    print ("YES")
else:
    print ("NO")