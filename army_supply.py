m,n =input().split()
m,n =int(m),int(n)
rows= 0
if m%2 ==0:
    rows=m//2
else:
    rows = m//2+1
cols= 0
if n%2 ==0:
    cols=n//2
else:
    cols = n//2+1
print(rows*cols)
