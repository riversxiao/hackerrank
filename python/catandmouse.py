#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if abs(z-x)==abs(z-y):
        print("Mouse C")
    else:
        [print("Cat B") if abs(z-x)>abs(z-y) else print("Cat A")]
