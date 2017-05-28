# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:16:31 2017

@author: ashishbansal
problem:
Dan is playing a video game in which his character competes in a hurdle
 race by jumping over n hurdles with heights [h1...h(n-1)]. 
 He can initially jump a maximum height of k units, but he has an unlimited
 supply of magic
 beverages that help him jump higher! Each time Dan drinks a magic beverage,
 the maximum height he can jump during the race increases by 1 unit.

Given n,k ,and the heights of all the hurdles, find and print the 
minimum number of magic beverages Dan must drink to complete the race.
"""
import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
h = max(height)
sol = 0
if h > k:
    sol = h - k
else:
    sol = sol
print(sol) 