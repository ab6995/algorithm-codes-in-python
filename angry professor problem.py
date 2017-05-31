# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:49:37 2017

@author: ashishbansal
Problem:A Discrete Mathematics professor has a class of N students.
 Frustrated with their lack of discipline, he decides to cancel class
 if fewer than k students are present when class starts.

Given the arrival time of each student, determine if the class is canceled.
"""
import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    print('YES' if len([i for i in a if i<=0])<k else 'NO')
