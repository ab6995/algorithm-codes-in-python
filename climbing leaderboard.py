# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:16:31 2017

@author: ashishbansal
problem:
Alice is playing an arcade game and wants to climb to the top of the 
leaderboard. Can you help her track her ranking as she beats each level? The
 game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number 1 on the leaderboard.
Players who have equal scores receive the same ranking number, and the 
next player(s) receive the immediately following ranking number.
For example, four players have the scores 100,90,90 and 80. Those players will 
have ranks 1,2,2 and 3 respectively.

When Alice starts playing, there are already n people on the leaderboard.
 The score of each player i is denoted by s. Alice plays for m levels, and 
 we denote her total score after passing each j level  as alice j. 
 After completing each level, Alice wants to know her current rank.

You are given an array,scores , of monotonically decreasing leaderboard scores,
 and another array,alice, of Alice's cumulative scores for each level of the 
 game. You must print m integers. The integer should indicate the current
jth rank of alice after passing the jth level.
"""
import sys


n = int(input().strip())
scores = (int,input().strip().split(' '))
m = int(input().strip())
alice = (int,input().strip().split(' '))

i = 0
j = m-1
rank = 1
ranks = []
while i<=(n-1) and j>=0:
    if alice[j]>=scores[i]:
        ranks.append(rank)
        j=j-1
    elif alice[j] < scores[i]:
        i = i+1
        if i!=0 and i!=n:
            if scores[i]!=scores[i-1]:
                rank=rank+1               
if i==n:
    for x in alice[0:j+1]:
        ranks.append(rank+1)     
for i in range(m-1,-1,-1):
    print (ranks[i])