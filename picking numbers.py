# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:16:31 2017

@author: ashishbansal
problem:
Given an array of integers, find and print the maximum number of integers you
 can select from the array such that the absolute difference between any two 
 of the chosen integers is<=1 .


"""
import sys

n=int(input())
a=[int(i) for i in input().split()]
maximum=0
for i in a:
    c=a.count(i)
    d=a.count(i-1)
    c=c+d
    if c > maximum:
        maximum=c
print(maximum)