array, m ,n =[input().split() for x in range(4)][1:]
m= set(m)
n= set(n)
data =[]
[data.append(1) for x in array if x in m]
[data.append(-1) for y in array if y in n]
print (sum(data))
sum([(i in A) - (i in B) for i in array])
