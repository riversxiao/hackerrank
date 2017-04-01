import math
lamb =float(input())
k = float(input())
def fact(k):
    return 1 if k ==0 else k*fact(k-1)
def p(lamb,k):
    return lamb**k * math.exp(-lamb)/fact(k)
print (round(p(lamb,k),3))
