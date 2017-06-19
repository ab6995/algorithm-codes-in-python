# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 21:45:19 2017

@author: ashishbansal
problem:Your local library needs your help! Given the expected and
 actual return dates for a library book, create a program that 
 calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will
 be charged (i.e.:fine =0 ).
If the book is returned after the expected return day but still within
 the same calendar month and year as the expected return date,fine= 15 hackos*
(no. of days late) .
If the book is returned after the expected return month but still
 within the same calendar year as the expected return date,the fine= 500hackos*
(no. of months late).
If the book is returned after the calendar year in which it was
 expected, there is a fixed fine of 10000 hackos.

"""
import sys

d1,m1,y1 = list(map(int, input().strip().split(' ')))
d2,m2,y2 = list(map(int, input().strip().split(' ')))

if y1 == y2:
    if m1 < m2:
        print(0)
    elif m1 == m2:
        if d1 <= d2:
            print(0)
        else:
            print(15*(d1-d2))
    else:
        print(500*(m1-m2))
elif y1 < y2:
    print(0)
else:
    print(10000*(y1-y2))

