import numpy as np

n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(input().split())
data = np.array(data, int)
print (np.transpose(data))
print (data.flatten())
