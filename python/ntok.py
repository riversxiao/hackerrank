#!/bin/python3
# I have to say, I failed most test in this example, so one problem is to
# make this model to be able to take slice algorithm to avoid multiple duplication
import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rawdata = []

for a0 in range(n):
    x_i,w_i = input().strip().split(' ')
    x_i,w_i = [int(x_i),int(w_i)]
    rawdata.append((x_i,w_i))

def k_subset(s, k):
    if k == len(s):
        return (tuple([(x,) for x in s]),)
    k_subs = []
    for i in range(len(s)):
        partials = k_subset(s[:i] + s[i + 1:], k)
        for partial in partials:
            for p in range(len(partial)):
                k_subs.append(partial[:p] + (partial[p] + (s[i],),) + partial[p + 1:])
    return k_subs
def uniq_subsets(s):
    u = set()
    for x in s:
        t = []
        for y in x:
            y = list(y)
            y.sort()
            t.append(tuple(y))
        t.sort()
        u.add(tuple(t))
    return u
t =uniq_subsets(k_subset(rawdata, k))
t =list(t)

def minimal(x):
    data=[]
    for t in x:
        data.append(t[0])
    return min(data)
result =[]

for x in t :
    sums = 0

    for value in x:

        for single in value:

            sums+= ((single[0]-minimal(value))*single[1])

    result.append(sums)

print (min(result))
