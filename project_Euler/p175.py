memo={0:1,1:1}
def p2(n):
    if not n in memo:
        if n%2 ==1:
            return p2((n-1)/2)
        memo[n]=p2(n/2)+p2(n/2-1)
    return memo[n]
def findnum(x,y):
    n=1
    while not(p2(n)==x and p2(n-1)==y):
        n+=1
    return n

t = "{0:b}".format(findnum(13,17))
from itertools import groupby
s = [len(list(value)) for key, value in groupby(t)]


",".join([str(i) for i in s])
