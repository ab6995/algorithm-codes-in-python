# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:49:37 2017

@author: ashishbansal
Problem:John's clothing store has a pile of n loose socks where each
 sock i is labeled with an integer,c[i] , denoting its color. He wants to
 sell as many socks as possible, but his customers will only buy them
 in matching pairs. Two socks,i and j, are a single matching pair ifc[i]=c[j] .

Given n and the color of each sock, how many pairs of socks can John sell? 
"""
import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
print (sum(c.count(x)//2 for x in set(c)))
