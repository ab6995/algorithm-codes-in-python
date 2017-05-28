# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:11:44 2017

@author: ashishbansal
problem:
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention
 to small details like topography. During his last hike, he took exactly n
 steps. For every step he took, he noted if it was an uphill or a downhill 
 step. Gary's hikes start and end at sea level. We define the following terms:

A mountain is a non-empty sequence of consecutive steps above sea level, 
starting with a step up from sea level and ending with a step down to sea level
A valley is a non-empty sequence of consecutive steps below sea level, starting
 with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and 
print the number of valleys he walked through.



"""
n = int(input())
steps = input()
level = 0
valley = 0
for i in steps:
    if i == 'U':
        level += 1
        if level == 0:
            valley += 1
    else:
        level -= 1
print(valley)