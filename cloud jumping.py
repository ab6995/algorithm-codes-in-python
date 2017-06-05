# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:08:12 2017

@author: ashishbansal
problem:

YAerith is playing a cloud game! In this game, there are  clouds 
numbered sequentially from  to . Each cloud is either an ordinary 
cloud or a thundercloud.

Aerith starts out on cloud  with energy level . She can use  unit 
of energy to make a jump of size  to cloud , and she jumps until
 she gets back to cloud . If Aerith lands on a thundercloud, her
 energy () decreases by  additional units. The game ends when 
 Aerith lands back on cloud .

Given the values of , , and the configuration of the clouds,
 can you determine the final value of  after the game ends?



"""

import sys

n, k  = map(int, input().strip().split())
clouds = list(map(int, input().strip().split()))
print(100 - sum(1 + 2 * clouds[i] for i in range(0, n, k)))