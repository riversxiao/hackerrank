#!/bin/python3

import sys


arr = []
for arr_i in range(6):

    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
patch=[]
for j in range(4):
    for x in range(4):
        t= sum(arr[j][x:x+3])+arr[j+1][x+1]+sum(arr[j+2][x:x+3])
        patch.append(t)
print (max(patch))
