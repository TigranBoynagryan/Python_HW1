# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:54:13 2021

@author: Tigran Boynagryan
"""



gumar = 0
num = int(input())
for i in range(3):
    gumar += num%10
    num = num//10

print(gumar)