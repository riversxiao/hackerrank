def g(p,n):
    return (1-p)**(n-1)*p
a,b = map(int,input().split())
n = int(input())
p = a/b
print (round(g(p,n),3))
