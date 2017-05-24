""" Given n positive integers, find the minimum and maximum values that can
 be calculated by summing exactly  (n-1)of the n integers. Then print the 
 respective minimum and maximum values as a single line of two space-separated
 long integers"""
import sys

nums = [int(x) for x in input().strip().split(' ')]
print(sum(nums) - max(nums), sum(nums) - min(nums))
