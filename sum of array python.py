""" SIMPLE ARRAY SUM
SAMPLE INPUT:
1 2 3 4 10 11
SAMPLE OUTPUT WILL BE:
31"""
import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print (sum(arr))

