# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 23:08:17 2017

@author: ashishbansal
"""

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


shopping = {
    "banana": 1,
    "apple": 1,
    "orange": 0,
    "pear": 1
}


def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
             
            total = total + prices[item]
            stock[item] = stock[item]-1
    return total 