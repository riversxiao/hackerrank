#!/bin/python3

import sys


n = int(input().strip())
score = list(map(int, input().strip().split(' ')))
# your code goes here
result={"best":[],
     "worst":[]}
best=score[0]
worst=score[0]
for i in score:
    if i>best:

        best = i
        result['best'].append(1)
    elif i<worst:
        worst =i
        result['worst'].append(1)
print ("{0} {1}".format(sum(result["best"]),sum(result["worst"])))
