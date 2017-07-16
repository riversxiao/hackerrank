#!/bin/python3

import sys

from itertools import combinations
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]


print (len([1 for t in combinations(a,2) if sum(t)%k ==0]))
