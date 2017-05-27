# -*- coding: utf-8 -*-
"""
Created on Fri May 26 23:46:21 2017

@author: ashishbansal
problem :
between two sets
The first line contains an integer denoting n (the number of games). 
The second line contains  space-separated integers describing the respective
 values of s0,s1....sn-1 .
 
Print two space-seperated integers describing the respective numbers of times 
her best (highest) score increased and her worst (lowest) score decreased.


"""

import sys



n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
def getRecord(s):
    # Complete this function
    high_score = s[0]
    low_score = s[0]
    best, worse = 0,0
    for score in s:
        if score > high_score:
            best += 1
            high_score = score
        
        if score < low_score:
            worse += 1
            low_score = score
            
    return [best, worse]

result = getRecord(s)
print (" ".join(map(str, result)))
