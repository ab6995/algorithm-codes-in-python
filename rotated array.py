# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:00:40 2017

@author: ashishbansal
problem:
John Watson performs an operation called a right circular rotation on an 
array of integers, . After performing one right circular rotation operation,
 the array is transformed from  to .

Watson performs this operation k times. To test Sherlock's ability to 
identify the current element at a particular position in the rotated array
, Watson asks q queries, where each query consists of a single integer,m, 
for which you must print the element at index m in the rotated array 
(i.e., the value ofa[m] ).
"""

import sys

ls = [int(x) for x in input().split()]
n = ls[0]
k = ls[1]
queries = ls[2]
array = [int(x) for x in input().split()]
result = []
for q in range(queries):
    q = int(input())
    result.append(array[q-k % n])
for e in result:
    print(e)