# -*- coding: utf-8 -*-
"""
Created on Thu May 25 23:48:57 2017

@author: ashishbansal
PROBLEM:
Sam's house has an apple tree and an orange tree that yield an abundance of 
fruit. In the diagram below, the red region denotes his house, where  is the 
start point and  is the end point. The apple tree is to the left of his house,
 and the orange tree is to its right. You can assume the trees are located on
 a single point, where the apple tree is at point  and the orange tree is at
 point .When a fruit falls from its tree, it lands  units of distance from its
 tree of origin along the -axis. A negative value of  means the fruit fell 
 units to the tree's left, and a positive value of  means it falls  units to 
 the tree's right.

Given the value of  for  apples and  oranges, can you determine how many apples
 and oranges will fall on Sam's house (i.e., in the inclusive range )? Print 
 the number of apples that fall on Sam's house as your first line of output,
 then print the number of oranges that fall on Sam's house as your second l
 ine of output.
"""
import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))
 