""" TWO WAYS TO PRINT LADDER OF N ELEMENTS  SUCH AS N =4
   #
  ##
 ###
####
SAMPLE INPUT:
N = 6
SAMPLE OUTPUT WILL BE:
     #
    ##
   ###
  ####
 #####
######"""
import sys
#FIRST WAY 
n = int(input())
for i in range(1,n+1):
    print(('#'*i).rjust(n,' '))
#SECOND WAY     
    
    
n = int(input())
for i in range(1,n+1):
    print (" "*(n-i) + "#"*i)
