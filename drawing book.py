# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:11:44 2017

@author: ashishbansal
problem:
The first line contains an integer,n, denoting the number of pages in the book. 
The second line contains an integer,p, denoting the page that Brie's teacher
 wants her to turn to.
Print an integer denoting the minimum number of pages Brie must turn to get to
 page p.

"""
import sys


  

n = int(input().strip())
p = int(input().strip())
print (min(p//2, n//2 - p//2))
