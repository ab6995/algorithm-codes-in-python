""" absolute difference of diagnols in a matrin of N X N
SAMPLE INPUT:
3X3 MATRIX
11 2 4
4 5 6
10 8 -12 DIAGNOLS ARE [11,5,-12],[4,5,10]
SAMPLE OUTPUT WILL BE:
Difference: |4 - 19| = 15 """
import sys
n = int(input())
l = []
for i in range(n):
    element = input().split()
    l.append(int(element[i]) - int(element[n-i-1]))
print(abs(sum(l)))
