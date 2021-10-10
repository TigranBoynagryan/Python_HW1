# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:07:12 2021

@author: Tigran Boynagryan
"""

year = int(input())

if year%10 >=1:
    print(year//100+1)
else:
    print(year//100)