n,s= map(int, input().split())

t=[]
for i in range(s):
    t.append(list(map(float,input().split())))
summary= list(zip(*t))
for i in summary:
    print (round(sum(i)/s,1))
