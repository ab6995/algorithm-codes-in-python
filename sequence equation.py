# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:08:12 2017

@author: ashishbansal
problem:

You are given a sequence of n integers,p(1),p(2)...p(n)Each element in the 
sequence is distinct and satisfies . For each  where , find any integer  such 
 that  and print the value of  on a new line.





"""

n = int(input())
p = list(map(int, input().split()))
aDict = dict()
for i in range(len(p)):
    aDict[p[i]] = i + 1

for i in range(1, n+1):
    print(aDict[aDict[i]])