# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:11:36 2021

@author: Tigran Boynagryan
"""

px=int(input())
py=int(input())
location = [px,py]
moves = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]

all_moves=[]
for i in moves:
    all_moves.append([location[j]+i[j] for j in range(len(location))])
    


for i in all_moves:
    if 1<=i[0]<=8 and 1<=i[1]<=8:
        print(i[0],i[1])