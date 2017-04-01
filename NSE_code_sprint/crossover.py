#!/bin/python3

import sys


import sys
n1 =60
n2 =300
n = int(input().strip())
p = list(map(int, input().strip().split(' ')))
def stma(p,n):
    return list(map(float,[sum(p[i-n1+1:i+1])/n1 for i in range(299,n)]))
def ltma(p,n):
    return list(map(float,[sum(p[i-n2+1:i+1])/n2 for i in range(299,n)]))
st =stma(p,n)
lt =ltma(p,n)

for i in range(len(st)-1):
    if st[i]<lt[i] and st[i+1]>=lt[i+1]:
        print (i+n2+1,float("{0:.2f}".format(st[i+1])),float("{0:.2f}".format(lt[i+1])))
    elif st[i]>lt[i] and st[i+1]<=lt[i+1]:
        print (i+n2+1,float("{0:.2f}".format(st[i+1])),float("{0:.2f}".format(lt[i+1])))
    elif st[i]==lt[i] and st[i+1]!=lt[i+1]:
        print (i+n2+1,float("{0:.2f}".format(st[i+1])),float("{0:.2f}".format(lt[i+1])))
