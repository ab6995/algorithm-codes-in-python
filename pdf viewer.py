# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:49:37 2017

@author: ashishbansal
Problem:When you select a contiguous block of text in a PDF viewer,
 the selection is highlighted with a blue rectangle. In a new kind of PDF 
 viewer, the selection of each word is independent of the other words; this
 means that each rectangular selection area forms independently around each
 highlighted word.
Consider a word consisting of lowercase English alphabetic letters, where each
 letter is 1mm wide. Given the height of each letter in millimeters (mm), find 
 the total area that will be highlighted by blue rectangle in  when the given
 word is selected in our new PDF viewer. 
"""
import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
lst=[]
for i in word:
    lst.append(h[ord(i)-97])
print((max(lst))*(len(word)))