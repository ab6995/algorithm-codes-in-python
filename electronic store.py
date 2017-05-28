# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:11:44 2017

@author: ashishbansal
problem:
Monica wants to buy exactly one keyboard and one USB drive from her favorite 
electronics store.The store sells n different brands of keyboards and m 
different brands  Monica has exactly s dollars to spend, and she wants to spend 
as much of it as possible(i.e.,the total cost of her purchase must be maximal).


Given the price lists for the store's keyboards and USB drives, find and print
 the amount money Monica will spend. If she doesn't have enough money to buy 
 one keyboard and one USB drive, print -1 instead.

Note: She will never buy more than one keyboard and one USB drive even if she
 has the leftover money to do so.


"""
import sys


def getMoneySpent(key, usb , s):
    su = 0
    for k in key:
        for d in usb:
            if (su < k+d <=s):
                su = k + d
    if su: return su 
    else: return "-1" 
    
s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
key = list(map(int, input().strip().split(' ')))
usb = list(map(int, input().strip().split(' ')))
moneySpent = getMoneySpent(key, usb, s) 
print (moneySpent)
