# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:49:37 2017

@author: ashishbansal
Problem:The Utopian Tree goes through 2 cycles of growth every year. 
Each spring, it doubles in height. Each summer, its height increases by 1 
meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of
 spring. How tall will her tree be after N growth cycles?
"""
import sys
def grow(zeit):
    if zeit == 0:
        return 1
    if zeit % 2 == 0:
        return 2 **((zeit/2) + 1) - 1
    else:
        return 2 **((zeit+3) /2) - 2

for a0 in range(int(input().strip())):
    print(int(grow(int(input().strip()))))

