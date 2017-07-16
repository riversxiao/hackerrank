def fact(n):
    return 1 if n==0 else n*fact(n-1)
def comb(n,x):
    return fact(n)/(fact(x)*fact(n-x))
def b(x,n,p):
    return comb(n,x)*(p**x * (1-p)**(n-x))
rejects, batch = map(int,input().split())
print (round(sum([b(x,batch,rejects/100) for x in range(3)]),3))
print (round(1-sum([b(x,batch,rejects/100) for x in range(2)]),3))
