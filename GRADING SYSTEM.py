# -*- coding: utf-8 -*-
"""
Created on Thu May 25 23:48:57 2017

@author: ashishbansal
GRADING SYSTEM FOR UNIVERSITY
"""
import sys
n = int(input().strip())
for i in range(n):
    grades = int(input().strip())
        
    if grades >= 38:
        if grades % 5 > 2:
            grades += 5 - (grades % 5)
    print(grades)
