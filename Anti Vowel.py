# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 23:08:17 2017

@author: ashishbansal
"""

def anti_vowel(text):
    text_final = ""
    for letter in text:
        if letter not in "aeiouAEIOU":
            text_final += letter
    return text_final
    print text_final
anti_vowel("abcd")
