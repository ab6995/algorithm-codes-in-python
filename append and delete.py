# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:08:12 2017

@author: ashishbansal
problem:

You have a string,s, of lowercase English alphabetic letters. 
You can perform two types of operations on s :

Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on
 an empty string results in an empty string.
Given an integer,k, and two strings,s and t, determine whether or not
 you can convert s to t by performing exactly k of the above operations on s .
 If it's possible, print Yes; otherwise, print No.



"""

s = input().strip()
t = input().strip()
k = int(input().strip())

numSameChars = min(len(s), len(t))
for i in range(len(t)):
    if s[:i] != t[:i]:
        numSameChars = i-1
        break

diff = len(s)-numSameChars + len(t)-numSameChars
print('Yes' if (diff <= k and diff%2 == k%2) or len(s) + len(t) < k else 'No')
