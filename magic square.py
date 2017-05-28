# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:16:31 2017

@author: ashishbansal
problem:
We define a magic square NXN to be an  matrix of distinct positive integers
 from 1 to N^2  where the sum of any row, column, or diagonal (of length N ) 
 is always equal to the same number (i.e., the magic constant).

Consider a matrix,3X3,of integers in the inclusive range{1,9}.We can convert 
any digit,a, to any other digit,b,in the range{1,9} at cost|a-b| .

Given s,convert it into a magic square at minimal cost by changing zero or more
 of its digits. Then print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the 
inclusive range {1,9} .


"""
m =     [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

matrix = []

for i in range(3):
    matrix.append(list(map(int, input().strip().split(' '))))

mincost = 81

for item in m:

    curr = 0
    for i in range(3):
        for j in range(3):
            curr += abs(matrix[i][j] - item[i][j])

    mincost = min(curr, mincost)

print (mincost)

